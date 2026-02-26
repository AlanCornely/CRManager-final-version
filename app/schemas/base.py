from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True

class Token(BaseSchema):
    access_token: str
    token_type: str

class TokenData(BaseSchema):
    email: Optional[str] = None
    usuario_id: Optional[int] = None