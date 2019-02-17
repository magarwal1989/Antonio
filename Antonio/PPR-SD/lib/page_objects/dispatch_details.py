from util.pagebase import PageBase
from ..page_objects.route_assignment import RouteAssignment
from conftest import logger



class DispatchDetails(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger

    current_date = "xpath@@//td[contains(@class,'fc-widget')][contains(@class,'today')]"
    latest_order_action_btn = "xpath@@//table[@id='fileData']/tbody/tr[1]/td//button[text()='Actions ']"
    assign_driver_btn = "xpath@@//a[text()='  Assign Route/Driver']"

    def select_actions_menu_on_latest_order(self):
        self.click(self.latest_order_action_btn)

    def select_order_action(self, action_type):
        self.select_actions_menu_on_latest_order()
        if "driver" in action_type:
            self.click(self.assign_driver_btn)
            return RouteAssignment(self.get_current_driver())








