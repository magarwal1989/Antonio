import pytest
from util.driverclass import driverClass
from lib.page_objects.login_panel import Login_Panel
from config.config import Config



class Testbase(object):


        @pytest.fixture()
        def login_screen(request):
                driver = driverClass.register_driver()
                login_obj = Login_Panel(driver)
                login_obj.open(Config.app_url)
                login_obj.loginDefaultUser()
                yield login_obj
