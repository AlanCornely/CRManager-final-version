from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioInDB, UsuarioLogin
from app.models.usuario import UsuarioModel
from app.schemas.base import Token
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

router = APIRouter()

def create_access_token(data: dict):
    """Cria token JWT"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/login", response_model=Token)
async def login(login_data: UsuarioLogin):
    """Login de usuário"""
    user = UsuarioModel.authenticate(login_data.email, login_data.senha)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user["email"], "usuario_id": user["id_usuario"]}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", response_model=dict)
async def criar_usuario(usuario: UsuarioCreate):
    """Cria um novo usuário"""
    # Verifica se email já existe
    existing_user = UsuarioModel.get_by_email(usuario.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    usuario_id = UsuarioModel.create(usuario.dict())
    return {"id_usuario": usuario_id, "message": "Usuário criado com sucesso"}

@router.get("/", response_model=List[UsuarioInDB])
async def listar_usuarios():
    """Lista todos os usuários"""
    usuarios = UsuarioModel.get_all()
    return usuarios

@router.get("/{id_usuario}", response_model=UsuarioInDB)
async def buscar_usuario(id_usuario: int):
    """Busca um usuário por ID"""
    usuario = UsuarioModel.get_by_id(id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    return usuario

@router.put("/{id_usuario}")
async def atualizar_usuario(id_usuario: int, usuario: UsuarioUpdate):
    """Atualiza um usuário"""
    result = UsuarioModel.update(id_usuario, usuario.dict(exclude_unset=True))
    if result:
        return {"message": "Usuário atualizado com sucesso"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )

@router.delete("/{id_usuario}")
async def deletar_usuario(id_usuario: int):
    """Remove um usuário"""
    result = UsuarioModel.delete(id_usuario)
    if result:
        return {"message": "Usuário deletado com sucesso"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )