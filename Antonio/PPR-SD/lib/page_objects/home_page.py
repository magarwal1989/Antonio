from util.pagebase import PageBase
from ..page_objects.sales_menu import SalesMenu
from conftest import logger
from config.config import Config
from ..page_objects.dispatch_menu import DispatchMenu
from ..page_objects.driver_menu import DriverMenu


class HomePage(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    sales_menu_lnk = "xpath@@//a[@class='mm_sales']"
    password = "xpath@@//input[@id='inputPassword']"
    login_btn = "xpath@@//button[@type='submit']"
    dispatch_menu_link = "xpath@@//a[@class='mm_dispatch']"
    driver_menu_link = "xpath@@//a[@class='mm_driver']"

    def select_sales_menu(self):

        self.log_obj.write("Selecting the sales menu")
        self.click(self.sales_menu_lnk)
        return SalesMenu(self.get_current_driver())

    def select_dispatch_menu(self):
        self.log_obj.write("Selecting the dispatch menu")
        self.click(self.dispatch_menu_link)
        return DispatchMenu(self.get_current_driver())

    def select_driver_menu(self):
        self.log_obj.write("Selecting the driver menu")
        self.click(self.driver_menu_link)
        return DriverMenu(self.get_current_driver())









