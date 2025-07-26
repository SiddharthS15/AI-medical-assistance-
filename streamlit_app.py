import streamlit as st
import google.generativeai as genai
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import os
import tempfile
from gtts import gTTS
import base64

# Page config
st.set_page_config(
    page_title="AI Medical Assistant",
    page_icon="🏥",
    layout="wide"
)

# Load environment variables
genai.configure(api_key=st.secrets.get("GEMINI_API_KEY", ""))

st.title("🏥 AI Medical Assistant")
st.markdown("Ask medical questions or upload medical documents for analysis")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Gemini API Key", type="password", value=st.secrets.get("GEMINI_API_KEY", ""))
    if api_key:
        genai.configure(api_key=api_key)
        st.success("API Key configured!")

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Medical Consultation")
    
    # Text input
    question = st.text_area("Ask your medical question:", height=100)
    
    # File upload
    uploaded_file = st.file_uploader("Upload medical document", type=['png', 'jpg', 'jpeg', 'pdf'])
    
    if st.button("Get Medical Advice", type="primary"):
        if question or uploaded_file:
            with st.spinner("Analyzing..."):
                try:
                    # Process uploaded file if any
                    extracted_text = ""
                    if uploaded_file:
                        if uploaded_file.type == "application/pdf":
                            # Process PDF
                            pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                            for page in pdf_document:
                                extracted_text += page.get_text()
                        else:
                            # Process image
                            image = Image.open(uploaded_file)
                            extracted_text = pytesseract.image_to_string(image)
                    
                    # Combine question and extracted text
                    full_prompt = f"""
                    Medical Question: {question}
                    
                    Extracted Document Text: {extracted_text}
                    
                    Please provide medical guidance based on this information. Include disclaimers about consulting healthcare professionals.
                    """
                    
                    # Get AI response
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(full_prompt)
                    
                    # Display response
                    st.header("AI Medical Assistant Response:")
                    st.write(response.text)
                    
                    # Text-to-speech
                    if st.button("🔊 Listen to Response"):
                        tts = gTTS(text=response.text, lang='en')
                        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                            tts.save(tmp_file.name)
                            
                            # Read audio file and encode for HTML
                            with open(tmp_file.name, "rb") as audio_file:
                                audio_bytes = audio_file.read()
                                audio_base64 = base64.b64encode(audio_bytes).decode()
                                audio_html = f"""
                                <audio controls autoplay>
                                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                                </audio>
                                """
                                st.markdown(audio_html, unsafe_allow_html=True)
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a question or upload a document.")

with col2:
    st.header("Important Notice")
    st.warning("""
    🚨 **Medical Disclaimer**
    
    This AI assistant provides general information only and should not replace professional medical advice, diagnosis, or treatment.
    
    Always consult with qualified healthcare professionals for medical concerns.
    """)
    
    st.info("""
    **Features:**
    - Medical Q&A
    - Document OCR analysis
    - Text-to-speech responses
    - Powered by Google Gemini AI
    """)

# Footer
st.markdown("---")
st.markdown("*AI Medical Assistant - For educational purposes only*")
