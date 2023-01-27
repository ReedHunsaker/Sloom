# test slooom/scraper.py
from sloom import Fetcher
from sloom import Scraper

# used for all tests
fetcher = Fetcher()
response = fetcher.get_page("http://example.com/api/123")
scraper = Scraper(response)

def test_scraper_getTitle():
    assert scraper.title == "Example Domain"