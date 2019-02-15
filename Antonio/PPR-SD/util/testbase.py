import pytest



class Testbase():

        """
    @pytest.fixture()
    def login_app(request):
        driver_panel_1 = driverClass.register_driver()
        HM_obj = HM_LOGIN_PANEL(driver_panel_1)
        HM_obj.open_health_monitor(Constants.HEALTH_MONITOR_URL)
        yield HM_obj
        HM_obj.logout()

    ## TEAR DOWN FIXTURE####
    @pytest.fixture(autouse=Constants.TEARDOWN_USE, scope=Constants.TEARDOWN_SCOPE)
    def my_fixture(self):
        yield
        if (Constants.TEARDOWN_USE == "True"):
            pagebase.quitAll()
        test_log_obj.write("Teardown executed with scope = "+Constants.TEARDOWN_SCOPE)

  