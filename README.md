# AI Medical Assistant

A comprehensive AI-powered medical assistance application built with Flask and Google's Gemini API. This application allows users to ask medical questions, upload and analyze medical reports, and get AI-generated responses with text-to-speech functionality.

## 🌟 Features

- **Natural Language Medical Queries**: Ask medical questions in plain English about symptoms, medications, diet, and general health advice
- **Medical Report Analysis**: Upload images (PNG, JPG, JPEG, GIF) or PDFs of medical reports for AI analysis using OCR
- **Text-to-Speech**: Listen to AI responses with integrated text-to-speech functionality
- **Conversation History**: Keep track of your medical consultations and report analyses
- **Secure Sessions**: Session-based conversation management with SQLite database
- **Responsive Design**: Modern, mobile-friendly interface with Bootstrap

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Tesseract OCR** for text extraction from images
3. **Google Gemini API Key** (free at https://makersuite.google.com/app/apikey)

### Installation

1. **Clone or download this project**
   ```bash
   cd AI-medical-assistance
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR**

   **Windows:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install to default location: `C:\Program Files\Tesseract-OCR\`

   **macOS:**
   ```bash
   brew install tesseract
   ```

   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt-get install tesseract-ocr
   ```

4. **Configure Environment Variables**
   
   Edit the `.env` file and add your API key:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   SECRET_KEY=your-secret-key-for-flask-sessions
   TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe  # Windows
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   Navigate to: http://localhost:5000

## 📋 Usage

### Asking Medical Questions
- Type your question in the chat interface
- Ask about symptoms, medications, diet, treatments, etc.
- Get AI-powered responses with medical disclaimers
- Use the "Listen" button to hear responses

### Uploading Medical Reports
- Drag and drop or click to select image/PDF files
- Supported formats: PNG, JPG, JPEG, GIF, PDF
- OCR extracts text automatically
- AI analyzes and summarizes the content

### Example Questions
- "What are the symptoms of diabetes?"
- "Is it safe to take ibuprofen with high blood pressure medication?"
- "What foods should I avoid with acid reflux?"
- "How can I improve my sleep quality?"

## 🔧 Configuration

### Environment Variables (.env file)

```bash
# Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Flask Configuration
SECRET_KEY=your-secret-key-change-in-production

# Tesseract OCR Path (adjust for your system)
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe  # Windows
# TESSERACT_CMD=/usr/local/bin/tesseract  # macOS
# TESSERACT_CMD=/usr/bin/tesseract  # Linux
```

### Getting a Free Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key
4. Copy and paste it into your `.env` file

## 📁 Project Structure

```
AI-medical-assistance/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── README.md             # This file
├── templates/
│   └── index.html        # Main web interface
├── uploads/              # Temporary file upload directory
└── medical_assistant.db  # SQLite database (created automatically)
```

## 🛠️ Technical Details

### Dependencies
- **Flask**: Web framework
- **google-generativeai**: Gemini AI API client
- **pytesseract**: OCR for text extraction
- **PyMuPDF**: PDF text extraction
- **Pillow**: Image processing
- **gTTS**: Google Text-to-Speech
- **SQLite3**: Database for conversation history

### Database Schema
- **users**: Session management
- **conversations**: Chat history
- **medical_reports**: Uploaded file analyses

### API Endpoints
- `GET /`: Main interface
- `POST /ask`: Submit medical questions
- `POST /upload`: Upload medical reports
- `POST /tts`: Text-to-speech conversion
- `GET /history`: Get conversation history
- `POST /clear_history`: Clear conversation history

## ⚠️ Important Disclaimers

1. **Medical Disclaimer**: This application provides general health information for educational purposes only. Always consult with qualified healthcare professionals for medical diagnosis and treatment.

2. **AI Limitations**: AI responses are generated based on training data and may not always be accurate or up-to-date. Do not rely on AI advice for serious medical conditions.

3. **Privacy**: Conversations are stored locally in a SQLite database. For production use, implement proper security measures.

4. **Emergency**: For medical emergencies, contact your local emergency services immediately.

## 🚀 Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure proper database (PostgreSQL/MySQL)
4. Set up SSL/HTTPS
5. Implement proper logging and monitoring
6. Use environment variables for all secrets

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes. Please ensure compliance with medical AI regulations in your jurisdiction.

## 🆘 Troubleshooting

### Common Issues

1. **Tesseract not found**: Ensure Tesseract is installed and path is correct in `.env`
2. **Gemini API errors**: Check your API key and internet connection
3. **File upload errors**: Ensure upload directory permissions are correct
4. **Database errors**: Delete `medical_assistant.db` to reset database

### Getting Help

- Check the console output for error messages
- Ensure all dependencies are installed correctly
- Verify environment variables are set properly
- Test with simple questions first

---

**Built with ❤️ for better healthcare accessibility using Google Gemini AI**
