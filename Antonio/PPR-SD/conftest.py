import ftplib
import os
from os import environ
from random import randint
from.Properties import Constants


import pytest



test_log_obj = BaseLogging("TEST_EXECUTION_LOGS")



def pytest_runtest_setup(item):
    """ called before ``pytest_runtest_call(item). """
    # do some stuff`
    try:
        test_log_obj = BaseLogging(item.name)
    except FileNotFoundError as f:
        print("file not found error occured . Setting the log file name to TEST_EXECUTION_LOGS for the test " + item.name)
        test_log_obj = BaseLogging("TEST_EXECUTION_LOGS")
    test_log_obj.write("TEST SETUP RUNNING FOR TEST  "+item.name)

def pytest_runtest_teardown(item):
    """ called before ``pytest_runtest_call(item). """
    # do some stuff`
    try:
        test_log_obj = BaseLogging(item.name)
    except FileNotFoundError as f:
        print("file not found error occured . Setting the log file name to TEST_EXECUTION_LOGS for the test "+item.name)
        test_log_obj = BaseLogging("TEST_EXECUTION_LOGS")
    test_log_obj.write("TEST TEAR DOWN COMPLETED "+item.name)

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
    if not os.path.exists(os.path.join(PROJECT_ROOT, 'Screenshots_Streaming')):
        os.makedirs(os.path.join(PROJECT_ROOT, 'Screenshots_Streaming'))



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
            test_log_obj.write("TEST SETUP "+report.outcome)
        if report.when == 'call':
            test_log_obj.write(Constants.TEST_COMPLETED+" "+report.outcome)
        if report.when == 'teardown':
            test_log_obj.write("TEST TEARDOWN COMPLETED "+report.outcome)



        if report.when == 'call' or report.when == "setup" or report.when == 'teardown':
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                ran_num = generate_Random_Number()
                name_screenshot = report.nodeid.split("::")[-1]+ "_" + ran_num
                if ("/") in name_screenshot:
                    name_screenshot = name_screenshot.replace("/", '_')
                screenshot_location_local = getScreeshotDirectoryLocation()
                base_loc_ftp = "ftp://"+ftp_server+"/"+remote_dir+"/"
                names_of_files = _capture_screenshot(screenshot_location_local,name_screenshot)
                _upload_screenshot_ftp(ftp_server_lab_ip, username, password, remote_dir)
                for item in names_of_files:
                    baseNameFTP = base_loc_ftp + "/"+item

                    file_name = baseNameFTP
                    if file_name:
                        html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                               'onclick="window.open(this.src)" align="right"/></div>' % file_name
                        extra.append(pytest_html.extras.html(html))
            report.extra = extra
    except Exception as e:
        test_log_obj.write(" Error in Generating the Pytest report ----->"+(str(e)),"warn")



def _capture_screenshot(location,name):
    """"
    capture screenshot
    """
   # PageBase_OpSpace.getCurrentDriverInstance().save_screenshot(name)
    driver_dict = PageBase_OpSpace.getAllCurrentDriverInstance()
    names=[]
    for k,v in driver_dict.items():
        name_of_screenshot=location+"/"+name+"_"+k+".png"
        name_of_screenshot_without_location =name+"_"+k+".png"
        v.save_screenshot(name_of_screenshot)
        names.append(name_of_screenshot_without_location)
    return names

def generate_Random_Number():
    """"
    Generates the random number to append with the screenshot
    """
    return str((randint(0, 9999999)))

