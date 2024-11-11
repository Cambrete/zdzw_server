from fastapi import FastAPI
from contextlib import asynccontextmanager
from middlewares.cors_middleware import add_middlewares
from routes.static_routes import register_static_routes
from routes.auth import router as auth_router
from database.database import init_db

# Initialize database
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
add_middlewares(app)

#Register static routes
register_static_routes(app)

# Register authentication routes
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000)

