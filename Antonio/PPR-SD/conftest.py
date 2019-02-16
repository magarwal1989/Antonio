import os
from os import environ
from random import randint
from base_logger import BaseLogging

import pytest
logger = BaseLogging("TEST_EXECUTION_LOGS")



def pytest_runtest_setup(item):
    """ called before ``pytest_runtest_call(item). """
    # do some stuff`
    try:
        logger = BaseLogging(item.name)
    except FileNotFoundError as f:
        logger = BaseLogging("TEST_EXECUTION_LOGS")
        logger.write("TEST SETUP RUNNING FOR TEST  "+item.name)

def pytest_runtest_teardown(item):
    """ called before ``pytest_runtest_call(item). """
    # do some stuff`
    try:
        logger = BaseLogging(item.name)
    except FileNotFoundError as f:
        logger = BaseLogging("TEST_EXECUTION_LOGS")
        logger.write("TEST TEAR DOWN COMPLETED "+item.name)

def get_project_root():
    path = os.path.join(os.path.dirname(__file__),'..')
    return os.path.abspath(path)

@pytest.fixture(autouse=True,scope='session')
def make_dir():
    make_results_dir()
    make_screenshots_dir()


def make_results_dir():
    """"
    Make the reuired directory
    """
    PROJECT_ROOT = get_project_root()
    if not os.path.exists(os.path.join(PROJECT_ROOT, 'Results')):
        os.makedirs(os.path.join(PROJECT_ROOT, 'Results'))
    return os.path.join(PROJECT_ROOT, 'Results')


def make_screenshots_dir():
    """"
    Make the reuired directory
    """
    PROJECT_ROOT = get_project_root()
    if not os.path.exists(os.path.join(PROJECT_ROOT, 'Screenshots')):
        os.makedirs(os.path.join(PROJECT_ROOT, 'Screenshots'))



def getScreeshotDirectoryLocation():
    PROJECT_ROOT = get_project_root()
    return os.path.join(PROJECT_ROOT,'Screenshots')


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    #MakeDirectory()
    try:
        """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        if report.when == 'setup':
            logger.write("TEST SETUP "+report.outcome)
        if report.when == 'call':
            logger.write("Test Finished"+" "+report.outcome)
        if report.when == 'teardown':
            logger.write("TEST TEARDOWN COMPLETED "+report.outcome)



        if report.when == 'call' or report.when == "setup" or report.when == 'teardown':
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                ran_num = generate_Random_Number()
                name_screenshot = report.nodeid.split("::")[-1]+ "_" + ran_num
                if ("/") in name_screenshot:
                    name_screenshot = name_screenshot.replace("/", '_')
                screenshot_location_local = getScreeshotDirectoryLocation()
                names_of_files = _capture_screenshot(screenshot_location_local,name_screenshot)

    except Exception as e:
        logger.write(" Error in Generating the Pytest report ----->"+(str(e)),"warn")



def _capture_screenshot(location,name):
    """"
    capture screenshot
    """

    #from util.pagebase import Pagebase
    #Pagebase.get_current_driver_instance().save_screenshot(location+"/"+name+"_"+".png")
    pass

def generate_Random_Number():
    """"
    Generates the random number to append with the screenshot
    """
    return str((randint(0, 9999999)))

