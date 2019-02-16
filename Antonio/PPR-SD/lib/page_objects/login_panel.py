from util.pagebase import PageBase
from conftest import logger
from config.config import Config

class Login_Panel(PageBase):

    def __init__(self,selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger


    username = "xpath@@//input[@id='inputEmail']"
    password = "xpath@@//input[@id='inputPassword']"
    login_btn = "xpath@@//button[@type='submit']"
    

    def loginDefaultUser(self, defaultUsername=Config.app_username,defaultPassword=Config.app_username):

        self.set_field(self.username, defaultUsername)
        self.set_field(self.password, defaultPassword)
        self.click(self.login_btn)








