import pytest
from Page_Objects.Main_Page import Main_Page
from Test_Data.TestData import TestData
from datetime import datetime

class TestUser():
 
    @pytest.fixture(scope="function",  autouse=True)
    def startPage(self,driver):
        self.page = Main_Page(driver)
        driver.get(TestData.URL['url_login'])
        return driver
    
    @pytest.mark.user
    def test_search_user_pass(self):
        result_list = self.page.get_user_search_result(TestData.NAME['usr2'])
        pass
        