from Common.Base import BasePage
from selenium.webdriver.common.by import By
import time
 
class Main_Page(BasePage):
    
    __profile_menu = (By.XPATH, "//ion-label[text()='Profile']")
    __groups_menu = (By.XPATH, "//ion-label[text()='Groups']")
    __users_menu = (By.XPATH, "//ion-label[text()='Users']")
    __settings_menu = (By.XPATH, "//ion-label[text()='Settings']")

    __new_group_btn = (By.XPATH, "//ion-button[@class='md button button-small button-outline ion-activatable ion-focusable hydrated']")
    __new_group_name_input = (By.XPATH, "//ion-input[@formcontrolname='name']//input")
    __new_group_descp_input = (By.XPATH, "//ion-textarea[@formcontrolname='description']//textarea")
    __new_group_tagline_input = (By.XPATH, "//ion-input[@formcontrolname='tagline']//input")
    __new_group_submit = (By.XPATH, "//ion-button[@type='submit']")
    __main_search_input = (By.XPATH, "//input[@aria-label='search text']")
    __main_search_result_list = (By.XPATH, "//ion-card//ion-list[@class='md list-md hydrated' and @role='list']")
    
    
    def __init__(self,driver):
        super().__init__(driver)
    
    def creat_group(self, _name, _descp, _tagline):
        self.click(self.__new_group_btn)
        self.input_text(self.__new_group_name_input, text=_name)
        self.input_text(self.__new_group_descp_input, text=_descp)
        self.input_text(self.__new_group_tagline_input, text=_tagline)
        self.click(self.__new_group_submit)
        
    def get_group_search_result(self, _name):
        self.click(self.__groups_menu)
        self.input_text(self.__main_search_input, text=_name)
        time.sleep(3)
        result_list = self.getElement_list(*self.__main_search_result_list)
        return result_list
    
    def verify_group_search_result(self, _result_list, _name, _tagline, _descp):
        if f'{_name}' in f'{_result_list[0].text}' and f'{_tagline}' in f'{_result_list[0].text}':
            self.click(_result_list[0])
            __group_descp = (By.XPATH, f"//div[@data-replicated-value='{_descp}']")
            if self.ifElementExist(*__group_descp):
                return True
            else:
                return False
        else:
            return False

    def get_user_search_result(self, _name):
        self.click(self.__users_menu)
        self.input_text(self.__main_search_input, text=_name)
        time.sleep(3)
        result_list = self.getElement_list(*self.__main_search_result_list)
        return result_list
    
    def verify_user_search_result(self, _result_list, _name):
        if f'{_name}' in f'{_result_list[0].text}':
            return True
        else:
            return False
        

