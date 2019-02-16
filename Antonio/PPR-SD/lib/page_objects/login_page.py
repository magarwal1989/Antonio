from util.pagebase import PageBase
from conftest import logger
from config.config import Config
from ..page_objects.home_page import HomePage


class LoginPage(PageBase):

    def __init__(self,selenium_driver):
        PageBase.__init__(self, selenium_driver)
        self.log_obj = logger


    username = "xpath@@//input[@id='inputEmail']"
    password = "xpath@@//input[@id='inputPassword']"
    login_btn = "xpath@@//button[@type='submit']"
    

    def login_default_user(self, defaultUsername=Config.app_username, defaultPassword=Config.app_password):

        self.log_obj.write("Logging in to the application with deafult user and default passowrd")
        self.set_field(self.username, defaultUsername)
        self.set_field(self.password, defaultPassword)
        self.click(self.login_btn)
        return HomePage(self.get_current_driver())

    def is_user_logged_in(self):
        self.log_obj.write("Verifying if the user is logged in")
        if"PPR-SD" in self.get_current_title():
            self.log_obj.write("Succesfully verified the Home page title as PPR-SD")
            return True
        else:
            self.log_obj.write("PPR-SD not found in the page title.","error")
            return False








