import feedparser
from typing import List, Dict
from datetime import datetime
from sqlalchemy.orm import Session
from .config import RSS_FEEDS
from .database import insert_news

def parse_rss_feed(url: str, source: str, category: str) -> List[Dict]:
    feed = feedparser.parse(url)
    entries = []
    
    for entry in feed.entries:
        # Extract image URL if available
        image_url = None
        if 'media_content' in entry:
            for media in entry.media_content:
                if media.get('type', '').startswith('image/'):
                    image_url = media.get('url')
                    break
        
        # Convert published date to datetime
        published_at = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z')
        
        news_item = {
            'title': entry.title,
            'link': entry.link,
            'image_url': image_url,
            'source': source,
            'category': category,
            'published_at': published_at
        }
        entries.append(news_item)
    
    return entries

def fetch_all_feeds(db: Session):
    for source, feeds in RSS_FEEDS.items():
        for feed_url in feeds:
            # Extract category from URL
            category = feed_url.split('/')[-1].replace('.xml', '')
            
            try:
                entries = parse_rss_feed(feed_url, source, category)
                for entry in entries:
                    insert_news(
                        db=db,
                        title=entry['title'],
                        link=entry['link'],
                        image_url=entry['image_url'],
                        source=entry['source'],
                        category=entry['category'],
                        published_at=entry['published_at']
                    )
                print(f"Successfully processed {len(entries)} entries from {source} - {category}")
            except Exception as e:
                print(f"Error processing feed {feed_url}: {e}") 