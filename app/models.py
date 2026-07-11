from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    tags: Optional[list[str]] = []


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    content: Optional[str] = None
    tags: Optional[list[str]] = None


class NoteResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: list[str] = []
    summary: Optional[str] = None  # AI se generate hoga
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1)