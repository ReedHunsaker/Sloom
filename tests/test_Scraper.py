# test slooom/scraper.py
from sloom import Scraper
from sloom import Fetcher
import constants as w

# used for all tests
fetcher = Fetcher()
response = fetcher.get_page(w.TEST_URL)
scraper = Scraper(response)

def test_scraper_getTitle():
    assert scraper.title == w.TEST_WEBSITE_TITLE
