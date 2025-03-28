from fastapi import APIRouter, HTTPException, Depends 
from typing import List
from noteapp_server.models import Note, NoteCreate, User 
from noteapp_server.routers.auth import get_current_active_user

router = APIRouter()


@router.post("/", response_model=Note)
async def create_note(note_request: NoteCreate,
                      current_user: User = Depends(get_current_active_user)):
    note = Note(**note_request.model_dump(), user_id = current_user.user_id)
    await note.create()
    return note 


@router.get("/", response_model=List[Note])
async def get_notes():
    notes = await Note.find_all().to_list()
    return notes 

@router.get("/{note_id}", response_model=Note)
async def get_note(note_id: str):
    note = await Note.get(note_id)
    throw_exception(note)
    return note 

@router.put("/{note_id}", response_model=Note)
async def update_note(note_id: str, request: NoteCreate):
    note = await Note.get(note_id)
    throw_exception(note)
    await note.update({"$set": request.model_dump(exclude_unset=True)})
    return await Note.get(note_id)

@router.delete("/{note_id}")
async def delete_note(note_id: str):
    note = await Note.get(note_id)
    throw_exception(note)
    await note.delete()


def throw_exception(note):
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
