import builtins

from appium.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def find_element(element: tuple, timeout=60) -> WebElement:
    """
    Find an element existing in DOM with a timeout in seconds.
    :return: WebElement if found
    :raise: NoSuchElementException if not found
    """
    driver = getattr(builtins, "driver_anvo")
    locator = element[0]
    value = element[1]
    try:
        return WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((locator, value)))
    except Exception:
        log = "Element not found with locator %s value '%s' after %d seconds" % (locator, value, timeout)
        raise NoSuchElementException(log)


def send_keys(element: tuple, value: str):
    find_element(element).send_keys(value)


def tap(element: tuple):
    find_element(element).click()
