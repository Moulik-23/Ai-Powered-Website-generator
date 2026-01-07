from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime


class WebsiteRequest(BaseModel):
    """Request model for website generation"""
    prompt: str = Field(..., description="User's description of the website")
    style: Optional[str] = Field(default="modern", description="Design style preference")
    color_scheme: Optional[str] = Field(default="default", description="Color scheme preference")


class ComponentData(BaseModel):
    """Model for individual UI components"""
    type: str
    html: str
    css: str
    js: Optional[str] = None


class WebsiteResponse(BaseModel):
    """Response model for generated website"""
    id: Optional[str] = None
    html: str
    css: str
    js: str
    components: List[ComponentData]
    meta_description: str
    title: str
    prompt: str
    style: str
    color_scheme: str


class ProjectModel(BaseModel):
    """Model for saved projects"""
    id: Optional[str] = None
    name: str
    prompt: str
    html: str
    css: str
    js: str
    components: List[Dict]
    meta_description: str
    title: str
    style: str
    color_scheme: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Photographer Portfolio",
                "prompt": "Create a portfolio website for a photographer",
                "html": "<html>...</html>",
                "css": "body { ... }",
                "js": "// JavaScript code",
                "components": [],
                "meta_description": "Professional photography portfolio",
                "title": "Photography Portfolio",
                "style": "modern",
                "color_scheme": "dark"
            }
        }
