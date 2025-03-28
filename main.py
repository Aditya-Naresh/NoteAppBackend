from fastapi import FastAPI
from contextlib import asynccontextmanager
from noteapp_server.database import init_db
from noteapp_server.routers import auth, notes 
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=['Authentication'])

app.include_router(notes.router, prefix="/notes", tags=["Notes"])
