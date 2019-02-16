from util.pagebase import PageBase
from ..page_objects.sales_menu import SalesMenu
from conftest import logger
from config.config import Config


class HomePage(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    sales_menu_lnk = "xpath@@//a[@class='mm_sales']"
    password = "xpath@@//input[@id='inputPassword']"
    login_btn = "xpath@@//button[@type='submit']"

    def select_sales_menu(self):

        self.log_obj.write("Selecting the sales menu")
        self.click(self.sales_menu_lnk)
        return SalesMenu(self.get_current_driver())










