from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
import jwt

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.mydatabase

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

class User(BaseModel):
    name: str
    email: str
    rollnumber: str
    phonenumber: str
    password: str

class Note(BaseModel):
    title: str
    content: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = await db.users.find_one({"_id": user_id})
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/add-registerform")
async def register(user: User):
    user.password = pwd_context.hash(user.password)
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

class Login(BaseModel):
    email: str
    password: str

@app.post("/login")
async def login(login: Login):
    user = await db.users.find_one({"email": login.email})
    if user and pwd_context.verify(login.password, user["password"]):
        token = jwt.encode({"id": str(user["_id"])}, SECRET_KEY, algorithm=ALGORITHM)
        return {"token": token}
    raise HTTPException(status_code=400, detail="Invalid email or password")

@app.get("/notes")
async def get_notes(current_user: User = Depends(get_current_user)):
    notes = await db.notes.find({"user_id": str(current_user["_id"])}).to_list(100)
    return notes

@app.post("/notes")
async def add_note(note: Note, current_user: User = Depends(get_current_user)):
    note_dict = note.dict()
    note_dict["user_id"] = str(current_user["_id"])
    result = await db.notes.insert_one(note_dict)
    return {"id": str(result.inserted_id)}

@app.put("/notes/{note_id}")
async def update_note(note_id: str, note: Note, current_user: User = Depends(get_current_user)):
    await db.notes.update_one(
        {"_id": note_id, "user_id": str(current_user["_id"])},
        {"$set": note.dict()}
    )
    return {"message": "Note updated"}

@app.delete("/notes/{note_id}")
async def delete_note(note_id: str, current_user: User = Depends(get_current_user)):
    await db.notes.delete_one({"_id": note_id, "user_id": str(current_user["_id"])})
    return {"message": "Note deleted"}
