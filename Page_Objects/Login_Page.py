from Common.Base import BasePage
from selenium.webdriver.common.by import By
import time
 
class LoginPage(BasePage):

    username_input = (By.NAME,'ion-input-0')
    pwd_input = (By.NAME,'ion-input-1')
    login_btn = (By.XPATH,"//ion-button[@type='submit']")
    main_page = 'user-profile'
    user_icon = (By.XPATH,"//ion-avatar[@class='padded-avatar md hydrated']")
    logout = (By.XPATH,"//ion-label[@class='sc-ion-label-md-h sc-ion-label-md-s md hydrated' and text()='Logout']")

    def __init__(self,driver):
        super().__init__(driver)
        
    def _login(self, usr, pwd):
        self.input_text(*self.username_input, text=usr)
        self.input_text(*self.pwd_input, text=pwd)
        self.click(*self.login_btn)

    def _login_result(self):
        __result = self.check_url(self.main_page)
        return __result
        
    def _logout(self):
        self.click(*self.user_icon)
        self.click(*self.logout)
        time.sleep(1)