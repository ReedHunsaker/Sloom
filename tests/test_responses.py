import sys
sys.path.append('../NewsAPI')
from app.source.Responses import Responses
from app.source.Response import Response
from app.source.RequestError import RequestError
import io

def test_bad_append():
    capturedOutput = io.StringIO()          # Create StringIO object
    sys.stdout = capturedOutput                   #  and redirect stdout.
    responses = Responses()
    responses.append("string type")
    sys.stdout = sys.__stdout__                   # Reset redirect.
    assert "ERROR" in capturedOutput.getvalue()

def test_good_append():
    responses = Responses()
    responses.append(Response(None, None))
    assert responses.count() > 0

