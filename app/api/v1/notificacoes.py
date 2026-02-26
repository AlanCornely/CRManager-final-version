from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from app.models.notificacao import NotificacaoModel
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class NotificacaoSchema(BaseModel):
    id_notificacao: int
    id_usuario: Optional[int]
    mensagem: str
    tipo: str
    lida: bool
    data_criacao: str # SQLite returns string timestamp

@router.get("/", response_model=List[NotificacaoSchema])
async def list_notifications(limit: int = 50, id_usuario: Optional[int] = None):
    """Lista notificações recentes"""
    return NotificacaoModel.get_recent(limit, id_usuario)

@router.post("/{id_notificacao}/read")
async def mark_as_read(id_notificacao: int):
    """Marca notificação como lida"""
    NotificacaoModel.mark_as_read(id_notificacao)
    return {"message": "Notificação marcada como lida"}

@router.get("/unread-count")
async def get_unread_count(id_usuario: Optional[int] = None):
    """Retorna contagem de não lidas"""
    count = NotificacaoModel.get_unread_count(id_usuario)
    return {"count": count}

@router.post("/mark-all-read")
async def mark_all_read(id_usuario: Optional[int] = None):
    """Marca todas como lida para o usuário (ou globais se usuario null)"""
    NotificacaoModel.mark_all_as_read(id_usuario)
    return {"message": "Todas as notificações marcadas como lidas"}
