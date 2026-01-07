# AI Website Generator

An AI-powered website generator that takes natural language input and automatically generates functional websites with layout, content, and styling.

## Features

- 🤖 Natural language input processing
- 🎨 AI-powered layout and content generation
- 📱 Fully responsive designs (mobile, tablet, desktop)
- 🧩 Reusable UI component library
- 💾 Save and manage generated projects
- 🔄 Real-time preview
- 📝 SEO-friendly content generation

## Tech Stack

### Frontend
- React.js with Next.js
- Tailwind CSS for styling
- Axios for API calls
- React Syntax Highlighter for code preview

### Backend
- Python FastAPI
- Google Gemini API for AI generation
- MongoDB for project storage
- Pydantic for data validation

## Project Structure

```
Talrn/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # Main application
│   │   ├── models/         # Database models
│   │   ├── routes/         # API routes
│   │   ├── services/       # Business logic
│   │   └── templates/      # Component templates
│   ├── requirements.txt
│   └── .env.example
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js app directory
│   │   ├── components/    # React components
│   │   ├── lib/          # Utilities
│   │   └── styles/       # Global styles
│   ├── package.json
│   └── .env.local.example
└── README.md
```

## Setup Instructions

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- MongoDB (local or MongoDB Atlas)
- Google Gemini API Key

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
GEMINI_API_KEY=your_gemini_api_key
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=website_generator
```

5. Run the backend:
```bash
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env.local` file:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Run the development server:
```bash
npm run dev
```

5. Open [http://localhost:3000](http://localhost:3000)

## Usage

1. Enter a description of the website you want to create (e.g., "Create a modern portfolio website for a photographer")
2. Click "Generate Website"
3. Preview the generated website in real-time
4. Download the HTML/CSS/JS files
5. Save projects for later editing

## API Endpoints

- `POST /api/generate` - Generate website from prompt
- `GET /api/projects` - Get all saved projects
- `POST /api/projects` - Save a new project
- `GET /api/projects/{id}` - Get specific project
- `DELETE /api/projects/{id}` - Delete project

## Environment Variables

### Backend
- `GEMINI_API_KEY` - Your Google Gemini API key
- `MONGODB_URL` - MongoDB connection string
- `DATABASE_NAME` - Database name

### Frontend
- `NEXT_PUBLIC_API_URL` - Backend API URL

## License

MIT License
