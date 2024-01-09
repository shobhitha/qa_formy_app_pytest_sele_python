from selenium.webdriver.common.by import By

from Utilities.readProperties import ReadConfig
from Pages.switchWindowsPage import SwitchWindowPage
import pytest

class Test_pageScrollPage:
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'switch-window')


    def test_01_open_new_tab(self):

        switchWindow_obj = SwitchWindowPage(self.driver)
        switchWindow_obj.open_tab_buttn_click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.get(self.baseURL)
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome to Formy')]")
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_02_open_new_alert(self):
        switchWindow_obj = SwitchWindowPage(self.driver)
        switchWindow_obj.open_alert_buttn_click()
        self.driver.switch_to.alert.accept()



