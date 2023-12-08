import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


#scope="class" - If we need to perform an action before and after of an class of a module we use class scope (scope=“class”)
#autouse=True https://docs.pytest.org/en/6.2.x/fixture.html
#request.cls.driver = driver => https://stackoverflow.com/questions/56856233/what-role-does-request-cls-driver-have-in-pytest-fixture-with-a-scope-of-class
#request parameter -> https://stackoverflow.com/questions/56856233/what-role-does-request-cls-driver-have-in-pytest-fixture-with-a-scope-of-class
@pytest.fixture(scope= "class", autouse=True)
def setup(request):

    print("initiating chrome driver")

    driver = webdriver.Chrome()
    WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    #driver.close()
    #driver.quit()
