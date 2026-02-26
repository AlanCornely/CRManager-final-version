from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    cargo: Optional[str] = None
    permissao: Optional[str] = None
    configuracoes: Optional[dict] = {}

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    cargo: Optional[str] = None
    permissao: Optional[str] = None
    ativo: Optional[bool] = None
    configuracoes: Optional[dict] = None

class UsuarioInDB(UsuarioBase):
    id_usuario: int
    ativo: bool

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str