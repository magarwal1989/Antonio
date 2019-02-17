from util.pagebase import PageBase
from conftest import logger
from ..page_objects.dispatch_calender import DispatchCalender

class DispatchMenu(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    dispatch_calender = "xpath@@//a[contains(text(), 'Dispatch Calendar')]"

    def select_dispatch_calendar(self):

        self.log_obj.write("Selecting dispatch calendar from the Dispathc menu")
        self.click(self.dispatch_calender)
        return DispatchCalender(self.get_current_driver())







