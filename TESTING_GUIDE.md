# Testing Your AI Medical Assistant

## 🧪 Complete Feature Test Guide

### Prerequisites
1. ✅ Application is running at http://localhost:5000
2. ✅ Gemini API key is configured in .env file
3. ✅ Tesseract OCR is installed (for document analysis)

---

## 🗣️ Testing Medical Question Feature

### Test Questions to Try:

**Basic Health Questions:**
```
What are the symptoms of high blood pressure?
How much water should I drink daily?
What foods are good for heart health?
What are the side effects of ibuprofen?
```

**Symptom-Based Questions:**
```
I have a headache and feel dizzy, what could be causing this?
What should I do if I have persistent cough for 2 weeks?
I'm feeling tired all the time, what might be wrong?
```

**Medication Questions:**
```
Can I take paracetamol with antibiotics?
What's the difference between aspirin and ibuprofen?
Is it safe to take vitamins during pregnancy?
```

**Expected Results:**
- ✅ AI provides helpful medical information
- ✅ Responses include medical disclaimers
- ✅ Conversations are saved in history
- ✅ "Listen" button works for text-to-speech

---

## 📄 Testing Document Upload Feature

### Test Documents to Upload:

**Image Tests:**
1. Take a photo of any medical document with text
2. Supported formats: PNG, JPG, JPEG, GIF
3. Try both clear and slightly blurry images

**PDF Tests:**
1. Upload any PDF with medical text
2. Try both scanned and digital PDFs

**Test Process:**
1. Click "Choose File" or drag & drop
2. Select your test document
3. Wait for processing
4. Check extracted text accuracy
5. Review AI analysis

**Expected Results:**
- ✅ Text is extracted from images/PDFs
- ✅ AI provides analysis and summary
- ✅ Upload appears in conversation history
- ✅ File processing completes without errors

---

## 🔊 Testing Text-to-Speech Feature

**How to Test:**
1. Ask any medical question
2. Wait for AI response
3. Click the "🔊 Listen" button
4. Audio should play the response

**Expected Results:**
- ✅ Audio file downloads/plays
- ✅ Speech is clear and understandable
- ✅ Medical disclaimers are excluded from audio

---

## 📱 Testing User Interface

**Responsive Design:**
- ✅ Test on different screen sizes
- ✅ Mobile-friendly layout
- ✅ Buttons and inputs work properly

**Chat Interface:**
- ✅ Messages appear in correct order
- ✅ User messages align right (blue)
- ✅ AI messages align left (light blue)
- ✅ File uploads have purple indicator
- ✅ Timestamps are visible

**Controls:**
- ✅ "Clear History" button works
- ✅ "Refresh" button reloads page
- ✅ File upload area responds to drag & drop

---

## 🗄️ Testing Database Features

**Conversation History:**
1. Ask several questions
2. Upload a document
3. Refresh the page
4. Check that history persists

**Clear History:**
1. Build up some conversation history
2. Click "Clear History"
3. Confirm deletion
4. Verify history is cleared

**Expected Results:**
- ✅ Conversations persist across page reloads
- ✅ History includes both questions and uploads
- ✅ Clear function removes all data
- ✅ New session starts fresh

---

## ⚠️ Testing Error Handling

**API Errors:**
- Try using without Gemini API key
- Test with invalid API key

**File Upload Errors:**
- Upload unsupported file types (.txt, .doc)
- Upload very large files (>16MB)
- Upload corrupted files

**Network Errors:**
- Test with poor internet connection
- Test text-to-speech offline

**Expected Results:**
- ✅ Clear error messages appear
- ✅ Application doesn't crash
- ✅ Users can continue after errors

---

## 🚀 Performance Testing

**Response Times:**
- Simple questions: < 5 seconds
- Document analysis: < 30 seconds
- Text-to-speech: < 10 seconds

**Memory Usage:**
- Monitor during extended use
- Check for memory leaks
- Test with multiple files

**Concurrent Users:**
- Test multiple browser tabs
- Each should maintain separate sessions

---

## 📋 Feature Checklist

### Core Functionality
- [ ] Ask medical questions
- [ ] Get AI responses with disclaimers
- [ ] Upload image documents (PNG, JPG, JPEG, GIF)
- [ ] Upload PDF documents
- [ ] OCR text extraction
- [ ] AI document analysis
- [ ] Text-to-speech responses
- [ ] Conversation history
- [ ] Session management

### User Interface
- [ ] Responsive design
- [ ] Drag & drop uploads
- [ ] Loading indicators
- [ ] Error messages
- [ ] Success notifications
- [ ] Clear visual hierarchy

### Data Management
- [ ] SQLite database creation
- [ ] Conversation persistence
- [ ] File upload records
- [ ] History clearing
- [ ] Session isolation

### Security & Reliability
- [ ] File type validation
- [ ] File size limits
- [ ] Secure file handling
- [ ] API key protection
- [ ] Error recovery

---

## 🐛 Common Issues & Solutions

**"Gemini API not configured"**
- Solution: Add API key to .env file

**"Tesseract not found"**
- Solution: Install Tesseract OCR and update path in .env

**"Could not extract text"**
- Solution: Use clearer images or different document format

**Text-to-speech not working**
- Solution: Check internet connection, try different browser

**File upload fails**
- Solution: Check file size (<16MB) and format (PNG, JPG, PDF)

---

## 📞 Test Scenarios

### Scenario 1: New User Experience
1. Open application for first time
2. See welcome message
3. Ask simple health question
4. Upload a medical document
5. Clear history and start fresh

### Scenario 2: Power User Workflow
1. Ask multiple related questions
2. Upload several documents
3. Use text-to-speech for responses
4. Review conversation history
5. Continue conversation across sessions

### Scenario 3: Error Recovery
1. Try invalid operations
2. Upload unsupported files
3. Use without API key
4. Test network interruptions
5. Verify graceful error handling

---

**Remember: This is for educational purposes only. Always consult healthcare professionals for real medical advice!**
