from sloom.Fetcher import *

def test_good_request():
    fetcher = Fetcher()
    url = "https://www.npr.org/2023/01/20/1150416982/leopard-2-tank-ukraine"
    response = fetcher.get_page(url)
    assert type(response) == type(Response(None, None))

def test_bad_request():
    fetcher = Fetcher()
    url = "https://www.npr.org/20/01/98/lepard-2-tak-uraine"
    response = fetcher.get_page(url)
    assert type(response) == type(RequestError(None, None))

def test_get_pages():
    fetcher = Fetcher()
    urls = [
        "https://www.cnn.com/2023/01/20/opinions/alec-baldwin-manslaughter-charges-rust-filipovic/index.html",
        "https://www.nbcnews.com/news/us-news/5-memphis-police-officers-fired-trye-nichols-rcna66817",
        "https://www.washingtonpost.com/politics/2023/01/20/supreme-court-leak-justices-questioned/"
    ]
    responses = fetcher.get_all_pages(urls)
    assert responses.count() == len(urls)

def test_filter_pages():
    fetcher = Fetcher()
    urls = [
        "https://www.cnn.com/2023/01/20/opinions/alec-baldwin-manslaughter-charges-rust-filipovic/index.html",
        "https://www.nbcnews.com/-nicho17",
        "https://www.washingtonpost.com/politics/2023/01/20/supreme-court-leak-justices-questioned/"
    ]
    responses = fetcher.get_all_pages(urls)
    responses.removeErrors()
    assert responses.count() < len(urls)