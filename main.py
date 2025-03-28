from fastapi import FastAPI
from contextlib import asynccontextmanager
from noteapp_server.database import init_db
from noteapp_server.routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router, prefix="/auth", tags=['Authentication'])

