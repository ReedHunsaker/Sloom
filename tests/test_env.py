from platform import python_version

def test_python_directory():
    assert python_version() == "3.10.0"
