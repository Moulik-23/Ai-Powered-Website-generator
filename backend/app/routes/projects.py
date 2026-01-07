from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..models.schemas import ProjectModel, WebsiteResponse
from ..models.database import get_database
from bson import ObjectId
from datetime import datetime

router = APIRouter()


@router.post("/projects", response_model=dict)
async def save_project(project: ProjectModel, db=Depends(get_database)):
    """
    Save a generated website project
    """
    try:
        project_dict = project.dict(exclude={"id"})
        project_dict["created_at"] = datetime.utcnow()
        project_dict["updated_at"] = datetime.utcnow()
        
        result = await db.projects.insert_one(project_dict)
        
        return {
            "id": str(result.inserted_id),
            "message": "Project saved successfully"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error saving project: {str(e)}"
        )


@router.get("/projects")
async def get_projects(db=Depends(get_database)):
    """
    Get all saved projects
    """
    try:
        projects = []
        cursor = db.projects.find().sort("created_at", -1)
        
        async for project in cursor:
            project["id"] = str(project["_id"])
            del project["_id"]
            projects.append(project)
        
        return {"projects": projects}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching projects: {str(e)}"
        )


@router.get("/projects/{project_id}")
async def get_project(project_id: str, db=Depends(get_database)):
    """
    Get a specific project by ID
    """
    try:
        if not ObjectId.is_valid(project_id):
            raise HTTPException(status_code=400, detail="Invalid project ID")
        
        project = await db.projects.find_one({"_id": ObjectId(project_id)})
        
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        
        project["id"] = str(project["_id"])
        del project["_id"]
        
        return project
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching project: {str(e)}"
        )


@router.put("/projects/{project_id}")
async def update_project(
    project_id: str,
    project: ProjectModel,
    db=Depends(get_database)
):
    """
    Update an existing project
    """
    try:
        if not ObjectId.is_valid(project_id):
            raise HTTPException(status_code=400, detail="Invalid project ID")
        
        project_dict = project.dict(exclude={"id", "created_at"})
        project_dict["updated_at"] = datetime.utcnow()
        
        result = await db.projects.update_one(
            {"_id": ObjectId(project_id)},
            {"$set": project_dict}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Project not found")
        
        return {"message": "Project updated successfully"}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error updating project: {str(e)}"
        )


@router.delete("/projects/{project_id}")
async def delete_project(project_id: str, db=Depends(get_database)):
    """
    Delete a project
    """
    try:
        if not ObjectId.is_valid(project_id):
            raise HTTPException(status_code=400, detail="Invalid project ID")
        
        result = await db.projects.delete_one({"_id": ObjectId(project_id)})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Project not found")
        
        return {"message": "Project deleted successfully"}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error deleting project: {str(e)}"
        )
