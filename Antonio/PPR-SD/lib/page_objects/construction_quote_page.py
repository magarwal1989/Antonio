from util.json_parser import parse_json_from_file
from conftest import get_test_data_directory
from util.pagebase import PageBase
from conftest import logger
from util.utils import get_current_date
from util.utils import get_next_week_date
from config.config import Config
from ..page_objects.list_quotation import ListQuotation
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
    delivery_city_input = "xpath@@//*[@id='job_city_chosen']//div/input"
    delivery_zip = "id@@job_zip"

    quantity_1="xpath@@//input[@id='quantity-1']"
    quantity_2 = "id@quantity_2"
    quantity_3 = "id@quantity_3"

    product_1="xpath@@//input[@id='product-1']"
    product_2 = "id@product_2"
    product_3 = "id@product_3"

    delivery_start_date = "xpath@@//input[@id='job_start_date']"
    delivery_end_date = "xpath@@//input[@id='job_end_date']"
    submit_btn = "xpath@@//input[@name='submit']"


    def add_construction_quote(self):
        created_by = data["quote"]["created_by"]
        self.enter_value_and_select_from_dropdown(self.created_by_xpath,self.created_by_input,created_by)

        sales_rep = data["quote"]["sale_rep"]
        self.enter_value_and_select_from_dropdown(self.seles_rep_xpath, self.sales_rep_input, sales_rep)

        quote_status = data["quote"]["status"]
        self.enter_value_and_select_from_dropdown(self.quote_status_xpath, self.quote_status_input, quote_status)

        #self.sleep_in_seconds(5)
        customer = data["quote"]["customer"]
        self.enter_value_and_select_from_dropdown(self.customer_xpath, self.customer_input, customer)


        delivery_start_date = get_current_date()
        self.set_field(self.delivery_start_date, delivery_start_date)
        self.hit_enter(self.delivery_start_date)

        delivery_end_date = get_next_week_date()
        self.set_field(self.delivery_end_date, delivery_end_date)
        self.hit_enter(self.delivery_end_date)

        delivery_zip = data["quote"]["delivery_zip"]
        self.set_field(self.delivery_zip, delivery_zip)

        delivery_add = data["quote"]["delivery_address"]
        self.set_field(self.delivery_address,delivery_add)

        delivery_city = data["quote"]["delivery_city"]
        self.enter_value_and_select_from_dropdown(self.delivery_city_xpath, self.delivery_city_input, delivery_city)

        equip_serv_1_quant = data["quote"]["equipment_services"][0]["Quantity"]
        equip_serv_1_prod = data["quote"]["equipment_services"][0]["product"]
        self.set_field(self.quantity_1,equip_serv_1_quant)
        self.set_field(self.product_1, equip_serv_1_prod)
        self.sleep_in_seconds(2)
        self.click("xpath@@//ul//li//div[text()='STANDARD RESTROOM']")
        self.sleep_in_seconds(2)
        self.click(self.submit_btn)
        return ListQuotation(self.get_current_driver())













