from fastapi import APIRouter, Query
from models.request import PromptRequest
from services.prompt_service import process_prompt

router = APIRouter(prefix="/api/v1", tags=["prompts"])

@router.post("/prompts")
async def submit_prompt(
    request: PromptRequest,
    page: int = Query(1, ge=1),
    pageSize: int = Query(10, ge=1)
):
    # This calls the "Brain" of your app (the service layer)
    return process_prompt(
        prompt=request.prompt,
        targetLanguage=request.targetLanguage,
        page=page,
        pageSize=pageSize
    )