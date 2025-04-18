from typing import Dict, List
import os
from dotenv import load_dotenv

load_dotenv()

# RSS Feed URLs
RSS_FEEDS: Dict[str, List[str]] = {
    "연합뉴스": [
        "https://www.yna.co.kr/rss/politics.xml",
        "https://www.yna.co.kr/rss/economy.xml",
        "https://www.yna.co.kr/rss/society.xml"
    ]
}

# Database Configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "counterpunch"),
    "port": int(os.getenv("DB_PORT", 3306))
}

# API Configuration
API_CONFIG = {
    "host": "0.0.0.0",
    "port": 8000
} 