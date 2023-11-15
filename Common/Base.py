from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def getElement_list(self, *loc):
        __element_list = self.driver.find_elements(*loc)
        return __element_list
    
    def ifElementExist(self, *loc):
        try:
            self.driver.find_element(*loc)
            return True
        except NoSuchElementException:
            return False

    def input_text(self, *loc, text):
        __element = self.scroll_to_element(*loc)
        __element.send_keys(text)

    def scroll_to_element(self, *loc):
        __element = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", __element)
        time.sleep(1)
        return __element

    def click(self, *loc):
        __element = self.scroll_to_element(*loc)
        __element.click()

    def get_text(self, *loc):
        __text = self.wait.until(EC.presence_of_element_located(*loc)).text
        return __text
    
    def check_url(self, content:str):
        try:
            self.wait.until(EC.url_contains(content))
            return True
        except TimeoutException:
            return False

    def create_new(self, param:str):
        """
        Parameters:
            param (str): 操作类型，可以是 'tab' 或 'window'。
        """
        self.driver.switch_to.new_window(f'{param}')
    
    def get_all_windows(self):
        __all_windows = self.driver.window_handles
        return __all_windows
    
    def get_current_window(self):
        __current_window = self.driver.current_window_handle
        return __current_window
    
    def switch_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def alert_handle(self, action:str):
        """
        处理 JavaScript 弹窗(alert)。

        Parameters:
            action (str): 操作类型，可以是 'accept' 或 'dismiss'。
        """
        __alert = self.driver.switch_to.alert
        if action == 'accept':
            __alert.accept()
        elif action == 'dismiss':
            __alert.dismiss()
        else:
            pass

    def get_title(self):
        return self.driver.title
    
    def select_option(self, *loc, method:str, value: str|int)->str:
        """
        选择下拉框或列表项。

        Parameters:
            method (str): 匹配类型，可以是 'text', 'value' 或 'index'。
        """
        __element = self.wait.until(EC.element_to_be_clickable(*loc))
        __option_list = self.Select(__element)
        match method:
            case 'text':
                __option_list.select_by_visible_text(f'{value}')
            case 'value':
                __option_list.select_by_value(value)
            case 'index':
                __option_list.select_by_index(value)
            case _:
                pass
        
    def doubleClick(self, *loc):
        __element = self.wait.until(EC.element_to_be_clickable(*loc))
        __action = ActionChains(self.driver)
        __action.double_click(__element).perform()
        
    def mouse_pointing(self, *loc):
        __element = self.scroll_to_element(*loc)
        __action = ActionChains(self.driver)
        __action.move_to_element(__element).perform()
        
    def right_click(self, *loc):
        __element = self.wait.until(EC.element_to_be_clickable(*loc))
        __action = ActionChains(self.driver)
        __action.context_click(__element).perform()
    
    def drag_and_drop(self, *loc):
        __element1 = self.wait.until(EC.element_to_be_clickable(*loc[0]))
        __element2 = self.wait.until(EC.element_to_be_clickable(*loc[1]))
        __action = ActionChains(self.driver)
        __action.drag_and_drop(__element1,__element2).perform()
