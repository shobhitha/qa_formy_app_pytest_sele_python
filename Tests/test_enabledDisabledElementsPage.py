from selenium.webdriver.common.by import By

from Utilities.readProperties import ReadConfig
from Pages.enabledDisabledElementsPage import EnabledDisabledElements
import time
import pytest
from Locators.locators import Locators


class Test_enabledDisabledElementsPage:

    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'enabled')

    #Test if the disabled element is disabled
    def test_01_disabled_element(self):

        elements_obj = EnabledDisabledElements(self.driver)
        assert elements_obj.disabled_input() is False

    #Test if the enabled element is enabled
    def test_02_enabled_element(self):
        elements_obj = EnabledDisabledElements(self.driver)

        if elements_obj.enabled_input():
            self.driver.find_element(By.ID,elements_obj.input_enabled_id).send_keys(Locators.full_address_text)
            time.sleep(1)



