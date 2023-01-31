from sloom.href import href


# test sub page of origin site
def test_url():
    my_href = href("/tools", "google.com", "https://www")
    assert my_href.url() == "https://www.google.com/tools"

def test_str():
    my_href = href("/tools", "google.com", "https://www")
    assert my_href.__str__() == "https://www.google.com/tools"

def test_subdomain():
    my_href = href("/tools", "google.com", "https://newsroom")
    assert my_href.url() == "https://newsroom.google.com/tools"

# test full url
def test_newSite():
    my_href = href("https://www.google.com/tools", "google.com", "https://www")
    assert my_href.url() == "https://www.google.com/tools"
