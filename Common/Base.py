from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)


    def input_text(self, *loc, text):
        element = self.wait.until(EC.element_to_be_clickable(*loc))
        element.send_keys(text)

    def scroll_to(self, *loc):
        element = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def click(self, *loc):
        element = self.wait.until(EC.element_to_be_clickable(*loc))
        element.click()

    def get_text(self, *loc):
        text = self.wait.until(EC.presence_of_element_located(*loc)).text
        return text
    
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
