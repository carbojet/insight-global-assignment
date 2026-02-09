# Insight Global -- Fullstack Assignment

## Overview

This project is a fullstack AI Insights platform built as part of the
Insight Global Senior Software Developer assignment.

The system consists of:

-   **Backend**: Python FastAPI middleware service that processes
    prompts and returns AI-generated insights.
-   **Frontend**: React application that allows users to submit prompts
    and view paginated insights.

------------------------------------------------------------------------

## Architecture

    frontend/   → React (Vite) client application  
    backend/    → FastAPI middleware service (Docker-enabled)

The frontend communicates with the backend via REST API.

------------------------------------------------------------------------

# Backend Setup (FastAPI)

### 1. Navigate to backend

``` bash
cd backend
```

### 2. (Optional) Create Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4. Run Server

``` bash
uvicorn main:app --reload
```

Backend runs at:

    http://localhost:8000

API endpoint:

    POST /api/v1/prompts?page=1&pageSize=10

------------------------------------------------------------------------

# Backend Using Docker

### Build Docker Image

``` bash
docker build -t middleware-service .
```

### Run Container

``` bash
docker run -p 8000:8000 middleware-service
```

------------------------------------------------------------------------

# Frontend Setup (React + Vite)

### 1. Navigate to frontend

``` bash
cd frontend
```

### 2. Install Dependencies

``` bash
npm install
```

### 3. Configure Environment Variable

Create a `.env` file:

    VITE_API_BASE_URL=http://localhost:8000/api/v1

### 4. Start Development Server

``` bash
npm run dev
```

Frontend runs at:

    http://localhost:5173

------------------------------------------------------------------------

# How to Use the Application

1.  Open frontend in browser.
2.  Enter a prompt (minimum 5 characters).
3.  Select a target language.
4.  Click **Submit**.
5.  First 10 insights will load.
6.  Click **Load More** to fetch additional insights.

The UI handles:

-   Validation
-   Error states
-   Clarification responses
-   Pagination

------------------------------------------------------------------------

# Tech Stack

## Backend

-   Python
-   FastAPI
-   Uvicorn
-   Docker

## Frontend

-   React
-   Redux Toolkit (RTK Query)
-   Vite
-   React Hook Form
-   Zod

------------------------------------------------------------------------

# Notes

-   `.env` files are excluded from repository.
-   Backend and frontend can be run independently.
-   Designed with production-oriented structure and clean separation of
    concerns.
