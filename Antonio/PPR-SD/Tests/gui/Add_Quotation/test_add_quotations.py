from util.testbase import Testbase
import pytest

class Test_AddQuote(Testbase):
    

    @pytest.mark.SMOKE
    def test_add_construction_quotation(self,construction_quote_obj):
        cust_name = construction_quote_obj.get_customer_name_data()
        list_quot_obj = construction_quote_obj.add_construction_quote()
        list_quot_obj.save_quote_number()
        quot = list_quot_obj.get_quote_number()
        list_quot_obj.search_for_quotation(quot)
        add_order_obj =list_quot_obj.select_order_action("generate_order")
        add_order_obj.select_order_status_ordered()# select order as ordered
        add_order_obj.wait_till_order_details_fetched(cust_name) # wait till order details page is fetched by checking customer filed data
        list_order = add_order_obj.submit_order()
        list_order.save_order_number()
        or_num = list_order.get_order_number()
        list_order.search_for_order(or_num)
        email_obj = list_order.select_order_action("email")
        email_obj.send_email()
        assert email_obj.is_email_sent() is True ,"Completed order email was not sent"
        email_obj.close_dlg_box()

     
