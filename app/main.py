from fastapi import FastAPI
from app.routes.notes_routes import router as notes_router

app = FastAPI(
    title="Smart Notes API",
    description="AI-powered notes app with MongoDB backend",
    version="1.0.0"
)

# Register routes
app.include_router(notes_router, prefix="/api/v1", tags=["Notes"])


@app.get("/")
def root():
    return {"message": "Smart Notes API chal raha hai! 🚀"}
