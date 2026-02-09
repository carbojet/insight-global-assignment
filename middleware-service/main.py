from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.prompt_routes import router as prompt_router
from core.exceptions import InvalidLanguageException
from core.error_handler import invalid_language_handler

app = FastAPI()

# CORS MUST BE IMMEDIATELY AFTER APP CREATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(InvalidLanguageException, invalid_language_handler)

app.include_router(prompt_router)

@app.get("/")
async def root():
    return {"message": "AI Middleware API is running"}
