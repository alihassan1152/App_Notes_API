from bson import ObjectId
from datetime import datetime
from app.database import notes_collection
from app.models import NoteCreate, NoteUpdate
from app.services.ai_service import generate_summary


def note_helper(note) -> dict:
    """MongoDB document ko dict mein convert karo"""
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "content": note["content"],
        "tags": note.get("tags", []),
        "summary": note.get("summary"),
        "created_at": note["created_at"],
        "updated_at": note["updated_at"],
    }


async def create_note(note: NoteCreate) -> dict:
    summary = await generate_summary(note.content)
    now = datetime.utcnow()
    note_doc = {
        "title": note.title,
        "content": note.content,
        "tags": note.tags,
        "summary": summary,
        "created_at": now,
        "updated_at": now,
    }
    result = await notes_collection.insert_one(note_doc)
    new_note = await notes_collection.find_one({"_id": result.inserted_id})
    return note_helper(new_note)


async def get_all_notes() -> list:
    notes = []
    async for note in notes_collection.find():
        notes.append(note_helper(note))
    return notes


async def get_note_by_id(note_id: str) -> dict | None:
    if not ObjectId.is_valid(note_id):
        return None
    note = await notes_collection.find_one({"_id": ObjectId(note_id)})
    return note_helper(note) if note else None


async def update_note(note_id: str, note_data: NoteUpdate) -> dict | None:
    if not ObjectId.is_valid(note_id):
        return None
    update_fields = {k: v for k, v in note_data.model_dump().items() if v is not None}
    if not update_fields:
        return await get_note_by_id(note_id)
    update_fields["updated_at"] = datetime.utcnow()
    await notes_collection.update_one(
        {"_id": ObjectId(note_id)}, {"$set": update_fields}
    )
    return await get_note_by_id(note_id)


async def delete_note(note_id: str) -> bool:
    if not ObjectId.is_valid(note_id):
        return False
    result = await notes_collection.delete_one({"_id": ObjectId(note_id)})
    return result.deleted_count > 0
