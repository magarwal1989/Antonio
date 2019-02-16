import pytest
from util.driverclass import driverClass
from lib.page_objects.login_page import LoginPage
from config.config import Config



class Testbase(object):


        @pytest.fixture()
        def login_screen_obj(request):
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