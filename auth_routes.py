from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags = ["auth"])

@auth_routes.get("/")
async def autenticar(): 
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """

    return {"Mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

