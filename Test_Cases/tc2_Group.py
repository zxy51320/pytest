import pytest
from Page_Objects.Main_Page import Main_Page
from Test_Data.TestData import TestData
from datetime import datetime

class TestGroup():
 
    @pytest.fixture(scope="function",  autouse=True)
    def startPage(self,driver):
        self.page = Main_Page(driver)
        driver.get(TestData.URL['url_login'])
        return driver
    
    @pytest.mark.group
    def test_creat_group_pass(self):
        name = 'groupname' + f'{str(datetime.now())[-6:]}'
        descp = 'description' + f'{str(datetime.now())[-6:]}'
        tagline = 'tagline' + f'{str(datetime.now())[-6:]}'
        self.page.creat_group(name,descp,tagline)
        result_list = self.page.get_group_search_result(name)
        result = self.page.verify_group_search_result(result_list,name,tagline)
        assert result == True
        