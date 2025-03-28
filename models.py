from pydantic import BaseModel, EmailStr, Field
from beanie import Document
from uuid import UUID, uuid4 
from datetime import date 

class User(Document):
    user_id: UUID = Field(default_factory=uuid4, unique=True)
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool = False
    hashed_password: str
    created_at: date = Field(default_factory=date.today)
    updated_at: date = Field(default_factory=date.today)

    async def save(self, *args, **kwargs):
        self.updated_at = date.today()
        if not self.id:
            return await self.insert()
        return await self.replace()

    class Settings:
        name = "users"

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: UUID | None = None

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    password: str  

class Note(Document):
    note_id: UUID = Field(default_factory=uuid4, unique=True)
    user_id: UUID 
    note_title: str 
    note_content: str 
    last_update: date = Field(default_factory=date.today)
    created_on: date = Field(default_factory=date.today)

    async def save(self, *args, **kwargs):
        self.updated_at = date.today()
        if not self.id:
            return await self.insert()
        return await self.replace()

    class Settings:
        name = "notes"


class NoteCreate(BaseModel):
    note_title: str 
    note_content: str 
