from flask import Flask, render_template, request, jsonify, session
from auto_scraper import AutoScraper
import os
import json
from datetime import datetime, timedelta
import threading
import time
import requests

app = Flask(__name__)
app.secret_key = 'zee-stream-secret-2024'

# Global cache for scraped data
CACHE = {
    'movies': [],
    'serials': [],
    'last_update': None,
    'is_scraping': False
}

CACHE_DURATION = 3 * 60 * 60  # 3 ghante

# IMDB API Configuration
IMDB_API_KEY = "k_19ykbw7b"  # Free tier
IMDB_BASE_URL = "https://imdb-api.com/en/API"

def is_cache_expired():
    """Check agar 3 ghante se zyada ho gaye"""
    if CACHE['last_update'] is None:
        return True
    return datetime.now() - CACHE['last_update'] > timedelta(hours=3)

def scrape_imdb_movies():
    """IMDB se latest movies scrape karo"""
    try:
        # Top 100 movies
        url = f"{IMDB_BASE_URL}/Top100Movies/{IMDB_API_KEY}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            movies = []
            
            for item in data.get('items', [])[:30]:  # Top 30
                movies.append({
                    'title': item.get('title'),
                    'year': item.get('year'),
                    'image': item.get('image'),
                    'rank': item.get('rank'),
                    'imdbID': item.get('id'),
                    'category': 'Hollywood',
                    'language': 'English',
                    'scrape_date': datetime.now().isoformat()
                })
            
            return movies
    except Exception as e:
        print(f"IMDB scrape error: {e}")
    
    return []

def scrape_hindi_movies():
    """Hindi movies ka fake data generate karo (real scraping ke liye bs)"""
    hindi_movies = [
        {'title': 'Dangal', 'year': '2016', 'category': 'Bollywood', 'language': 'Hindi', 'type': 'Movie'},
        {'title': 'Bajrangi Bhaijaan', 'year': '2015', 'category': 'Bollywood', 'language': 'Hindi', 'type': 'Movie'},
        {'title': 'PK', 'year': '2014', 'category': 'Bollywood', 'language': 'Hindi', 'type': 'Movie'},
        {'title': 'Dilwale Dulhania Le Jayenge', 'year': '1995', 'category': 'Bollywood', 'language': 'Hindi', 'type': 'Movie'},
        {'title': 'Sholay', 'year': '1975', 'category': 'Bollywood', 'language': 'Hindi', 'type': 'Movie'},
    ]
    
    for movie in hindi_movies:
        movie['scrape_date'] = datetime.now().isoformat()
    
    return hindi_movies

def scrape_punjabi_movies():
    """Punjabi movies"""
    punjabi_movies = [
        {'title': 'Carry On Jatta', 'year': '2012', 'category': 'Punjabi', 'language': 'Punjabi', 'type': 'Movie'},
        {'title': 'Jatt & Juliet', 'year': '2012', 'category': 'Punjabi', 'language': 'Punjabi', 'type': 'Movie'},
        {'title': 'Sardaar Ji', 'year': '2015', 'category': 'Punjabi', 'language': 'Punjabi', 'type': 'Movie'},
    ]
    
    for movie in punjabi_movies:
        movie['scrape_date'] = datetime.now().isoformat()
    
    return punjabi_movies

def auto_scraper_background():
    """Background mein har 3 ghante baad scrape karo"""
    while True:
        if is_cache_expired():
            print(f"[{datetime.now()}] Auto-scraping started...")
            CACHE['is_scraping'] = True
            
            try:
                # Scrape karo
                imdb_movies = scrape_imdb_movies()
                hindi_movies = scrape_hindi_movies()
                punjabi_movies = scrape_punjabi_movies()
                
                # Cache mein save karo
                CACHE['movies'] = imdb_movies + hindi_movies + punjabi_movies
                CACHE['last_update'] = datetime.now()
                
                print(f"✅ Auto-scrape complete: {len(CACHE['movies'])} items")
            except Exception as e:
                print(f"❌ Auto-scrape error: {e}")
            finally:
                CACHE['is_scraping'] = False
        
        time.sleep(60)  # Every minute check karo

# Background thread shuru karo
scraper_thread = threading.Thread(target=auto_scraper_background, daemon=True)
scraper_thread.start()

@app.route('/')
def home():
    """Homepage - Glassmorphism UI"""
    return render_template('index.html', 
                         site_name='ZEE STREAM',
                         description='Hindi | Punjabi | Bollywood | Hollywood')

@app.route('/api/movies')
def get_movies():
    """API - Sab movies return karo"""
    if not CACHE['movies'] or is_cache_expired():
        # Agar cache empty ho ya expire ho gaya
        imdb_movies = scrape_imdb_movies()
        hindi_movies = scrape_hindi_movies()
        punjabi_movies = scrape_punjabi_movies()
        
        CACHE['movies'] = imdb_movies + hindi_movies + punjabi_movies
        CACHE['last_update'] = datetime.now()
    
    # Filter by category agar param ho
    category = request.args.get('category', 'all')
    
    if category != 'all':
        movies = [m for m in CACHE['movies'] if m.get('category', '').lower() == category.lower()]
    else:
        movies = CACHE['movies']
    
    return jsonify({
        'success': True,
        'total': len(movies),
        'movies': movies,
        'last_update': CACHE['last_update'].isoformat() if CACHE['last_update'] else None,
        'cache_expires_in': f"{int((CACHE['last_update'] + timedelta(hours=3) - datetime.now()).total_seconds() / 60)} minutes"
    })

@app.route('/api/search')
def search():
    """Search movies by title"""
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify({'error': 'Query required'}), 400
    
    results = [m for m in CACHE['movies'] if query in m.get('title', '').lower()]
    
    return jsonify({
        'success': True,
        'query': query,
        'results': results,
        'count': len(results)
    })

@app.route('/api/categories')
def get_categories():
    """Sab categories return karo"""
    categories = set()
    
    for movie in CACHE['movies']:
        cat = movie.get('category', 'Unknown')
        if cat:
            categories.add(cat)
    
    return jsonify({
        'success': True,
        'categories': sorted(list(categories))
    })

@app.route('/api/status')
def status():
    """Server status"""
    return jsonify({
        'success': True,
        'status': 'running',
        'cached_movies': len(CACHE['movies']),
        'last_update': CACHE['last_update'].isoformat() if CACHE['last_update'] else 'Never',
        'is_scraping': CACHE['is_scraping'],
        'next_update': (CACHE['last_update'] + timedelta(hours=3)).isoformat() if CACHE['last_update'] else 'Soon',
        'version': '1.0.0',
        'site': 'zeestrempython.com'
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
