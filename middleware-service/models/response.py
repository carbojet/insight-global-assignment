from pydantic import BaseModel
from typing import List, Optional
from insight import Insight

class PaginationMetadata(BaseModel):
    total: int
    page: int
    limit: int
    totalPages: int
    hasNext: bool

class SuccessResponse(BaseModel):
    status: str = "SUCCESS"
    data: List[Insight]
    pagination: PaginationMetadata

class ClarificationResponse(BaseModel):
    status: str = "NEEDS_CLARIFICATION"
    message: str

class ErrorResponse(BaseModel):
    error: str
    message: str