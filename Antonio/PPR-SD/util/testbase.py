import pytest
from util.driverclass import driverClass
from lib.page_objects.login_page import LoginPage
from config.config import Config

driver = None

class Testbase(object):




        @pytest.fixture()
        def login_screen_obj(request):
                global driver
                driver = driverClass.register_driver()
                login_obj = LoginPage(driver)
                login_obj.open(Config.app_url)
                yield login_obj

        @pytest.fixture()
        def home_page_obj(request,login_screen_obj):
                home_page_obj=login_screen_obj.login_default_user()
                yield home_page_obj

        @pytest.fixture()
        def construction_quote_obj(requests,home_page_obj):
                sales_menu_obj = home_page_obj.select_sales_menu()
                construct_quote_page = sales_menu_obj.open_add_construction_quotation()
                yield construct_quote_page

        @pytest.fixture()
        def special_event_quote_obj(requests, home_page_obj):
                sales_menu_obj = home_page_obj.select_sales_menu()
                construct_quote_page = sales_menu_obj.open_add_special_event_quotation()
                yield construct_quote_page

        @pytest.fixture
        def get_order_num_after_add_construction_quotation(self, construction_quote_obj):
                cust_name = construction_quote_obj.get_customer_name_data()
                list_quot_obj = construction_quote_obj.add_construction_quote()
                list_quot_obj.save_quote_number()
                quot = list_quot_obj.get_quote_number()
                list_quot_obj.search_for_quotation(quot)
                add_order_obj = list_quot_obj.select_order_action("generate_order")
                add_order_obj.select_order_status_ordered()  # select order as ordered
                add_order_obj.wait_till_order_details_fetched(cust_name)
                list_order = add_order_obj.submit_order()
                list_order.save_order_number()
                or_num = list_order.get_order_number()
                yield or_num,list_quot_obj


