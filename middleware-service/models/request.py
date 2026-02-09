from pydantic import BaseModel, Field, field_validator
from typing import Optional
from uuid import UUID
class PromptRequest(BaseModel):
    prompt: str = Field(...,minimum_length=1, max_length=10000, description="The prompt to be processed by the model.")
    targetLanguage: Optional[str] = Field(None, description="The target language for translation tasks.")
    contextId: Optional[UUID] = Field(None, description="The context ID for the request.")

    @field_validator('targetLanguage')
    @classmethod
    def validate_language(cls, v: str):
        supported = ['en', 'es', 'fr', 'de']
        if v.lower() not in supported:
            # We will handle this custom exception in the core layer next
            raise ValueError(f"Language '{v}' is not supported.")
        return v.lower()