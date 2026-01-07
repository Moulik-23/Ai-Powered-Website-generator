from fastapi import APIRouter, HTTPException, Depends
from ..models.schemas import WebsiteRequest, WebsiteResponse
from ..services.ai_service import AIService
from typing import Dict

router = APIRouter()
_ai_service: AIService | None = None

def get_ai_service() -> AIService:
    """Lazy-load AIService to ensure .env is loaded first"""
    global _ai_service
    if _ai_service is None:
        _ai_service = AIService()
    return _ai_service


@router.post("/generate", response_model=WebsiteResponse)
async def generate_website(request: WebsiteRequest) -> Dict:
    """
    Generate a website based on user prompt
    """
    try:
        ai_service = get_ai_service()
        result = await ai_service.generate_website(
            prompt=request.prompt,
            style=request.style,
            color_scheme=request.color_scheme
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating website: {str(e)}"
        )


@router.get("/color-schemes")
async def get_color_schemes():
    """
    Get available color schemes
    """
    from ..templates.color_schemes import COLOR_SCHEMES
    
    return {
        "color_schemes": [
            {"id": key, "name": value["name"]}
            for key, value in COLOR_SCHEMES.items()
        ]
    }


@router.get("/styles")
async def get_styles():
    """
    Get available design styles
    """
    return {
        "styles": [
            {"id": "modern", "name": "Modern", "description": "Clean and contemporary design"}
        ]
    }
