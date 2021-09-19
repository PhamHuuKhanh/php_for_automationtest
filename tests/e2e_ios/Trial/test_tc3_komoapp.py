from src.utils.log import logger
from tests.base_test import BaseTest
from src.app_android.JP.screens_jp import *
# from src.app_android.action_android import *

class TC2(BaseTest):

    def test_22_khuyenmai(self):
        logger.info("HELLO---> qua file moi")
        #tap_on(Signin_Screen.btn_back)
        #tap_on(Welcome_Screen.btn_getcpupon)
        assert "-----" == "Please log in or create a new account to enjoy coupon(s)----"
    def test_33_khonglamgihet(self):
        logger.info("HELLO2")
        assert "1" == "1"
    def test_44_khonglamgihet(self):
        logger.info("HELLO2")
        assert "1" == "1"
    def test_55_khonglamgihet(self):
        logger.info("HELLO2")
        assert "1" == "2"

