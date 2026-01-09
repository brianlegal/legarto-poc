from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Configuração de CORS: Isso permite que o Lovable acesse sua API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite acesso de qualquer lugar (importante para o teste)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def raiz():
    return {"mensagem": "API do Legarto está online!"}

@app.get("/status")
async def pegar_status():
    status_opcoes = [
        {"status": "PISCA", "cor": "green", "detalhes": "Operação rodando 100%"},
        {"status": "MRBLINK", "cor": "yellow", "detalhes": "Flutuação de tráfego detectada"},
        {"status": "OROCHINO", "cor": "red", "detalhes": "Encerrando atividades. Procure o RH"},
        {"status": "MILTON", "cor": "blue", "detalhes": "Contratando novos talentos"}
    ]
    
    # Escolhe um status aleatório
    resultado = random.choice(status_opcoes)
    return resultado