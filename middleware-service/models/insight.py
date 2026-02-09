from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Insight(BaseModel):
    id: UUID
    title: str
    content: str
    category: str
    confidenceScore: float
    createdAt: datetime
    updatedAt: datetime