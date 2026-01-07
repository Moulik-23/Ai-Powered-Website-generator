# AI Website Generator - Setup Script for Windows
# Run this script with PowerShell: .\setup.ps1

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "AI Website Generator - Setup" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.9+ from python.org" -ForegroundColor Red
    exit 1
}

# Check Node.js
Write-Host "Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host "✓ Found Node.js: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found. Please install Node.js 18+ from nodejs.org" -ForegroundColor Red
    exit 1
}

# Setup Backend
Write-Host ""
Write-Host "Setting up Backend..." -ForegroundColor Yellow
Write-Host "------------------------------"

Set-Location backend

# Create virtual environment
Write-Host "Creating Python virtual environment..."
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..."
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing Python dependencies..."
pip install -r requirements.txt

# Create .env file
if (!(Test-Path .env)) {
    Write-Host "Creating .env file..."
    Copy-Item .env.example .env
    Write-Host ""
    Write-Host "⚠️  IMPORTANT: Edit backend\.env and add your GEMINI_API_KEY" -ForegroundColor Yellow
    Write-Host "   Get your key from: https://makersuite.google.com/app/apikey" -ForegroundColor Cyan
    Write-Host ""
}

Set-Location ..

# Setup Frontend
Write-Host ""
Write-Host "Setting up Frontend..." -ForegroundColor Yellow
Write-Host "------------------------------"

Set-Location frontend

# Install dependencies
Write-Host "Installing Node.js dependencies..."
npm install

# Create .env.local file
if (!(Test-Path .env.local)) {
    Write-Host "Creating .env.local file..."
    Copy-Item .env.local.example .env.local
}

Set-Location ..

# Final instructions
Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "1. Edit backend\.env and add your GEMINI_API_KEY" -ForegroundColor White
Write-Host "2. Start MongoDB (if using local installation)" -ForegroundColor White
Write-Host "3. Open TWO terminal windows:" -ForegroundColor White
Write-Host ""
Write-Host "   Terminal 1 (Backend):" -ForegroundColor Yellow
Write-Host "   cd backend" -ForegroundColor White
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "   uvicorn app.main:app --reload --port 8000" -ForegroundColor White
Write-Host ""
Write-Host "   Terminal 2 (Frontend):" -ForegroundColor Yellow
Write-Host "   cd frontend" -ForegroundColor White
Write-Host "   npm run dev" -ForegroundColor White
Write-Host ""
Write-Host "4. Open browser to http://localhost:3000" -ForegroundColor White
Write-Host ""
Write-Host "For detailed instructions, see QUICKSTART.md" -ForegroundColor Cyan
Write-Host ""
