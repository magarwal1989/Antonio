from util.testbase import Testbase
from conftest import logger
import pytest

class Test_Dispatch(Testbase):
    

    @pytest.mark.SMOKE
    def test_dispatch(self,home_page_obj):
        logger.write("Starting the test","info")
        dispatch_menu_obj =home_page_obj.select_dispatch_menu()
        dcal_obj = dispatch_menu_obj.select_dispatch_calendar()
        d_details_obj = dcal_obj.select_current_date()
        route_Ass_obj = d_details_obj.select_order_action("assign_driver")
        route_Ass_obj.assign_driver("Joe Shelton")
        route_Ass_obj.click_assign_event()
        driver_menu_oj = home_page_obj.select_driver_menu()
        driver_list_page_obj = driver_menu_oj.select_driver_list()
        driver_list_page_obj.search_for_driver("Joe Shelton")






     
