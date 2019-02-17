from util.pagebase import PageBase
from conftest import logger
from ..page_objects.add_order_page import AddOrders

quote_number = 0

class ListQuotation(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger



    latest_quote_number = "xpath@@//table[@id='fileData']/tbody/tr[1]/td[2]"
    search_quotation = "xpath@@//input[@type='search']"
    actions_button = "xpath@@//button[text()='Actions ']"
    generate_order = "xpath@@//a[text()=' Generate Order']"

    def save_quote_number(self):
        global quote_number
        self.wait_till_element_is_visible(self.latest_quote_number)
        quote_number = self.get_text(self.latest_quote_number)

    def get_quote_number(self):
        return quote_number

    def search_for_quotation(self,quote_num):
        self.set_field(self.search_quotation,quote_number)
        self.hit_enter(self.search_quotation)

    def select_order_action(self,action_type):
        self.click(self.actions_button)
        if "generate" in action_type:
            self.click(self.generate_order)
            return AddOrders(self.get_current_driver())









