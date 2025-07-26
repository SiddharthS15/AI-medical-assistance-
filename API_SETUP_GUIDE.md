# Getting Your Free Gemini API Key

## Step-by-Step Guide

### 1. Visit Google AI Studio
Go to: https://makersuite.google.com/app/apikey

### 2. Sign In
- Sign in with your Google account
- If you don't have one, create a free Google account

### 3. Create API Key
- Click "Create API Key"
- Choose "Create API key in new project" (recommended)
- Copy the generated API key

### 4. Configure Your Application
Open the `.env` file in your AI-medical-assistance folder and replace:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

With your actual API key:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Restart the Application
- Stop the application (Ctrl+C in the terminal)
- Run `python app.py` again
- You should see "✅ Gemini API configured successfully!"

## API Usage Limits
- Gemini API has generous free tier limits
- Perfect for testing and personal use
- No credit card required for the free tier

## Security Note
- Keep your API key secure
- Don't share it publicly
- Don't commit it to version control
- The `.env` file is already configured to be ignored by git

## Troubleshooting
If you see API errors:
1. Double-check your API key is correct
2. Ensure there are no extra spaces
3. Make sure you have internet connectivity
4. Check if you've exceeded rate limits (rare with normal usage)
