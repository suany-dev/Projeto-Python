from fastapi import APIRouter  

order_routes = APIRouter (prefix="/pedidos", tags =["pedidos"])

@order_routes.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}
