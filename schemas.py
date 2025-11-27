from pydantic import BaseModel, EmailStr

class MessageCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    message: str
