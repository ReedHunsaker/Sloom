from sloom.Fetcher import *

def test_good_request():
    fetcher = Fetcher()
    url = "https://httpbin.org/headers"
    response = fetcher.get_page(url)
    assert type(response) == type(Response(None, None))

def test_bad_request():
    fetcher = Fetcher()
    url = "https://httpbin.org/hidden-basic-auth/:user/:passwd"
    response = fetcher.get_page(url)
    assert type(response) == type(RequestError(None, None))

def test_get_pages():
    fetcher = Fetcher()
    urls = [
        "https://httpbin.org/headers",
        "http://example.com/api/123",
        "http://example.com/api/123"
    ]
    responses = fetcher.get_all_pages(urls)
    assert responses.count() == len(urls)

def test_filter_pages():
    fetcher = Fetcher()
    urls = [
        "https://httpbin.org/headers",
        "https://httpbin.org/hidden-basic-auth/:user/:passwd",
        "http://example.com/api/123"
    ]
    responses = fetcher.get_all_pages(urls)
    responses.removeErrors()
    assert responses.count() < len(urls)