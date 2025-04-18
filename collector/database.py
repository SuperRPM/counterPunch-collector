from sqlalchemy.orm import Session
from .models import News, SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    from .models import Base, engine
    Base.metadata.create_all(bind=engine)

def insert_news(db: Session, title: str, link: str, image_url: str, source: str, category: str, published_at: str):
    try:
        news = News(
            title=title,
            link=link,
            image_url=image_url,
            source=source,
            category=category,
            published_at=published_at
        )
        db.add(news)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"Error while inserting news: {e}")
        return False

def get_news(db: Session, source: str = None, category: str = None, limit: int = 10, offset: int = 0):
    query = db.query(News)
    
    if source:
        query = query.filter(News.source == source)
    if category:
        query = query.filter(News.category == category)
        
    return query.order_by(News.published_at.desc()).offset(offset).limit(limit).all() 