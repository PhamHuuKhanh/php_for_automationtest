from src.app_ios.screens.home_screen import HomeScreen
from src.app_ios.screens.login_screen import LoginScreen

from tests.base_test import BaseTest


class TC1(BaseTest):

    __VALID_USER_NAME = "brian@pizzahut.io"
    __VALID_PASSWORD = "112358@Anz"

    def test_tc1_simple_flow(self):
        home_screen = HomeScreen()
        home_screen.tap_sign_in_button()
        login_screen = LoginScreen()
        login_screen.login(self.__VALID_USER_NAME, self.__VALID_PASSWORD)
