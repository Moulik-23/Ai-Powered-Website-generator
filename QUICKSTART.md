# AI Website Generator - Quick Start Guide

## Prerequisites Check

Before starting, ensure you have:
- ✅ Python 3.9 or higher
- ✅ Node.js 18 or higher
- ✅ MongoDB installed (local or cloud)
- ✅ Google Gemini API key

## Step 1: Get Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key" or "Create API Key"
4. Copy your API key (keep it secure!)

## Step 2: Setup Backend (FastAPI)

```powershell
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env and add your API key
# GEMINI_API_KEY=your_actual_api_key_here
notepad .env
```

## Step 3: Setup MongoDB

### Option A: Local MongoDB
1. Download and install from [MongoDB Community Server](https://www.mongodb.com/try/download/community)
2. Start MongoDB service
3. Keep default connection string: `mongodb://localhost:27017`

### Option B: MongoDB Atlas (Cloud)
1. Create free account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a cluster
3. Get connection string
4. Update `MONGODB_URL` in `.env`

## Step 4: Start Backend Server

```powershell
# Make sure you're in backend directory with venv activated
uvicorn app.main:app --reload --port 8000
```

Backend will run at: `http://localhost:8000`

## Step 5: Setup Frontend (Next.js)

Open a new terminal:

```powershell
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create .env.local file
copy .env.local.example .env.local

# No need to edit - default settings work!
```

## Step 6: Start Frontend Server

```powershell
# Make sure you're in frontend directory
npm run dev
```

Frontend will run at: `http://localhost:3000`

## Step 7: Test the Application

1. Open browser to `http://localhost:3000`
2. Enter a website description like:
   - "Create a portfolio website for a photographer"
   - "Build a modern landing page for a SaaS startup"
3. Click "Generate Website"
4. Wait 10-30 seconds for AI to generate
5. View, download, or save your website!

## Troubleshooting

### Backend won't start
- Check if Python 3.9+ is installed: `python --version`
- Ensure virtual environment is activated
- Verify GEMINI_API_KEY is set in `.env`

### Frontend won't start
- Check if Node.js 18+ is installed: `node --version`
- Delete `node_modules` and run `npm install` again
- Make sure backend is running first

### MongoDB connection error
- For local: Ensure MongoDB service is running
- For Atlas: Check connection string and IP whitelist

### Gemini API errors
- Verify API key is correct
- Check API quota/limits
- Ensure billing is enabled (if required)

## Development Workflow

1. **Make changes to backend**: Server auto-reloads with `--reload` flag
2. **Make changes to frontend**: Next.js hot-reloads automatically
3. **Test changes**: Refresh browser to see updates

## Next Steps

- Explore different color schemes in Advanced Options
- Save your favorite projects
- Customize components in `backend/app/templates/components.py`
- Add new color schemes in `backend/app/templates/color_schemes.py`

## Getting Help

- Check API status: `http://localhost:8000/health`
- View API docs: `http://localhost:8000/docs`
- Check logs in both terminal windows for errors

Happy generating! 🚀
