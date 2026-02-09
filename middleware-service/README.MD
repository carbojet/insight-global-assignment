
# AI Middleware Service (Backend)

## Overview

This service implements a middleware (Backend-for-Frontend) API that simulates an AI orchestration layer.

The middleware is responsible for:

- Input validation  
- Business rule enforcement  
- AI invocation (simulated)  
- Structured response modeling  
- Pagination handling  
- Error normalization  

The goal of this implementation is to demonstrate clean layered architecture, explicit API contracts, and scalable service design rather than AI model integration.

---

## Architecture

Client (React UI)
        |
        |  HTTP (REST)
        v
FastAPI Middleware (BFF)
        |
        |  AI Service (Simulated)
        v
Structured Insight Response

### Architectural Principles

- Separation of concerns  
- Backend-driven pagination  
- Explicit response modeling  
- Centralized error handling  
- AI abstraction layer for extensibility  

---

## Project Structure

middleware-service/
│
├── main.py                # Application bootstrap
├── routes/                # HTTP routing layer
│   └── prompt_routes.py
│
├── services/              # Business logic layer
│   ├── prompt_service.py
│   └── ai_service.py
│
├── models/                # Request/Response schemas
│   ├── request.py
│   ├── response.py
│   └── insight.py
│
├── core/                  # Exceptions & global handlers
│   ├── exceptions.py
│   └── error_handler.py
│
├── utils/                 # Reusable utilities
│   └── pagination.py
│
├── Dockerfile
├── requirements.txt
└── README.md

---

## API Contract

### Base URL

/api/v1

---

### POST /api/v1/prompts

Submits a prompt for AI processing.

#### Query Parameters

| Parameter | Type | Default  | Description    |
|-----------|------|----------|----------------|
| page      | int  | 1        | Page number    |
| pageSize  | int  | 10       | Items per page |

---

### Request Body

{
  "prompt": "Analyze system design patterns",
  "targetLanguage": "en",
  "contextId": "optional-uuid"
}

### Validation Rules

- prompt must be non-empty.
- targetLanguage must be supported (en, es, fr).
- If prompt length < 5 → clarification response.
- Validation occurs before AI invocation.

---

## Response Types

### SUCCESS

{
  "status": "SUCCESS",
  "contextId": "uuid",
  "data": [ ... ],
  "pagination": {
    "page": 1,
    "pageSize": 10,
    "totalItems": 37,
    "totalPages": 4,
    "hasNext": true
  }
}

### NEEDS_CLARIFICATION

{
  "status": "NEEDS_CLARIFICATION",
  "message": "Please provide more details."
}

### Validation Error (400)

{
  "error": "INVALID_LANGUAGE",
  "message": "Target language is not supported"
}

---

## Design Decisions

### Backend-Driven Pagination

Pagination is handled server-side to:

- Prevent excessive payload size  
- Simulate realistic AI output volumes  
- Improve scalability  
- Keep frontend logic simple  

### AI Abstraction Layer

The AI integration is abstracted into ai_service.py.

This enables:

- Easy replacement with real LLM integration  
- Isolation of AI logic from business rules  
- Independent testing  

### Centralized Error Handling

Custom exceptions are defined in core/ and mapped using FastAPI’s global exception handlers.

---

## Running the Service (Local)

### Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Start Server

uvicorn main:app --reload

Access Swagger UI:

http://127.0.0.1:8000/docs

---

## Running with Docker

### Build Image

docker build -t ai-middleware .

### Run Container

docker run -p 8000:8000 ai-middleware

Access:

http://localhost:8000/docs

---

## Sample Test Scenarios

1. Unsupported language → 400  
2. Short prompt → NEEDS_CLARIFICATION  
3. Valid prompt → SUCCESS (paginated insights)  
4. Pagination via ?page=2&pageSize=10  

---

## Future Enhancements

- Cursor-based pagination  
- Conversation persistence via contextId  
- Real LLM integration  
- Structured logging  
- Rate limiting & authentication  
- Health checks & observability  

---

## Evaluation Focus

This implementation emphasizes:

- Clean layered architecture  
- Explicit API contracts  
- Deterministic response modeling  
- Extensibility and scalability  
- Production-aware structure  
