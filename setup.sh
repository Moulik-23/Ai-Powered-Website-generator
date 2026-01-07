#!/bin/bash

# AI Website Generator - Setup Script for Linux/Mac
# Run this script with: chmod +x setup.sh && ./setup.sh

echo "=================================="
echo "AI Website Generator - Setup"
echo "=================================="
echo ""

# Check Python
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ Found: $PYTHON_VERSION"
else
    echo "✗ Python not found. Please install Python 3.9+ from python.org"
    exit 1
fi

# Check Node.js
echo "Checking Node.js installation..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo "✓ Found Node.js: $NODE_VERSION"
else
    echo "✗ Node.js not found. Please install Node.js 18+ from nodejs.org"
    exit 1
fi

# Setup Backend
echo ""
echo "Setting up Backend..."
echo "------------------------------"

cd backend

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create .env file
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Edit backend/.env and add your GEMINI_API_KEY"
    echo "   Get your key from: https://makersuite.google.com/app/apikey"
    echo ""
fi

cd ..

# Setup Frontend
echo ""
echo "Setting up Frontend..."
echo "------------------------------"

cd frontend

# Install dependencies
echo "Installing Node.js dependencies..."
npm install

# Create .env.local file
if [ ! -f .env.local ]; then
    echo "Creating .env.local file..."
    cp .env.local.example .env.local
fi

cd ..

# Final instructions
echo ""
echo "=================================="
echo "Setup Complete!"
echo "=================================="
echo ""
echo "Next Steps:"
echo "1. Edit backend/.env and add your GEMINI_API_KEY"
echo "2. Start MongoDB (if using local installation)"
echo "3. Open TWO terminal windows:"
echo ""
echo "   Terminal 1 (Backend):"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   uvicorn app.main:app --reload --port 8000"
echo ""
echo "   Terminal 2 (Frontend):"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "4. Open browser to http://localhost:3000"
echo ""
echo "For detailed instructions, see QUICKSTART.md"
echo ""
