import sqlite3
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.database_path = os.getenv("DB_PATH", "crm_estoque.db")
        self.connection = None
    
    def get_connection(self):
        """Cria e retorna uma conexão com o banco de dados SQLite"""
        try:
            if self.connection is None:
                self.connection = sqlite3.connect(self.database_path, check_same_thread=False)
                self.connection.row_factory = sqlite3.Row
            return self.connection
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao SQLite: {e}")
            return None
    
    def execute_query(self, query: str, params: tuple = None, fetch_one: bool = False):
        """Executa uma query SQL"""
        connection = self.get_connection()
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            
            if query.strip().upper().startswith("SELECT"):
                if fetch_one:
                    row = cursor.fetchone()
                    result = dict(row) if row else None
                else:
                    rows = cursor.fetchall()
                    result = [dict(row) for row in rows] if rows else []
            else:
                connection.commit()
                result = cursor.lastrowid
            
            return result
        except sqlite3.Error as e:
            print(f"Erro ao executar query: {e}")
            connection.rollback()
            return None
        finally:
            if cursor:
                cursor.close()
    
    def execute_many(self, query: str, params_list: list):
        """Executa múltiplas queries"""
        connection = self.get_connection()
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.executemany(query, params_list)
            connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao executar múltiplas queries: {e}")
            connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
    
    def close(self):
        """Fecha a conexão com o banco"""
        if self.connection:
            self.connection.close()
            self.connection = None

# Instância global do banco de dados
db = Database()