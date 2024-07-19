from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

client = AsyncIOMotorClient(MONGO_URI)
db = client.mydatabase

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    name: str
    email: str
    rollnumber: str
    phonenumber: str
    password: str

class Login(BaseModel):
    email: str
    password: str

router = APIRouter()

@router.post("/add-registerform")
async def register(user: User):
    user.password = pwd_context.hash(user.password)
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id)}

@router.post("/login")
async def login(login: Login):
    user = await db.users.find_one({"email": login.email})
    if user and pwd_context.verify(login.password, user["password"]):
        token = jwt.encode({"id": str(user["_id"])}, SECRET_KEY, algorithm="HS256")
        return {"token": token}
    raise HTTPException(status_code=400, detail="Invalid email or password")
