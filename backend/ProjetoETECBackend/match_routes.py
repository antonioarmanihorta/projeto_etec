from fastapi import APIRouter

match_router = APIRouter(prefix="/match", tags=["match"])

@match_router.post("/")
async def iniciar_partida():
    """
    Essa e a rota padrao de criação de partidas. Somente usuarios autenticados podem acessar.
    """
    return {"mensagem": "Você acessou o menu de criação de partidas"}


