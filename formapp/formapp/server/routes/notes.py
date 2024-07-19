from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

client = AsyncIOMotorClient(MONGO_URI)
db = client.mydatabase

class Note(BaseModel):
    title: str
    content: str

router = APIRouter()

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload["id"]
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/")
async def create_note(note: Note, token: str = Depends(get_current_user)):
    note_data = note.dict()
    note_data["user_id"] = ObjectId(token)
    result = await db.notes.insert_one(note_data)
    return {"id": str(result.inserted_id)}

@router.get("/")
async def get_notes(token: str = Depends(get_current_user)):
    notes = await db.notes.find({"user_id": ObjectId(token)}).to_list(1000)
    for note in notes:
        note["_id"] = str(note["_id"])
    return notes

@router.delete("/{note_id}")
async def delete_note(note_id: str, token: str = Depends(get_current_user)):
    result = await db.notes.delete_one({"_id": ObjectId(note_id), "user_id": ObjectId(token)})
    if result.deleted_count == 1:
        return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Note not found")
