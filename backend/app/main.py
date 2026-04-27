from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers.health import router as health_router

# Create all database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GDFC API",
    description="Backend API for the Gradey Dick Fan Club",
    version="0.1.0",
)

# Allow the React frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        # Add your deployed frontend URL here later, e.g.:
        # "https://gdfc.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health_router)