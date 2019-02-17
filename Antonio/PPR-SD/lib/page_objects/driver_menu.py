from util.pagebase import PageBase
from conftest import logger
from ..page_objects.driver_lists_page import DriverListsPage

class DriverMenu(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    driver_lists = "xpath@@//a[@id='driver_index']"

    def select_driver_list(self):

        self.log_obj.write("Selecting driver lists")
        self.click(self.driver_lists)
        return DriverListsPage(self.get_current_driver())







