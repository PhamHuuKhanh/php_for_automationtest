import subprocess
from src.consts.consts import Consts
from src.utils import logger, yaml_util
from appium import webdriver
import sys
import appscript
import time

# check env and platform to run test
config = yaml_util.load(Consts.DATA_CONFIG_DIR)
env = config["run"]["env_default"]
platform = config["run"]["platform_default"]
for x in sys.argv:
    print(x)
    if(x =="android"):
        platform = "android"
    if(x == "ios"):
        platform = "ios"
    if (x == "dev"):
        env = "dev"
    if (x == "pro"):
        env = "pro"

logger.info("Env is: "+env)
logger.info("Platform is: "+platform)

# Check appium is open or not
output = subprocess.getoutput("ps -A | grep appium")
if(output.find("node") == -1): # -1 is not run appium
    appscript.app('Terminal').do_script('appium --session-override')
    logger.info("[Appium]: Start with comment: appium --session-override")
    time.sleep(5)
else:
    logger.info("[Appium]: Had started before")

logger.info("=== Start Application ===")
# Android - Dev - Universal

desired_cap = {
    'platformName': 'Android',
    'noReset': 'true',
    'platformVersion': config["Device_Remi"]["version_android"],
    'deviceName': config["Device_Remi"]["name"],
    'appPackage': config["Android_Dev_JP"]["appPackage"],
    'appActivity': config["Android_Dev_JP"]["appActivity"]
}
logger.info("Open app")
driver = webdriver.Remote(Consts.HUB_URL, desired_cap)
