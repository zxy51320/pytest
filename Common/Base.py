from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def getElement_list(self, *loc):
        __element_list = self.driver.find_elements(*loc)
        return __element_list

    def input_text(self, *loc, text):
        __element = self.wait.until(EC.element_to_be_clickable(*loc))
        __element.send_keys(text)

    def scroll_to(self, *loc):
        __element = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", __element)
        time.sleep(1)

    def click(self, *loc):
        __element = self.wait.until(EC.element_to_be_clickable(*loc))
        __element.click()

    def get_text(self, *loc):
        __text = self.wait.until(EC.presence_of_element_located(*loc)).text
        return __text
    
    def check_url(self,content):
        try:
            self.wait.until(EC.url_contains(content))
            return True
        except TimeoutException:
            return False

    def switch_handle(self,window_name):
        self.driver.switch_to.window(window_name)

    def get_title(self):
        return self.driver.title
