from util.pagebase import PageBase
from conftest import logger
from ..page_objects.construction_quote_page import ConstructionQuote
from config.config import Config


class SalesMenu(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    quotation_box_modal = "xpath@@//div[@id='specialeventModal']//div[@class='modal-body']"
    add_quotation_btn = "xpath@@//a[@id='sales_add_quote']"
    add_construction_quote = "xpath@@//a[text()='Add Construction Quote']"
    add_special_event_quote = "xpath@@//a[text()='Add Special Event Quote']"

    def select_add_quotation(self):

        self.log_obj.write("Selecting add quotation from the Sales menu")
        self.click(self.add_quotation_btn)


    def open_add_construction_quotation(self):
        self.select_add_quotation()
        self.log_obj.write("Selecting add construction quotation from the add quotations menu")
        self.wait_till_element_is_visible(self.quotation_box_modal)
        self.click(self.add_construction_quote)
        return ConstructionQuote(self.get_current_driver())

    def open_add_special_event_quotation(self):
        self.select_add_quotation()
        self.log_obj.write("Selecting add construction quotation from the add quotations menu")
        self.wait_till_element_is_visible(self.quotation_box_modal)
        self.click(self.add_special_event_quote)
        return ConstructionQuote(self.get_current_driver())







