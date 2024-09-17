from pydantic import BaseModel, Field
from typing import Optional

class QueryCategory(BaseModel):
    category: str = Field(..., description="The main category of the query")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score of the categorization")

    class Config:
        json_schema_extra = {
            "example": {
                "category": "Savings Account",
                "confidence": 0.95
            }
        }