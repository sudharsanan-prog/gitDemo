import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed at the last")


@pytest.fixture()
def dataLoad():
    print("we have to return a function")
    return ["A-404", "Astha Appartments", "Kudasen"]


@pytest.fixture(params=[("chrome", "is", "best"), "firefox", "IE"])
def classBrowser(request):
    return request.param
