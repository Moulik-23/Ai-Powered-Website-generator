from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from .routes import generate, projects
from .models.database import Database

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup and shutdown events
    """
    # Startup
    print("Starting up AI Website Generator API...")
    yield
    # Shutdown
    print("Shutting down...")
    await Database.close_connection()


app = FastAPI(
    title="AI Website Generator API",
    description="Generate websites using AI based on natural language prompts",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(generate.router, prefix="/api", tags=["Generate"])
app.include_router(projects.router, prefix="/api", tags=["Projects"])


@app.get("/")
async def root():
    """
    Root endpoint
    """
    return {
        "message": "AI Website Generator API",
        "version": "1.0.0",
        "endpoints": {
            "generate": "/api/generate",
            "projects": "/api/projects",
            "color_schemes": "/api/color-schemes",
            "styles": "/api/styles"
        }
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}
