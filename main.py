from fastapi import FastAPI #importa a classe FastAPI

app = FastAPI() # instanciando a classe

from auth_routes import auth_routes 
from order_routes import order_routes

app.include_router(auth_routes)
app.include_router(order_routes)











#para rodar o codigo , executar no terminal :uvicorn main:app --reload