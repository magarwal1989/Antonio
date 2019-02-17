from util.pagebase import PageBase
from conftest import logger



class RouteAssignment(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    driver_list = "xpath@@//select[@id='driver']"
    submit = "xpath@@//input[@name='submit']"

    def assign_driver(self,driver_name):
        self.sleep_in_seconds(5)
        self.select_dropdown_option(self.driver_list,driver_name)

    def click_assign_event(self):
        self.click(self.submit)
        self.sleep_in_seconds(5)









