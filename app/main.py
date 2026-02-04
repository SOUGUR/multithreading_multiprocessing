from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Cell Analytics Engine")
app.include_router(router)
