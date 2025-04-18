from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from .config import API_CONFIG
from .rss_parser import fetch_all_feeds
from .database import get_db, get_news

app = FastAPI(title="CounterPunch Collector API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "CounterPunch Collector API"}

@app.post("/collect")
async def collect_news(db: Session = Depends(get_db)):
    try:
        fetch_all_feeds(db)
        return {"message": "News collection completed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/news")
async def get_news(
    source: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    try:
        news = get_news(db, source, category, limit, offset)
        return news
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "collector.main:app",
        host=API_CONFIG["host"],
        port=API_CONFIG["port"],
        reload=True
    ) 