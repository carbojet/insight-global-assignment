from fastapi import Request
from fastapi.responses import JSONResponse
from core.exceptions import InvalidLanguageException

async def invalid_language_handler(request: Request, exc: InvalidLanguageException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "INVALID_LANGUAGE",
            "message": "Target language is not supported"
        }
    )
