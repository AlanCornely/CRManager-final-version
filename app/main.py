from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import api_router

app = FastAPI(
    title="CRM de Gerenciamento de Estoque",
    description="API para gerenciamento de estoque e CRM",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas da API
app.include_router(api_router, prefix="/api/v1")

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Create frontend directory if it doesn't exist (just to be safe, though we know it does)
if not os.path.exists("frontend"):
    os.makedirs("frontend")

app.mount("/assets", StaticFiles(directory="frontend"), name="assets")

@app.get("/")
async def root():
    return FileResponse('frontend/index.html')

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "crm-estoque-api"}