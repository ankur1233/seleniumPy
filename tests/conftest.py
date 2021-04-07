import os
import time

import pytest
from pytest_html.hooks import pytest_html_results_summary

from base.selenium_driver import SeleniumDriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

# @pytest.yield_fixture()
# # @pytest.fixture()
# def setUp():
#     print("Running method level setUp")
#     yield
#     print("Running method level tearDown")
from pages.loginPage.MystoreHomePage import MystoreHomePage
from pages.loginPage.MystoresignPage import MystoresignPage

usr = ""  # user Name
password = ""
_driver = None


# @pytest.yield_fixture(scope="class")  # run one time per class
# # @pytest.fixture(scope="class")
# def oneTimeSetUp(request, browser, url):
#     print("Running one time setUp")
#     wdf = WebDriverFactory(browser)  # get instance of  WebDriverFactory & set browser value {__init__()}
#     driver = wdf.getWebDriverInstance()  # get driver instance from WebDriverFactory
#
#     lp = LoginPage(driver)  # Pass driver instance in page class
#
#     lp.login("test@email.com", "abcabc")
#
#     if request.cls is not None:
#         request.cls.driver = driver
#     yield driver
#     driver.quit()  # quit after every class
#     print("Running one time tearDown")


@pytest.yield_fixture(scope="class")
def setupmystore(request, browser, url):
    print("Inside class setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance(url)
    global _driver
    _driver = driver
    MystoresignPage(driver)
    MystoreHomePage(driver)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()  # quit after every class
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--url", help="Type app url")
    parser.addoption("--user", help="Type app url", default="Singh")
    parser.addoption("--password", help="Type app url", default="pass**pas")


@pytest.fixture(scope="session")  # run per session
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture(scope="class")
# def userName(request):
#     global usr
#     usr = request.config.getoption("--user")

def getUser():
    return usr


def getPassword():
    return password


@pytest.fixture(scope="session")  # run per session
def user(request):
    global usr
    print("User ::  " + request.config.getoption("--user"))
    usr = request.config.getoption("--user")


@pytest.fixture(scope="session")  # run per session
def password(request):
    global password
    print("User ::  " + request.config.getoption("--password"))
    password = request.config.getoption("--password")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    screen = SeleniumDriver(_driver)
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # resultMessage  # + "." + str(round(time.time() * 1000)) + ".png"
            file_name = str(round(time.time() * 1000)) + ".png"


            print("File Name :Link: " + file_name)
            # print("Path ::"+os.getcwd())
            # srt1= os.getcwd().find()
            # print()os.getcwdb()

            # file_name = "screenshots"+os.sep+time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))+".png"
            screen.screenShot(file_name)
            # _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

        report.extra = extra

