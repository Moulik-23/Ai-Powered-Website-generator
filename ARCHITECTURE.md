# System Architecture Diagram

## High-Level Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER'S BROWSER                            │
│  ┌────────────────────────────────────────────────────────┐     │
│  │              Frontend (Next.js/React)                   │     │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │     │
│  │  │ Generator    │  │   Preview    │  │   Projects   │ │     │
│  │  │    Form      │  │    View      │  │     List     │ │     │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘ │     │
│  │         │                  │                  │         │     │
│  │         └──────────────────┴──────────────────┘         │     │
│  │                            │                            │     │
│  └────────────────────────────┼────────────────────────────┘     │
└─────────────────────────────────┼──────────────────────────────┘
                                  │ HTTP/REST
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Backend API (FastAPI)                         │
│  ┌────────────────────────────────────────────────────────┐     │
│  │                    API Routes                           │     │
│  │  ┌──────────────┐              ┌──────────────┐        │     │
│  │  │  /generate   │              │  /projects   │        │     │
│  │  └──────┬───────┘              └──────┬───────┘        │     │
│  │         │                              │                │     │
│  │         ▼                              ▼                │     │
│  │  ┌──────────────────┐         ┌──────────────────┐    │     │
│  │  │   AI Service     │         │  Project Manager │    │     │
│  │  └──────┬───────────┘         └──────┬───────────┘    │     │
│  │         │                              │                │     │
│  │         │                              │                │     │
│  └─────────┼──────────────────────────────┼────────────────┘     │
└─────────────┼──────────────────────────────┼──────────────────────┘
              │                              │
              ▼                              ▼
    ┌───────────────────┐         ┌────────────────────┐
    │  Google Gemini    │         │     MongoDB        │
    │       API         │         │    Database        │
    │  (AI Generation)  │         │  (Project Store)   │
    └───────────────────┘         └────────────────────┘
```

## Component Interaction Flow

### Website Generation Flow

```
1. User Input
   ↓
2. Frontend Form
   │ Collects: prompt, style, color_scheme
   ↓
3. API Call: POST /api/generate
   ↓
4. AI Service
   │ ┌─ Analyze prompt
   │ ├─ Determine components needed
   │ ├─ Generate content for each component
   │ ├─ Assemble HTML
   │ ├─ Assemble CSS with color scheme
   │ └─ Add JavaScript
   ↓
5. Gemini API
   │ Processes natural language
   │ Returns structured data
   ↓
6. Response with generated website
   │ {html, css, js, components, meta}
   ↓
7. Frontend renders preview
   │ Live preview in iframe
   │ Code view with syntax highlighting
   │ Download/Save options
```

### Project Save/Load Flow

```
Save Flow:
User clicks Save → Modal opens → Enter name → POST /api/projects
    → MongoDB stores project → Success message

Load Flow:
User opens Projects tab → GET /api/projects → Display list
    → User clicks project → Load into preview → Ready to edit
```

## Backend Architecture Details

```
backend/
├── app/
│   ├── main.py                    [FastAPI Application]
│   │   ├── CORS Middleware
│   │   ├── Route Registration
│   │   └── Startup/Shutdown Events
│   │
│   ├── routes/
│   │   ├── generate.py            [Generation Endpoints]
│   │   │   ├── POST /generate
│   │   │   ├── GET /color-schemes
│   │   │   └── GET /styles
│   │   │
│   │   └── projects.py            [CRUD Endpoints]
│   │       ├── POST /projects
│   │       ├── GET /projects
│   │       ├── GET /projects/{id}
│   │       ├── PUT /projects/{id}
│   │       └── DELETE /projects/{id}
│   │
│   ├── services/
│   │   └── ai_service.py          [AI Generation Logic]
│   │       ├── generate_website()
│   │       ├── _analyze_prompt()
│   │       ├── _generate_components()
│   │       ├── _generate_component_content()
│   │       ├── _generate_meta_info()
│   │       ├── _assemble_html()
│   │       └── _assemble_css()
│   │
│   ├── models/
│   │   ├── database.py            [MongoDB Connection]
│   │   │   ├── Database class
│   │   │   └── get_database()
│   │   │
│   │   └── schemas.py             [Pydantic Models]
│   │       ├── WebsiteRequest
│   │       ├── WebsiteResponse
│   │       ├── ComponentData
│   │       └── ProjectModel
│   │
│   └── templates/
│       ├── components.py          [UI Components Library]
│       │   ├── navigation
│       │   ├── hero
│       │   ├── features
│       │   ├── gallery
│       │   ├── contact
│       │   └── footer
│       │
│       └── color_schemes.py       [Color Definitions]
│           ├── default
│           ├── dark
│           ├── ocean
│           ├── sunset
│           ├── forest
│           ├── purple
│           └── minimal
```

## Frontend Architecture Details

```
frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx             [Root Layout]
│   │   ├── page.tsx               [Main Application]
│   │   │   ├── State Management
│   │   │   ├── Tab Navigation
│   │   │   └── Component Rendering
│   │   │
│   │   └── globals.css            [Global Styles]
│   │
│   ├── components/
│   │   ├── GeneratorForm.tsx      [Input Form Component]
│   │   │   ├── Prompt Input
│   │   │   ├── Advanced Options
│   │   │   └── Submit Handler
│   │   │
│   │   ├── WebsitePreview.tsx     [Preview Component]
│   │   │   ├── Iframe Rendering
│   │   │   ├── Viewport Switching
│   │   │   ├── Download Handler
│   │   │   └── Save Handler
│   │   │
│   │   ├── CodeView.tsx           [Code Display]
│   │   │   ├── Syntax Highlighting
│   │   │   ├── Tab Switching
│   │   │   └── Copy to Clipboard
│   │   │
│   │   ├── ProjectsList.tsx       [Projects Manager]
│   │   │   ├── Fetch Projects
│   │   │   ├── Display List
│   │   │   ├── Load Handler
│   │   │   └── Delete Handler
│   │   │
│   │   └── SaveProjectModal.tsx   [Save Dialog]
│   │       ├── Name Input
│   │       ├── Project Details
│   │       └── Save Handler
│   │
│   └── lib/
│       ├── api.ts                 [API Client]
│       │   ├── generateWebsite()
│       │   ├── getColorSchemes()
│       │   ├── saveProject()
│       │   ├── getProjects()
│       │   └── deleteProject()
│       │
│       └── utils.ts               [Utilities]
│           ├── downloadFile()
│           ├── downloadWebsite()
│           ├── copyToClipboard()
│           └── formatDate()
```

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ 1. User Input                                                │
│    "Create a portfolio website for a photographer"          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. API Request                                               │
│    POST /api/generate                                        │
│    {                                                         │
│      "prompt": "Create a portfolio...",                      │
│      "style": "modern",                                      │
│      "color_scheme": "default"                               │
│    }                                                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Prompt Analysis (Gemini API)                              │
│    → Determines: navigation, hero, gallery, contact, footer │
│    → Identifies: portfolio, photographer, visual focus      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Component Generation                                      │
│    For each component:                                       │
│    ├─ Get template from components.py                       │
│    ├─ Generate content via Gemini                           │
│    ├─ Fill template with content                            │
│    └─ Add component CSS                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. Assembly                                                  │
│    ├─ Combine all component HTML                            │
│    ├─ Merge all CSS + color scheme                          │
│    ├─ Add common JavaScript                                 │
│    └─ Generate meta information                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. API Response                                              │
│    {                                                         │
│      "html": "<!DOCTYPE html>...",                          │
│      "css": "* { margin: 0; }...",                          │
│      "js": "document.addEventListener...",                   │
│      "components": [...],                                    │
│      "meta_description": "Professional photography...",     │
│      "title": "Photography Portfolio"                       │
│    }                                                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. Frontend Rendering                                        │
│    ├─ Create complete HTML document                         │
│    ├─ Render in iframe                                      │
│    ├─ Display code with syntax highlighting                 │
│    └─ Enable download/save options                          │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack Details

```
┌────────────────────────────────────────────────────────────┐
│                     FRONTEND LAYER                          │
├────────────────────────────────────────────────────────────┤
│ Framework:        Next.js 14                               │
│ Language:         TypeScript                               │
│ Styling:          Tailwind CSS                             │
│ State:            React Hooks (useState, useEffect)        │
│ HTTP Client:      Axios                                    │
│ Code Display:     React Syntax Highlighter                 │
│ Icons:            React Icons                              │
│ Animations:       Framer Motion                            │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                     BACKEND LAYER                           │
├────────────────────────────────────────────────────────────┤
│ Framework:        FastAPI 0.109                            │
│ Language:         Python 3.9+                              │
│ Async Runtime:    asyncio                                  │
│ Validation:       Pydantic 2.5                             │
│ CORS:             FastAPI CORS Middleware                  │
│ API Docs:         OpenAPI (Swagger)                        │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                     DATA LAYER                              │
├────────────────────────────────────────────────────────────┤
│ Database:         MongoDB 6.0+                             │
│ Driver:           Motor 3.3 (async)                        │
│ ORM:              PyMongo 4.6                              │
│ Schema:           Pydantic Models                          │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                     AI LAYER                                │
├────────────────────────────────────────────────────────────┤
│ Provider:         Google AI                                │
│ Model:            Gemini Pro                               │
│ SDK:              google-generativeai 0.3                  │
│ Use Cases:        Content generation, analysis             │
└────────────────────────────────────────────────────────────┘
```

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         PRODUCTION                           │
└─────────────────────────────────────────────────────────────┘

Frontend (Vercel/Netlify)
    ↓
    CDN (Static Assets)
    ↓
    HTTPS
    ↓
Load Balancer (Optional)
    ↓
Backend Server(s)
    ├─ FastAPI Application
    ├─ Nginx Reverse Proxy
    └─ SSL/TLS (Let's Encrypt)
    ↓
    ├─ MongoDB Atlas (Database)
    └─ Google Gemini API (AI)

Monitoring & Logging
    ├─ Application Logs
    ├─ Error Tracking
    └─ Performance Metrics
```

## Security Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Security Layers                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  1. Transport Layer                                      │
│     └─ HTTPS/TLS encryption                             │
│                                                          │
│  2. Application Layer                                    │
│     ├─ CORS configuration                               │
│     ├─ Input validation (Pydantic)                      │
│     └─ Parameterized queries                            │
│                                                          │
│  3. Data Layer                                           │
│     ├─ Environment variables for secrets                │
│     ├─ API key management                               │
│     └─ Database authentication                          │
│                                                          │
│  4. AI Layer                                             │
│     ├─ API key protection                               │
│     ├─ Rate limiting (recommended)                      │
│     └─ Content filtering                                │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Scalability Considerations

```
Horizontal Scaling:
┌────────────────────────────────────────────────────┐
│ Load Balancer                                       │
├────────────────────────────────────────────────────┤
│  ↓              ↓              ↓                    │
│ API Server 1  API Server 2  API Server 3           │
│  ↓              ↓              ↓                    │
│ └──────────────┴──────────────┘                    │
│         ↓                                           │
│    MongoDB Cluster                                  │
│    (Replica Set)                                    │
└────────────────────────────────────────────────────┘

Caching Strategy:
┌────────────────────────────────────────────────────┐
│ Browser Cache (Static Assets)                      │
│      ↓                                              │
│ CDN Cache (Frontend)                               │
│      ↓                                              │
│ Redis Cache (API Responses) [Optional]             │
│      ↓                                              │
│ Database (Persistent Storage)                      │
└────────────────────────────────────────────────────┘
```

---

For more details on any component, see:
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Technical overview
- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - API details
- [CUSTOMIZATION.md](CUSTOMIZATION.md) - Customization guide
