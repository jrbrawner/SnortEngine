from fastapi import FastAPI
from .basic.router import router as basic_router

app = FastAPI()

app.include_router(basic_router)



