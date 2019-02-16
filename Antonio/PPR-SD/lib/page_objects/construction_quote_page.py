from util.json_parser import parse_json_from_file
from conftest import get_test_data_directory
from util.pagebase import PageBase
from conftest import logger
from config.config import Config
import os

file_path = os.path.join(get_test_data_directory(),"construction_quote.json")
data = parse_json_from_file(file_path)

class ConstructionQuote(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    created_by_xpath = "xpath@@//label[@for='entered_by']/..//div[@id='user_chosen']"
    created_by_input = "xpath@@//label[@for='entered_by']/following-sibling::*//input"
    seles_rep_xpath = "xpath@@//label[@for='sales_rep']/..//div[@id='user_chosen']"
    sales_rep_input = "xpath@@//label[@for='sales_rep']/following-sibling::*//input"
    quote_status_xpath = "xpath@@//label[@for='status']/..//div[@id='status_chosen']"
    quote_status_input = "xpath@@//label[@for='status']/following-sibling::*//input"
    customer_xpath = "xpath@@//label[@for='customer']/..//div[@id='customer_chosen']"
    customer_input = "xpath@@//label[@for='customer']/following-sibling::*//input"

    delivery_address = "id@@job_address"
    delivery_city_xpath = "xpath@@//*[@id='job_city_chosen']"
    delivery_city_input = "xpath@@//*[@id='job_city_chosen']/following-sibling::*//input"
    delivery_zip = "id@@job_zip"

    quantity_1="id@quantity_1"
    quantity_2 = "id@quantity_2"
    quantity_3 = "id@quantity_3"

    product_1="id@product_1"
    product_2 = "id@product_2"
    product_3 = "id@product_3"


    def enter_value_and_select_from_dropdown(self,dropdown_locator,dropdown_input_box_locator,value):
        self.click(dropdown_locator)
        self.set_field(dropdown_input_box_locator, value)
        self.hit_enter(dropdown_input_box_locator)

    def add_construction_quote(self):
        created_by = data["quote"]["created_by"]
        self.enter_value_and_select_from_dropdown(self.created_by_xpath,self.created_by_input,created_by)

        sales_rep = data["quote"]["sale_rep"]
        self.enter_value_and_select_from_dropdown(self.seles_rep_xpath, self.sales_rep_input, sales_rep)

        quote_status = data["quote"]["status"]
        self.enter_value_and_select_from_dropdown(self.quote_status_xpath, self.quote_status_input, quote_status)

        customer = data["quote"]["customer"]
        self.enter_value_and_select_from_dropdown(self.customer_xpath, self.customer_input, customer)

        delivery_add = data["quote"]["delivery_address"]
        self.set_field(self.delivery_address,delivery_add)

        delivery_city = data["quote"]["delivery_city"]
        self.enter_value_and_select_from_dropdown(self.delivery_city_xpath, self.delivery_city_input, delivery_city)

        equip_serv_1_quant = data["quote"]["equipment_services"][0]["Quantity"]
        equip_serv_1_prod = data["quote"]["equipment_services"][0]["product"]
        self.set_field(self.quantity_1,equip_serv_1_quant)
        self.set_field(self.product_1, equip_serv_1_prod)












