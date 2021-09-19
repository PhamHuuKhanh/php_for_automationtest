from appium.webdriver.common.mobileby import MobileBy

from src.utils import logger
from src.utils.appium_element import send_keys, tap


class LoginScreen:
    # ELEMENT LOCATORS:
    __USERNAME_TXT_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@content-desc='userName']")
    __PASSWORD_TXT_FIELD = (MobileBy.XPATH, "//android.widget.EditText[@content-desc='userPassword']")
    __LOGIN_BTN = (MobileBy.ID, "com.pizzahut.singapore.test:id/btnLogin")

    # ACTION
    def login(self, username, password):
        logger.info("Enter user name %s ", username)
        send_keys(self.__USERNAME_TXT_FIELD, username)
        logger.info("Enter password %s ", password)
        send_keys(self.__PASSWORD_TXT_FIELD, password)
        logger.info("Click on login button")
        tap(self.__LOGIN_BTN)
