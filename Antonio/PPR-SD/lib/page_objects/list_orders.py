from util.pagebase import PageBase
from conftest import logger
from ..page_objects.email_order import EmailOrders


order_number = 0

class ListOrders(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger



    latest_order_number = "xpath@@//table[@id='fileData']/tbody/tr[1]/td[2]"
    search_order = "xpath@@//input[@type='search']"
    actions_button = "xpath@@//button[text()='Actions ']"
    email_order = "xpath@@//a[text()=' Email Order to Customer']"

    def save_order_number(self):
        global order_number
        self.wait_till_element_is_visible(self.latest_order_number)
        order_number = self.get_text(self.latest_order_number)

    def get_order_number(self):
        return order_number

    def search_for_order(self,order_number):
        self.set_field(self.search_order,order_number)
        self.hit_enter(self.search_order)

    def select_order_action(self,action_type):
        self.click(self.actions_button)
        if "email" in action_type:
            self.click(self.email_order)
            return EmailOrders(self.get_current_driver())









