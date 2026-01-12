"""
TalentProof - Core Screening Engine
FastAPI application entry point.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.routes.resume_routes import router as resume_router

app = FastAPI(
    title="TalentProof API",
    description="Agentic Talent Intelligence Platform - Core Screening Engine",
    version="0.1.0"
)

# CORS middleware for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(resume_router)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "AIHR is healthy"}
