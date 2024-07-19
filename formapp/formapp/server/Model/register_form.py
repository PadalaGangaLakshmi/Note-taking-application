from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    rollnumber: str
    phonenumber: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class NoteIn(BaseModel):
    content: str
