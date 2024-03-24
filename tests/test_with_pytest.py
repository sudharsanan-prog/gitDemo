import pytest


@pytest.mark.skip
def test_firstProgramming():
    print("Hello")
    assert "hello" == "hi"


@pytest.mark.smoke
def test_secondGreekCreditCard():
    print("Good Morning")


def test_secondFix(setup):
    print("I will be executed at the second")
