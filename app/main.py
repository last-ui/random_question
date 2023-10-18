from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.description)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
