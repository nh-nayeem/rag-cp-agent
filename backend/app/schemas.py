from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class EmbedRequest(BaseModel):
    text: str

class EmbedResponse(BaseModel):
    embedding: List[float]

class AskRequest(BaseModel):
    query: str

class SourceInfo(BaseModel):
    payload: Dict[str, Any]
    score: float

class AskResponse(BaseModel):
    answer: str
    sources: List[SourceInfo]

class HealthResponse(BaseModel):
    status: str