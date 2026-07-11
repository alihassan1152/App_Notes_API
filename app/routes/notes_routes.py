from fastapi import APIRouter, HTTPException, status
from app.models import NoteCreate, NoteUpdate, NoteResponse, QuestionRequest
from app.services import notes_service
from app.services.ai_service import ask_about_notes

router = APIRouter()


@router.post("/notes", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteCreate):
    """Naya note banao"""
    return await notes_service.create_note(note)


@router.post("/notes/ask")
async def ask_notes(request: QuestionRequest): 
    notes = await notes_service.get_all_notes()
    if not notes:
        return {"answer": "Aap ke paas abhi koi note nahi hai."}
    answer = await ask_about_notes(notes, request.question)
    return {"answer": answer}     


@router.get("/notes", response_model=list[NoteResponse])
async def get_all_notes():
    """Saare notes lao"""
    return await notes_service.get_all_notes()


@router.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note(note_id: str):
    """Ek note lao ID se"""
    note = await notes_service.get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note nahi mila!")
    return note


@router.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note(note_id: str, note: NoteUpdate):
    """Note update karo"""
    updated = await notes_service.update_note(note_id, note)
    if not updated:
        raise HTTPException(status_code=404, detail="Note nahi mila!")
    return updated


@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: str):
    """Note delete karo"""
    deleted = await notes_service.delete_note(note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Note nahi mila!")


