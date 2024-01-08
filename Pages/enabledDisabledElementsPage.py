from Locators.locators import Locators
from selenium.webdriver.common.by import By


class EnabledDisabledElements:

    def __init__(self, driver):
        self.driver = driver
        self.input_disabled_id = Locators.input_disabled_id
        self.input_enabled_id = Locators.input_enabled_id

    def disabled_input(self):
        return self.driver.find_element(By.ID,self.input_disabled_id ).is_enabled()

    def enabled_input(self):
        return self.driver.find_element(By.ID, self.input_enabled_id).is_enabled()

