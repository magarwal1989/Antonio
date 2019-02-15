class Login_Panel(pagebase):

    def __init__(self,selenium_driver):
        pasgease.__init__(self, selenium_driver)
        self.log_obj = test_log_obj


    username = "xpath@@//*[@class='loginForm auth-action-login']//*[@name='username']//input"
    password = "xpath@@//*[@class='loginForm auth-action-login']//*[@name='password']//input"
    login_btn = "xpath@@//span[text()='Login']"
    

    def loginDefaultUser(self, defaultUsername=Constants.USERNAME,defaultPassword=Constants.PASSWORD):
        try:
            if(self.isUserLoggedIn()):
                self.log_obj.write("No action performed , user is already logged in ")
                return(Console_Panel(self.driver))
            else:
                self.set_field(self.username, defaultUsername)
                self.set_field(self.password, defaultPassword)
                self.move_and_click(self.login_btn)
            self.log_obj.write("Credential entered and login button clicked ")
        except Exception as e:
            self.log_obj.write("Could not login due to error {}".format(str(e)),"error")
            raise Exception("Could Not login to opspace because of error ----> {}".format(str(e)))
        return(Console_Panel(self.driver))







