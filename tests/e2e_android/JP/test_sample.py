from src.app_android.JP.screens_jp import *
from src.utils.log import logger
#from src.app_android.action_android import *

def test_sample():
    logger.info("đang trong tc 1")
    print("1")
   # assert True
    print("2")
    try:
        assert False
    except:
        print("ahihi")
    print("3")

def test_sample2():
    logger.info("đang trong tc 2")
    print("4")
    assert True
    print("5")

