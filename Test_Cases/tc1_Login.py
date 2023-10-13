import pytest
from Page_Objects.Login_Page import LoginPage
from Test_Data.TestData import TestData

class TestLogin():
 
    @pytest.fixture(scope="function",  autouse=True)
    def startPage(self,driver):
        self.page = LoginPage(driver)
        driver.get(TestData.URL['url_login'])
        return driver
    
    def test_login_pass(self):
        self.page._login(TestData.USERNAME['urs_login1'][0],TestData.USERNAME['urs_login1'][1])
        result = self.page._login_result()
        assert result == True
        
    def test_login_false(self,driver):
        self.page._logout()
        driver.refresh()
        self.page._login(TestData.USERNAME['urs_login2'][0],TestData.USERNAME['urs_login2'][1])
        result = self.page._login_result()
        assert result == False
 
if __name__ == "__main__":
    pytest.main(["-s", "tc1_Login.py"])
