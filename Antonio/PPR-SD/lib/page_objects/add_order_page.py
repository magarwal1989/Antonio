from util.pagebase import PageBase
from ..page_objects.list_orders import ListOrders
from conftest import logger


class AddOrders(PageBase):

    def __init__(self,selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger


    username = "xpath@@//input[@id='inputEmail']"
    password = "xpath@@//input[@id='inputPassword']"
    ordered = "xpath@@//ul/li[text()='Ordered']"
    select_status = "xpath@@//div[@id='status_chosen']"
    subm_order = "xpath@@//input[@id='floatingBtn']"
    customer_xpath = "xpath@@//label[@for='customer']/..//div[@id='customer_chosen']"
    customer_input = "xpath@@//label[@for='customer']/following-sibling::*//input"
    delivery_city_xpath = "xpath@@//*[@id='job_city_chosen']"
    delivery_city_input = "xpath@@//*[@id='job_city_chosen']//div/input"
    

    def select_order_status_ordered(self):
        self.click(self.select_status)
        #self.sleep_in_seconds(2)
        self.click(self.ordered)
        #self.sleep_in_seconds(10)

    def wait_till_order_details_fetched(self,order_data):
        self.wait_till_text_present_in_input_field(self.customer_xpath,order_data)


    def submit_order(self):

        from ..page_objects.construction_quote_page import data
        #self.sleep_in_seconds(5)
      #  customer = data["quote"]["customer"]
       # self.enter_value_and_select_from_dropdown(self.customer_xpath,self.customer_input,customer) #select customer
        #delivery_city = data["quote"]["delivery_city"]
        #self.enter_value_and_select_from_dropdown(self.delivery_city_xpath, self.delivery_city_input, delivery_city) #select delivery city
        self.click(self.subm_order)
        return ListOrders(self.get_current_driver())



