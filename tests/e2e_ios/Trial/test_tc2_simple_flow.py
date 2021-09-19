from src.utils.log import logger

from src.app_android.JP.screens_jp import *
from src.app_android.action_android import *
from tests.base_test import BaseTest

class TC2(BaseTest):

    def test_tc222_simple_flow(self):
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
            assert get_text(Welcome_Screen.textview_title) == "アカウントを使って始めましょう"
            tap_on(Welcome_Screen.btn_changelaguage)
            tap_on(Welcome_Screen.language_en)

    def test_tc3_simple_flow(self):
        logger.info("HELLO")
        assert 1 == 2
    def test_tc333_simple_flow(self):
        logger.info("HELLO2")
