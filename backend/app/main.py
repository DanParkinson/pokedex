from backend.app.api.pokemon import router as pokemon_router
from backend.app.core.cors import setup_cors
from fastapi import FastAPI

app = FastAPI()

setup_cors(app)

app.include_router(pokemon_router)
