import pytest


@pytest.mark.skip
def test_firstProgramming():
    print("Hello")
    assert "hello" == "hi"


@pytest.mark.smoke
def test_secondGreekCreditCard():
    print("Good Morning")
    print("good Afternoon")
    print("good night")
    print("Altered the code")


def test_secondFix(setup):
    print("I will be executed at the second")
    print("Because I am lazy")
    print("night")
    print("day")
