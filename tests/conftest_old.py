import builtins
import pytest
from src.consts.consts import Consts
from src.utils import logger, yaml_util
from appium import webdriver
# get param from cmd
def pytest_addoption(parser):
    parser.addoption("--env", action="store")


@pytest.fixture(scope="session")
def setup_environment(request):
    print("\x00")  # print a non-printable character to break a new line on console
    logger.info("=== Start Pytest session ===")
    env = str(request.config.getoption("--env"))  # env = uat_market_an  .??
    print("env la gi: "+env)
    env = "uat_market_khanh"
    app_env = env.split("_")[0]  # app_env = uat
    config = yaml_util.load(Consts.ENV_CONFIG_FILE % env)
    device_udid = config["devices"]["udid_iphone"]
    bundle_id = Consts.BUNDLE_ID_UAT if app_env == "uat" else Consts.BUNDLE_ID_PROD

    logger.info("Init Appium iOS driver")
   # desired_caps = {
        # "platformName": "iOS",
        # "deviceName": "I love coffee",
        # "automationName": "XCUITest",
        # "udid": device_udid,
        # "bundleId": bundle_id
        #"'platformName': 'Android',
        #'platformVersion': '10.0',
        #'deviceName': device_udid,
        #'appPackage': 'com.pizzahut.singapore.test',
        #'app': '/Users/voan/python_framework/app/app-dev-0.0.42-231120.apk'
  #  }

   # driver = webdriver.Remote(Consts.HUB_URL, desired_caps)
   # builtins.driver_anvo = driver


    #driver = webdriver.Remote(Consts.HUB_URL, desired_caps)
    #builtins.driver_anvo = driver


    import time

    desired_cap = {
        'platformName': 'Android',
        'platformVersion': '9',
        # 'deviceName': 'R58N958WQMN', Samsung os 11
        'deviceName': '179998977d26',  # Remi
        # app universal
        # 'appPackage': 'com.phdv.universal.sit',
        # 'appActivity': 'com.phdv.universal.feature.main.MainActivity'

        'appPackage': 'com.pizzahut.jp',
        'appActivity': 'com.pizzahut.jp.view.splash.SplashActivity'
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    builtins.driver_anvo = driver
    logger.info("Successfully")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    logger.info("=== Finish Pytest session ===")
