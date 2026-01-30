from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
