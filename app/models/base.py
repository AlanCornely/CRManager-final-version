from datetime import datetime
from typing import Optional

class BaseModel:
    """Classe base para todos os modelos"""
    
    @staticmethod
    def to_dict(data: dict) -> dict:
        """Converte resultados do banco para dict"""
        if not data:
            return {}
        
        result = {}
        for key, value in data.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        return result