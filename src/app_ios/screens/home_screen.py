from appium.webdriver.common.mobileby import MobileBy

from src.utils.appium_element import tap


class HomeScreen:
    # ELEMENT LOCATORS
    # ----------------
    __SIGN_IN_BUTTON = (MobileBy.ID, "btnSignInSignUp")

    # ACTIONS
    # -------
    def tap_sign_in_button(self):
        tap(self.__SIGN_IN_BUTTON)
