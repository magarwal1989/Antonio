from util.pagebase import PageBase
from conftest import logger
from ..page_objects.dispatch_details import DispatchDetails



class DispatchCalender(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    current_date = "xpath@@//td[contains(@class,'fc-widget')][contains(@class,'today')]"

    def select_current_date(self):


        self.click(self.current_date)
        return DispatchDetails(self.get_current_driver())







