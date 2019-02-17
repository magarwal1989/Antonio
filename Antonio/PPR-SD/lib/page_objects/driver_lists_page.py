from util.pagebase import PageBase
from conftest import logger
from ..page_objects.dispatch_details import DispatchDetails



class DriverListsPage(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    search_driver = "xpath@@//input[@type='search']"
    search_result = "xpath@@//table[@id='fileData']//tbody/tr[1]/td[1]"

    def search_for_driver(self,driver_name):
        self.set_field(self.search_driver, driver_name)
        self.hit_enter(self.search_driver)
        self.click(self.search_result)
        self.sleep_in_seconds(30)







