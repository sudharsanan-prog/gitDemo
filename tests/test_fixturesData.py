import pytest

from tests.BaseClass import BaseClass

pytest.mark.usefixtures("dataLoad")


class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad)
        print(dataLoad[2])
        print(dataLoad[0])
