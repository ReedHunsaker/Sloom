import sys
from sloom.Responses import *
from sloom.Response import *
import io

def test_bad_append():
    responses = Responses()
    try:
        responses.append("string type")
    except TypeError:
        assert True
    if responses.count == 0: assert False

def test_good_append():
    responses = Responses()
    responses.append(Response(None, None))
    assert responses.count() > 0

