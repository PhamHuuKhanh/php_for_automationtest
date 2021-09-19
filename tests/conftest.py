import os
from datetime import datetime
from urllib import request
import yaml
from py.xml import html

import pytest
from appium import webdriver
from src.app_android.action_android import screenshot
from src.consts.consts import Consts
from src.utils import logger, yaml_util
from src.utils.driver_setup import platform, env

# To get parameter on cmd: pytest testcasename --os ios --env pro
def pytest_addoption(parser):
    parser.addoption("--env", action="store")
    parser.addoption("--os", action="store")


@pytest.fixture(scope="session")
def setup_environment(request):
    logger.info("=== Start Run TestCases===")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    logger.info("=== Finish Pytest session ===")


# setup report image
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
       Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
       :param item:
       """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            #tc_name = report.nodeid.split("::")[2] + "_" + datetime.now().strftime("%d%m%Y%H%M%S")
            tc_name = datetime.now().strftime("%d%m%Y%H%M%S")
            print(tc_name)
            screenshot(tc_name)
            path_image = Consts.SCREENSHOT_DIR + tc_name + ".png"
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:150px;height:243px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % path_image
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# setup report path
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # to remove environment section
    config._metadata = None

    if not os.path.exists('reports'):
        os.makedirs('reports')

    config.option.htmlpath = Consts.REPORT_DIR + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"

def pytest_html_report_title(report):
    report.title = "Automation test report..."

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["env"] = env
    session.config._metadata["Platform"] = platform
    session.config._metadata["Design by:"] = "Dong Mon Khanh"