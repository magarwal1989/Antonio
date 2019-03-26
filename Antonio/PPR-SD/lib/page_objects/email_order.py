from util.pagebase import PageBase
from conftest import logger

class EmailOrders(PageBase):
    def __init__(self, selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger



    send_email_btn = "xpath@@//button[@id='email_now']"
    confirm_email_dlg = "xpath@@//div[@class='dialog-confirm']"


    def send_email(self):
        #self.sleep_in_seconds(5)
        self.click(self.send_email_btn)

    def is_email_sent(self):
        if self.is_element_present(self.confirm_email_dlg):
            return True
        else:
            return False

    def close_dlg_box(self):
        self.click(self.confirm_email_dlg)
