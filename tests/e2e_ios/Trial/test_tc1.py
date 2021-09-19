from src.utils.log import logger
from tests.base_test import BaseTest
from src.app_android.JP.screens_jp import *
from src.app_android.action_android import *

class TC2(BaseTest):

    def test_11_changelanguage(self):
        logger.info("Tc1: change language")

        current_language = get_text(Welcome_Screen.txtview_language)
        if (current_language == "日本語"):
            assert get_text(Welcome_Screen.textview_title) == "アカウントを使って始めましょう"
            tap_on(Welcome_Screen.btn_changelaguage)
            tap_on(Welcome_Screen.language_en)
            assert get_text(Welcome_Screen.textview_title) == "Use your account to get started"
        elif (current_language == "English"):
            assert get_text(Welcome_Screen.textview_title) == "Use your account to get started"
            tap_on(Welcome_Screen.btn_changelaguage)
            tap_on(Welcome_Screen.language_jp)
            assert get_text(Welcome_Screen.textview_title) == "アカウントを使って始めましょう----"
            tap_on(Welcome_Screen.btn_changelaguage)
            tap_on(Welcome_Screen.language_en)
    def test_12_taponsigin(self):
        logger.info("HELLO2")
        tap_on(Welcome_Screen.btn_signin_signup)
        assert get_text(Signin_Screen.txtlink_forgotpass) == "Forgot your password?"
        screenshot("22")
