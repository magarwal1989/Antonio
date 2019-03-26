from util.testbase import Testbase
from conftest import logger
import pytest

class Test_Dispatch(Testbase):
    

    @pytest.mark.SMOKE
    def test_dispatch(self,get_order_num_after_add_construction_quotation):
        or_no,list_quote_obj = get_order_num_after_add_construction_quotation
        home_page_obj = list_quote_obj.return_home_page_obj()
        logger.write("Starting the test","info")
        dispatch_menu_obj =home_page_obj.select_dispatch_menu()
        dcal_obj = dispatch_menu_obj.select_dispatch_calendar()
        d_details_obj = dcal_obj.select_current_date()
        d_details_obj.search_for_order(or_no)
        route_Ass_obj = d_details_obj.select_order_action("assign_driver")
        route_Ass_obj.assign_driver("Joe Shelton")
        route_Ass_obj.click_assign_event()
        driver_menu_oj = home_page_obj.select_driver_menu()
        driver_list_page_obj = driver_menu_oj.select_driver_list()
        driver_list_page_obj.search_for_driver("Joe Shelton")






     
