from pathlib import Path


class Consts:
    # Project structure
    PROJECT_ROOT = str(Path(__file__).parent.parent.parent)
    PROJECT_NAME = PROJECT_ROOT.split("/")[-1]
    DATA_CONFIG_DIR = PROJECT_ROOT + "/config/data_config.yaml"
    LOG_FILE = PROJECT_ROOT + "/logs/" + "%s.log"
    # DATA_FILE = PROJECT_ROOT + "/data/%s/%s.properties"
    SCREENSHOT_DIR = PROJECT_ROOT + "/screenshots/"
    REPORT_DIR = PROJECT_ROOT + "/reports/"


    # Apps
    BUNDLE_ID_UAT = "com.abc..."
    BUNDLE_ID_PROD = "com.xyz..."

    # Selenium & Appium
    HUB_URL = "http://localhost:4723/wd/hub"