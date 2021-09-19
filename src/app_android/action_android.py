import builtins

from appium.webdriver.common.touch_action import TouchAction
from src.consts.consts import Consts
from src.utils.log import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.utils.driver_setup import driver


def isID(element):
    if (element[0] == "id"):
        return True
    else:
        return False


def tap_on(element):
    wating(element)
    logger.info("[TAP ON] " + element[1])
    if (isID(element)):
        driver.find_element_by_id(element[1]).click()
    else:
        driver.find_element_by_xpath(element[1]).click()


def get_text(element):
    wating(element)
    if (isID(element)):
        text = driver.find_element_by_id(element[1]).text
        logger.info("[GET TEXT] " + element[1] + ": " + text)
        return text
    else:
        logger.info("[GET TEXT] " + " chua code lol")


def screenshot(name):
    logger.info("[SCREEN SHOT] name image is " + name)
    path = Consts.SCREENSHOT_DIR + name + ".png"
    #path = "/Users/phdvqc/Documents/GitHub/python-mobile-automation-test/screenshots/"+name+".png"
    #path = name+ ".png"
    logger.info(path)
    driver.save_screenshot(path)



def scroll_dow():
    logger.info("[SCROLL DOW] ")
    width_device = driver.get_window_size()['width']
    hight_device = driver.get_window_size()['height']
    # scroll a to b
    start_x = width_device / 2
    start_y = hight_device * 2 / 3
    end_x = width_device / 2
    end_y = hight_device * 1 / 3
    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()


def scroll_up():
    logger.info("[SCROLL UP] ")
    width_device = driver.get_window_size()['width']
    hight_device = driver.get_window_size()['height']
    # scroll a to b
    start_x = width_device / 2
    start_y = hight_device * 1 / 3
    end_x = width_device / 2
    end_y = hight_device * 2 / 3
    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()


def scroll_a_to_b(start_x, start_y, end_x, end_y):
    logger.info("[SCROLL A TO B] " + "(" + start_x + "," + start_y + ") " + "(" + end_x + "," + end_y + ")")
    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()


def wating(element):
    try:
        wait = WebDriverWait(driver, 20)
        if (isID(element)):
            currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, element[1])))
        else:
            currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH, element[1])))
        logger.info("[WATING] showed element: " + element[1])
    except:
        logger.info("[WATING] error element: " + element[1])

def checktextview(element, expected):
    assert get_text(element) == expected