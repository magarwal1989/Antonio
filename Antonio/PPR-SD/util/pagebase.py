"""
Abstract base class for automating web pages using Selenium WebDriver
This is the base class that all the classes representing various pages
of application inherit from. This class contains all selenium actions.
"""
from time import sleep


from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from ..Utils.DriverClass import browserDictionary
from ...generic_libraries.libraries.web.page_base import PageBase
from retry import retry


from selenium.webdriver.common.by import By




CurrentDriverInstance=None

class pagebase():
   
    def __init__(self, selenium_driver):
            self.driver = selenium_driver
            self.timeout = 30
           

    def clickElement(self, element):
        """
        Clicks the given element
        :param locator: Element locator strategy
        :return: element
        """

        if element is not None:
            element.click()
        else:
            raise Exception("Could not click on locator " )
        return element

    def open(self,url,wait_time=2):
        "Visit the page base_url + url"
        
         self.driver.get(url)
        

   
    def move_and_Doubbleclick(self, locator):
        """
        Move and click to the given element using
        selenium action class
        :param element: webelement instance
        :return: element
        """
        element = self.find_element(locator)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).double_click(element).perform()

        except Exception as e:
            raise Exception("Could Not click locator {} due to {}".format(element, e))
        return element

    def execute_javascript_doubbleClick(self,locator):
        """
        Execute doble click usign java script on the element found through the locator
        selenium action class
        :param element: webelement instance
        :return: element
        """
        element = self.find_element(locator)
        self.driver.execute_script("var evt = document.createEvent('MouseEvents');" + "evt.initMouseEvent('dblclick',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" + "arguments[0].dispatchEvent(evt);", element)

    def execute_javascript_Click(self,locator):
        """
        Execute single click usign java script on the element found through the locator
        selenium action class
        :param element: webelement instance
        :return: element
        """
        self.javascript_click(locator)

    def rightClickElement(self, locator):
        """
        Perform right click action on an element
        selenium action class
        :param element: webelement instance
        :return: element
        """
        element = self.find_element(locator)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).context_click().perform()
        except Exception as e:
            raise Exception("Could Not right click locator {} due to {}".format(element, e))
        return element


    def click_and_Hold(self, locator):
        """
        Move and click to the given element using
        selenium action class
        :param element: webelement instance
        :return: element
        """
        element = self.find_element(locator)
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).click_and_hold().perform()
        except Exception as e:
            raise Exception("Could Not click locator {} due to {}".format(element, e))
        return element


    def drag_and_drop_by_offset(self, draggable_loc, xoffset , yoffset):
            """
            Performs drag and drop action using selenium action class
            :param draggable: draggable element
            :param droppable: droppable element
            :return:
            """
            element = self.find_element(draggable_loc)
            try:
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(element,xoffset,yoffset)
            except Exception as e:
                raise e

    def setAttribute(self,element,attributeName,attributeValue):

        self.driver.execute_script("arguments[0].setAttribute('"+attributeName+"','"+attributeValue+"')", element)

  

    def _capture_screenshot(self,name):
        self.driver.get_screenshot_as_file(name)

   

    def getColourOfElement(self,locator):
        """"
        This method will get the color properties of the element
        """
        element = self.find_element(locator)
        return element.value_of_css_property('color')

    @retry((StaleElementReferenceException, ElementNotVisibleException), tries=5, delay=2)
    def get_text_Element(self, element):
        """
        get  the inner text of given element
        :param locator: Element
        :return: text
        """

        return element.text

    def splitStringAndGetValue(self,InputString,splitBy,index):
        """"
        This function will split the input string by the delimmiter mentioned and retuen thhe value of the indexed key
        """
        splitString=InputString.strip().split(splitBy)
        attribute = splitString[index]
        return attribute


    def wait_for_element_by_xpath(self, locator, timeout=60):
        """"
        xpath without @@
        """
        xpath=self.splitStringAndGetValue(locator,"@@",1)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH,xpath)))
            return True
        except TimeoutException:
            return False
        except WebDriverException as w:
            raise Exception("Exception occured while waiting for element with locator {} due to error {}".
                            format(locator, w))

    def wait_for_invisibility_element_by_xpath(self, locator, timeout=60):
        """"
        xpath without @@
        """
        xpath=self.splitStringAndGetValue(locator,"@@",1)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.XPATH,xpath))
            )
            return True
        except:
            return False



    def set_field_without_wait(self, locator, element_value):
        """
        Locates the element by specified locator and then sets its value
        :param locator: Element locator strategy
        :param element_value: value to be written
        :return: element
        """
        webelement = self.find_element(locator)
        try:
            self.hover(locator)
            webelement.send_keys(Keys.CONTROL, 'a')
            webelement.clear()
            webelement.send_keys(element_value)
        except Exception as e:
            raise Exception("Could not write on the the element {} due to {}".
                            format(webelement, e))

        return webelement

