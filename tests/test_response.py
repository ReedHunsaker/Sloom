from sloom.Response import Response

def test_getOrigin():
    response = Response("/", "https://wwww.google.com/tools")
    _, origin = response.getOrigin()
    assert origin == "google.com"