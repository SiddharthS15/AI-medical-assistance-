from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import pytesseract
from PIL import Image
import fitz  # PyMuPDF for PDF processing
import gtts
import tempfile
import google.generativeai as genai

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Using system environment variables.")

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# API Configuration
gemini_api_key = os.environ.get('GEMINI_API_KEY')

# Configure Gemini API
if gemini_api_key and gemini_api_key != 'your_gemini_api_key_here':
    genai.configure(api_key=gemini_api_key)
    print("✅ Gemini API configured successfully!")
else:
    print("⚠️  WARNING: Gemini API key not configured!")
    print("Please set GEMINI_API_KEY environment variable or add it to .env file")
    print("Get your free API key at: https://makersuite.google.com/app/apikey")

# Configure Tesseract path if specified
tesseract_cmd = os.environ.get('TESSERACT_CMD')
if tesseract_cmd:
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
else:
    # Default paths for different platforms
    import platform
    if platform.system() == 'Linux':
        pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    elif platform.system() == 'Darwin':  # macOS
        pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Set Flask secret key
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key-for-development')

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_image(image_path):
    """Extract text from image using Tesseract OCR"""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using PyMuPDF"""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def get_ai_response(prompt):
    """Get response from Gemini AI"""
    try:
        # Check if Gemini API is configured
        if not gemini_api_key or gemini_api_key == 'your_gemini_api_key_here':
            return "❌ Gemini API not configured. Please set up your API key in the .env file to use this medical assistant.\n\nGet your free API key at: https://makersuite.google.com/app/apikey\n\n⚠️ DISCLAIMER: This is AI-generated advice for informational purposes only. Please consult with a qualified healthcare professional for proper medical diagnosis and treatment."
        
        # Configure the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the medical prompt
        system_prompt = """You are a helpful medical assistant AI. Provide informative and helpful responses about medical questions, symptoms, treatments, and health advice.

IMPORTANT GUIDELINES:
- Provide accurate, evidence-based medical information
- Be empathetic and supportive
- Never provide definitive diagnoses
- Always recommend consulting healthcare professionals for serious symptoms
- Focus on general health education and guidance
- Keep responses concise but comprehensive

ALWAYS end your responses with this disclaimer:
"⚠️ DISCLAIMER: This is AI-generated advice for informational purposes only. Please consult with a qualified healthcare professional for proper medical diagnosis and treatment."

Remember: You are providing general health information, not replacing professional medical care."""

        full_prompt = system_prompt + "\n\nUser question: " + prompt + "\n\nPlease provide a helpful medical response:"
        
        # Generate response
        response = model.generate_content(full_prompt)
        
        if response.text:
            return response.text.strip()
        else:
            return "I apologize, but I received an empty response. Please try rephrasing your question.\n\n⚠️ DISCLAIMER: This is AI-generated advice for informational purposes only. Please consult with a qualified healthcare professional for proper medical diagnosis and treatment."
                    
    except Exception as e:
        print(f"Gemini API error: {e}")
        return f"I apologize, but I'm having trouble processing your request right now. Error: {str(e)}\n\nPlease try again later. If you have urgent medical concerns, please contact a healthcare professional immediately.\n\n⚠️ DISCLAIMER: This is AI-generated advice for informational purposes only. Please consult with a qualified healthcare professional for proper medical diagnosis and treatment."

def text_to_speech(text, lang='en'):
    """Convert text to speech using gTTS"""
    try:
        # Remove disclaimer text for better audio experience
        clean_text = text.replace("⚠️ DISCLAIMER:", "").replace("Please consult with a qualified healthcare professional for proper medical diagnosis and treatment.", "")
        
        tts = gtts.gTTS(text=clean_text, lang=lang, slow=False)
        
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        tts.save(temp_file.name)
        
        return temp_file.name
    except Exception as e:
        print(f"Error converting text to speech: {e}")
        return None

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    """Handle medical questions"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({'error': 'Please enter a question'}), 400
        
        # Get Gemini response
        ai_response = get_ai_response(question)
        
        return jsonify({
            'response': ai_response,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
    except Exception as e:
        print(f"Error in ask_question: {e}")
        return jsonify({'error': 'An error occurred processing your question'}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads (images and PDFs)"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed. Please upload PNG, JPG, JPEG, GIF, or PDF files.'}), 400
        
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        unique_filename = timestamp + filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        # Extract text based on file type
        extracted_text = ""
        if filename.lower().endswith('.pdf'):
            extracted_text = extract_text_from_pdf(filepath)
        else:
            extracted_text = extract_text_from_image(filepath)
        
        if not extracted_text:
            # Clean up uploaded file
            os.remove(filepath)
            return jsonify({'error': 'Could not extract text from the file. Please ensure the image/PDF contains readable text.'}), 400
        
        # Get AI analysis of the extracted text
        analysis_prompt = f"""Please analyze this medical report/document text and provide a summary:

{extracted_text}

Please provide:
1. A brief summary of the key findings
2. Any important medical information mentioned
3. Recommendations for follow-up if applicable

Remember to include appropriate medical disclaimers."""
        
        ai_analysis = get_ai_response(analysis_prompt)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify({
            'extracted_text': extracted_text,
            'analysis': ai_analysis,
            'filename': filename,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
    except Exception as e:
        print(f"Error in upload_file: {e}")
        return jsonify({'error': 'An error occurred processing the file'}), 500

@app.route('/tts', methods=['POST'])
def text_to_speech_endpoint():
    """Convert text to speech"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        audio_file = text_to_speech(text)
        if not audio_file:
            return jsonify({'error': 'Error generating speech'}), 500
        
        return send_file(audio_file, as_attachment=True, download_name='response.mp3', mimetype='audio/mpeg')
        
    except Exception as e:
        print(f"Error in text_to_speech_endpoint: {e}")
        return jsonify({'error': 'An error occurred generating speech'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
