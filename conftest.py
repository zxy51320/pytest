import pytest
from selenium import webdriver
 
@pytest.fixture(scope='session')
def driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    #先调用login函数登录
    def end():
        driver.quit()
    request.addfinalizer(end)#终结函数
    return driver
