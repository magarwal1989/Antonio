"""
Base class for automating web pages using Selenium WebDriver
This is the base class that all the classes representing various pages
of application inherit from. This class contains all selenium actions.
"""

from enum import Enum
from time import sleep
from retry import retry
from PIL import Image

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


class PageBase(object):
    """
    Base Class for web related operations using Selenium WebDriver
    """

    def __init__(self, driver):
        """
        Provides webdriver instance to the classes inheriting it
        :param browser_type: browser, e.g. IE, Firefox, Chrome
        :param driver: WebDriver object
        """
        self._driver = driver



    def open(self, url, wait_time=2):
        """
        Visit the page base_url + url
        :param url: URL to be opened
        :param wait_time: time to wait till url opens
        :return:
        """
        # url = self.base_url + url
        if self._driver.current_url != url:
            self._driver.get(url)
        self.sleep_in_seconds(wait_time)

    def get_current_driver(self):
        """
        Return current driver
        :return: current driver instance
        """
        return self._driver

    def get_current_title(self):
        """
        Get the current title of the opened browser
        :return: current browser title
        """
        return self._driver.title

    def get_current_url(self):
        """
        Get the current URL
        :return: Return current URL
        """
        return self._driver.current_url

    def is_element_selected(self, locator):
        """
        Check whether provided element is selected
        :param locator: Element locator strategy
        :return: True or False about the element selection
        """
        element = self.find_element(locator)
        return element.is_selected()

    def is_element_enabled(self, locator):
        """
        Returns whether given element is enabled or not
        :param locator: Element locator strategy
        :return: True if given element is enabled else returns false
        """
        element = self.find_element(locator)
        return element.is_enabled()

    @retry(StaleElementReferenceException, tries=5, delay=2)
    def click(self, locator):
        """
        Clicks the given element
        :param locator: Element locator strategy
        :return: element
        """
        element = None
        if isinstance(locator, str):
            element = self.find_element(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            element.click()
        else:
            raise Exception("Could not click on the element with locator {}".
                            format(locator))

    def javascript_click(self, locator):
        element = None
        if isinstance(locator, str):
            element = self.find_element(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            self._driver.execute_script("arguments[0].click();", element)
        else:
            raise Exception("Could not click on locator " +locator)

    def set_field(self, locator, element_value):
        """
        Locates the element by specified locator and then sets its value
        :param locator: Element locator strategy
        :param element_value: value to be written
        :return: element
        """
        webelement = self.find_element(locator)
        try:

            webelement.send_keys(element_value)
        except Exception as e:
            raise Exception("Could not write on the the element {} due to {}".
                            format(webelement, e))

        return webelement

    def get_text(self, locator):
        """
        get  the inner text of given element
        :param locator: Element locator strategy
        :return: text
        """
        try:
            element = self.find_element(locator)
        except Exception as e:
            raise Exception("Could not get the text of the the element with locator {} due to {}".
                            format(locator, e))
        return element.text

    def get_element_text(self, element):
        """
        get  the inner text of given element
        :param locator: Element locator strategy
        :return: text
        """
        # element = self.find_element(locator)
        return element.text

    def is_element_displayed(self, locator):
        """
        Returns whether given element is displayed or no
        :param locator: Element locator strategy
        :return: True if given element is displayed else returns false
        """
        try:
            element = self.find_element(locator)
        except:
            return False
        return element.is_displayed()

    def switch_to_frame(self, frame_id):
        """
        Switch to the given frame based on id
        :param frame_id: id of the frame (can be xpath also)
        :return:
        """
        self._driver.switch_to_frame(frame_id)

    def switch_to_main_window(self):
        """
        Switch to the main browser window
        :return:
        """
        self._driver.switch_to_default_content()

    def move_and_click(self, locator):
        """
        Move and click to the given element using
        selenium action class
        :param locator: Element locator strategy
        :return: element
        """
        element = self.find_element(locator)
        try:
            action = ActionChains(self._driver)
            action.move_to_element(element).click().perform()
        except Exception as e:
            raise Exception("Could Not click locator {} due to {}".format(element, e))
        return element

    def click_and_move_by_offset(self, locator, offset):
        element = self.find_element(locator)
        drawing = ActionChains(self._driver) \
            .move_to_element(element) \
            .click_and_hold(element) \
            .move_by_offset(*offset) \
            .release()
        drawing.perform()

    def find_element(self, locator, timeout=5):
        """
        Find and return element based on the given locator value
        E.g: draggableElement = ("xpath@@//div[@id='draggable']")
        :param locator: Element locator strategy
        :return: Element
        """
        try:
            return WebDriverWait(self._driver, timeout=timeout) \
                .until(EC.presence_of_element_located(self.__get_by(locator_with_strategy=locator)),message = "Timed out after {} seconds while waiting to find the element with locator {} ".format(timeout,locator))
        except Exception as e:
            raise Exception("Could Not Find Element with locator {} due to error {} ".format(locator,str(e)))



    def __get_by(self, locator_with_strategy):
        """
        Get and return By instance based on the locator strategy
        :param locator_with_strategy: Element locator strategy
        :return: By instance of the element
        """

        if "@@" not in locator_with_strategy:
            locator_with_strategy = Strategy.ID.value + "@@" + locator_with_strategy

        strategy_and_locator = str(locator_with_strategy).split("@@")
        strategy = strategy_and_locator[0]
        locator = strategy_and_locator[1]
        by = None
        if strategy == Strategy.XPATH.value:
            by = (By.XPATH, locator)
        elif strategy == Strategy.ID.value:
            by = (By.ID, locator)
        elif strategy == Strategy.CSS.value:
            by = (By.CSS_SELECTOR, locator)
        elif strategy == Strategy.TAGNAME.value:
            by = (By.TAG_NAME, locator)
        else:
            raise Exception(" Incorrect locator specified . Locator has to be either xpath,id,css,tagname -->" + locator_with_strategy)
        return by

    def find_elements(self, locator):
        """
        Find and return the list of webelements based on the given locator value
        :param locator: Element locator strategy
        :return: list of the elements
        """
        try:
            return self._driver.find_elements(*self.__get_by(locator_with_strategy=locator))
        except Exception as e:
            raise Exception("Could Not Find Elements with locator {} due to error {}".format(locator,str(e)))

    @retry(StaleElementReferenceException, tries=5, delay=2)
    def get_attribute(self, locator, attribute):
        """
        Get the provided attribute value for the given element
        :param locator: Element locator strategy
        :param attribute: attribute
        :return: value of the attribute
        """
        if isinstance(locator, WebElement):
            return locator.get_attribute(attribute)
        else:
            element = self.find_element(locator)
            return element.get_attribute(attribute)

    def drag_and_drop(self, draggable, droppable):
        """
        Performs drag and drop action using selenium action class
        :param draggable: draggable element
        :param droppable: droppable element
        :return:
        """
        try:
            action = ActionChains(self._driver)
            action.click_and_hold(draggable).perform()
            action.move_to_element(droppable).perform()
            action.release(droppable).perform()
        except Exception as e:
            raise e

    def sleep_in_seconds(self, seconds=1):
        """
        Method for hard wait as per given seconds
        :param seconds: time in seconds
        :return:
        """
        sleep(seconds)

    def select_value_from_dropdown(self, locator, value):
        """
        It will select value from dropdown based on visible text
        :param locator: dropdwon Element locator strategy
        :return:
        """
        element = self.find_element(locator)
        select = Select(element)
        sleep(3)
        select.select_by_visible_text(value)

    def explicit_wait(self, locator):
        """
        Smart Wait in Selenium, wait till element is clickable
        :param locator: Element locator strategy
        :return: Found Element
        """
        element = self.find_element(locator)
        try:
            element = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(element))
        except Exception as e:
            raise e
        return element
    def explicit_wait_til_alert_is_present(self,timeout=10):
        """
        Smart Wait in Selenium, wait till alert is present
        :param locator: Element locator strategy
        :return: Found Element
        """
        try:
            element = WebDriverWait(self._driver, timeout).until(EC.alert_is_present())
        except Exception as e:
            raise e
        return element

    def select_dropdown_option(self, locator, option_text):
        """
        Selects the option in the drop-down based on the tag text
        :param locator: element
        :param option_text: value to be selected
        :return:
        """
        dropdown = self.find_element(locator)
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

    def hit_enter(self, locator, wait_time=2):
        """
        Hit Enter
        :param locator: element
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.ENTER)
            self.sleep_in_seconds(wait_time)
        except Exception as e:
            raise e

    def send_keys(self, locator, *keys):
        """
        send keys to locator
        :param locator: element
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(*(keys))
        except Exception as e:
            raise e

    def scroll_down(self, locator, wait_time=2):
        """
        Scroll down WebPage
        :param locator: locator
        :param wait_time: time to wait
        :return:
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.PAGE_DOWN)
            self.sleep_in_seconds(wait_time)
        except Exception as e:
            raise e

    def hover(self, locator, wait_seconds=2):
        """
        Hover over the element
        :param locator: locator
        :param wait_seconds: time to wait
        :return:
        """
        element = self.find_element(locator)
        action_obj = ActionChains(self._driver)
        action_obj.move_to_element(element)
        action_obj.perform()
        self.sleep_in_seconds(wait_seconds)

    def read_browser_console_log(self, log_type='browser'):
        """
        Read Browser Console log
        :param log_type: driver.get_log('browser')
            driver.get_log('driver')
            driver.get_log('client')
            driver.get_log('server')
        :return: logs
        """
        return self._driver.get_log(log_type)

    def execute_javascript(self, js_script):
        """
        Execute javascipt
        :param js_script:
        :return:
        """
        try:
            self._driver.execute_script(js_script)
        except Exception as e:
            raise e

    def accept_alert(self):
        """
        Accepts Java Alert
        :return:
        """
        try:
            self._driver.switch_to_alert().accept()
        except NoAlertPresentException:
            raise NoAlertPresentException

    def dismiss_alert(self):
        """
        Dismiss Java Alert
        :return:
        """
        try:
            self._driver.switch_to_alert().dismiss()
        except NoAlertPresentException:
            raise NoAlertPresentException

    def wait_till_element_is_present(self, locator, timeout=10):
        """
        WebDriver Explicit wait till element is present
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        try:
            element = WebDriverWait(self._driver, timeout). \
                until(EC.presence_of_element_located(self.__get_by(locator)))
            return element
        except Exception as e:
            raise e

    def wait_till_element_is_visible(self, locator, timeout=10):
        """
        WebDriver Explicit wait till element is visible, once appeared wait will over
        :param locator: element to be checked
        :param timeout: timeout
        :return:
        """
        try:
            element = WebDriverWait(self._driver, timeout). \
                until(EC.visibility_of_element_located(self.__get_by(locator)))
            return element
        except Exception as e:
            raise e



    def teardown_browser(self):
        """
        Close all browser instances
        :return:
        """
        self._driver.quit()

    def close_browser(self):
        """
        Close current browser instance
        :return:
        """
        self._driver.close()


    def maximize_browser(self):
        """
        Maximize the browser
        :return:
        """
        self._driver.maximize_window()

    def back(self):
        """
        browser back button
        :return:
        """
        self._driver.back()

    def is_element_present(self, locator, timeout=2):
        """
        Check the presence of element.
        :return: Boolean
        """
        try:
            WebDriverWait(self._driver, timeout=timeout) \
                .until(EC.presence_of_element_located(self.__get_by(locator)))
        except TimeoutException:
            return False
        except Exception as e:
            raise Exception("Could Not Verify Element Presence {} due to error {}".format(locator, str(e)))
        return True

    def get_css_value(self, locator, css_property):
        """"
        This method will get the CSS property of the element
        :return: CSS property Value

        Usage
        get_css_value(locator,"color")
        get_css_value(locator,"font-family")
        get_css_value(locator,"font-size")
        The above code will return value in RGB format such as “rgba(36, 93, 193, 1)”
        """
        element = self.find_element(locator)
        return element.value_of_css_property(css_property)

    def get_current_window_handle(self):
        """
        Returns the handle of the current window.
        :return: string containing current window handle
        """
        return self._driver.current_window_handle

    def get_window_handles(self):
        """
        Returns the list containing handles of all windows within the current session.
        :return: list containing all opened window handles in current session
        """
        return self._driver.window_handles

    def switch_to_new_window(self, win_handle):
        """
        Switch to window corresponding to windows handle id
        :return:
        """
        self._driver.switch_to_window(win_handle)

    def refresh_browser(self):
        """
        Refreshes the page
        :return:
        """
        self._driver.refresh()

   

class Strategy(Enum):
    """
    Locator Strategy Constants
    """
    XPATH = "xpath"
    ID = "id"
    CSS = "css"
    TAGNAME = "tag name"
