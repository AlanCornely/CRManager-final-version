from typing import Type, TypeVar, Generic, List, Optional, Dict, Any
from app.database import db

ModelType = TypeVar('ModelType')

class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
    
    def create(self, **kwargs) -> Optional[int]:
        """Cria um novo registro"""
        pass
    
    def get(self, id: int) -> Optional[Dict[str, Any]]:
        """Busca um registro por ID"""
        pass
    
    def get_all(self) -> List[Dict[str, Any]]:
        """Busca todos os registros"""
        pass
    
    def update(self, id: int, **kwargs) -> bool:
        """Atualiza um registro"""
        pass
    
    def delete(self, id: int) -> bool:
        """Remove um registro"""
        pass