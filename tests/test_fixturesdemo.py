import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_demo(self):
        print("I'll execute now...")

    def test_demo1(self):
        print("I'll execute now...")
        print("say kudos")

    def test_demo2(self):
        print("I'll execute now...")

    def test_demo3(self):
        print("I'll execute now...")
