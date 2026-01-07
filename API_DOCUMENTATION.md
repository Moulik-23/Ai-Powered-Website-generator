# API Documentation

## Base URL
```
http://localhost:8000/api
```

## Endpoints

### 1. Generate Website

Generate a complete website from a text prompt.

**Endpoint:** `POST /api/generate`

**Request Body:**
```json
{
  "prompt": "Create a portfolio website for a photographer",
  "style": "modern",
  "color_scheme": "default"
}
```

**Parameters:**
- `prompt` (required): Text description of the website
- `style` (optional): Design style - default: "modern"
- `color_scheme` (optional): Color scheme - default: "default"

**Response:**
```json
{
  "html": "<!DOCTYPE html>...",
  "css": "* { margin: 0; }...",
  "js": "document.addEventListener...",
  "components": [
    {
      "type": "navigation",
      "html": "<nav>...</nav>",
      "css": ".navbar {...}",
      "js": ""
    }
  ],
  "meta_description": "Professional photography portfolio",
  "title": "Photography Portfolio",
  "prompt": "Create a portfolio website for a photographer",
  "style": "modern",
  "color_scheme": "default"
}
```

### 2. Get Color Schemes

Get list of available color schemes.

**Endpoint:** `GET /api/color-schemes`

**Response:**
```json
{
  "color_schemes": [
    {"id": "default", "name": "Default Light"},
    {"id": "dark", "name": "Dark Mode"},
    {"id": "ocean", "name": "Ocean Blue"}
  ]
}
```

### 3. Get Styles

Get list of available design styles.

**Endpoint:** `GET /api/styles`

**Response:**
```json
{
  "styles": [
    {
      "id": "modern",
      "name": "Modern",
      "description": "Clean and contemporary design"
    }
  ]
}
```

### 4. Save Project

Save a generated website project.

**Endpoint:** `POST /api/projects`

**Request Body:**
```json
{
  "name": "My Portfolio",
  "prompt": "Create a portfolio website",
  "html": "<!DOCTYPE html>...",
  "css": "body {...}",
  "js": "document.addEventListener...",
  "components": [],
  "meta_description": "My portfolio website",
  "title": "Portfolio",
  "style": "modern",
  "color_scheme": "default"
}
```

**Response:**
```json
{
  "id": "507f1f77bcf86cd799439011",
  "message": "Project saved successfully"
}
```

### 5. Get All Projects

Retrieve all saved projects.

**Endpoint:** `GET /api/projects`

**Response:**
```json
{
  "projects": [
    {
      "id": "507f1f77bcf86cd799439011",
      "name": "My Portfolio",
      "prompt": "Create a portfolio website",
      "html": "<!DOCTYPE html>...",
      "css": "body {...}",
      "js": "document.addEventListener...",
      "components": [],
      "meta_description": "My portfolio website",
      "title": "Portfolio",
      "style": "modern",
      "color_scheme": "default",
      "created_at": "2026-01-06T10:30:00",
      "updated_at": "2026-01-06T10:30:00"
    }
  ]
}
```

### 6. Get Project by ID

Get a specific project.

**Endpoint:** `GET /api/projects/{project_id}`

**Response:**
```json
{
  "id": "507f1f77bcf86cd799439011",
  "name": "My Portfolio",
  "prompt": "Create a portfolio website",
  "html": "<!DOCTYPE html>...",
  "css": "body {...}",
  "js": "document.addEventListener...",
  "components": [],
  "meta_description": "My portfolio website",
  "title": "Portfolio",
  "style": "modern",
  "color_scheme": "default",
  "created_at": "2026-01-06T10:30:00",
  "updated_at": "2026-01-06T10:30:00"
}
```

### 7. Update Project

Update an existing project.

**Endpoint:** `PUT /api/projects/{project_id}`

**Request Body:**
```json
{
  "name": "Updated Portfolio",
  "prompt": "Create a portfolio website",
  "html": "<!DOCTYPE html>...",
  "css": "body {...}",
  "js": "document.addEventListener...",
  "components": [],
  "meta_description": "Updated description",
  "title": "Portfolio",
  "style": "modern",
  "color_scheme": "dark"
}
```

**Response:**
```json
{
  "message": "Project updated successfully"
}
```

### 8. Delete Project

Delete a project.

**Endpoint:** `DELETE /api/projects/{project_id}`

**Response:**
```json
{
  "message": "Project deleted successfully"
}
```

### 9. Health Check

Check API health status.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy"
}
```

## Error Responses

All endpoints may return error responses:

```json
{
  "detail": "Error message describing what went wrong"
}
```

**Common HTTP Status Codes:**
- `200`: Success
- `400`: Bad Request (invalid parameters)
- `404`: Not Found (resource doesn't exist)
- `500`: Internal Server Error

## Rate Limiting

Currently no rate limiting is implemented. For production use, consider adding rate limiting middleware.

## Authentication

Currently no authentication is required. For production use, implement authentication and authorization.

## Interactive Documentation

FastAPI provides interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
