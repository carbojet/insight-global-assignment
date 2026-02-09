import logging
from core.exceptions import InvalidLanguageException
from services.ai_service import generate_insights
from utils.pagination import paginate
from logging import getLogger

logger = logging.getLogger(__name__)
SUPPORTED_LANGUAGES = ["en", "es", "fr"]

def process_prompt(prompt: str, targetLanguage: str, page: int, pageSize: int):
    
    if targetLanguage not in SUPPORTED_LANGUAGES:
        raise InvalidLanguageException()

    if len(prompt.strip()) < 5:
        return {
            "status": "NEEDS_CLARIFICATION",
            "message": "Please provide more details."
        }

    insights = generate_insights(prompt)
    paginated = paginate(insights, page, pageSize)

    return {
        "status": "SUCCESS",
        "contextId": None,
        "data": paginated["data"],
        "pagination": paginated["meta"]
    }
