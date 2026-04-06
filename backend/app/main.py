from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import subjects, papers, analysis, strategy, drive

app = FastAPI(
    title="MarksIntel API",
    description="AI-Powered Exam Intelligence Platform for SPPU",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(subjects.router, prefix="/subjects", tags=["Subjects"])
app.include_router(papers.router, prefix="/papers", tags=["Papers"])
app.include_router(analysis.router, prefix="/analysis", tags=["Analysis"])
app.include_router(strategy.router, prefix="/strategy", tags=["Strategy"])
app.include_router(drive.router, prefix="/drive", tags=["Drive"])

@app.get("/")
def health_check():
    return {"status": "MarksIntel API is running", "version": "0.1.0"}
