from sloom.Fetcher import *
import constants as w

def test_good_request():
    fetcher = Fetcher()
    url = w.TEST_URL
    response = fetcher.get_page(url)
    assert isinstance(response, Response)

def test_bad_request():
    fetcher = Fetcher()
    url = w.EMPTY_URL
    response = fetcher.get_page(url)
    assert isinstance(response, RequestError)

def test_get_pages():
    fetcher = Fetcher()
    urls = [
        w.TEST_URL,
        w.TEST_URL,
        w.TEST_URL
    ]
    responses = fetcher.get_all_pages(urls)
    assert responses.count() == len(urls)

def test_filter_pages():
    fetcher = Fetcher()
    urls = [
        w.TEST_URL,
        w.EMPTY_URL,
        w.TEST_URL
    ]
    responses = fetcher.get_all_pages(urls)
    responses.removeErrors()
    assert responses.count() < len(urls)