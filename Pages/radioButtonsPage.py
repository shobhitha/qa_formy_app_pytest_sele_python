from selenium.webdriver.common.by import By
from Locators.locators import Locators

class RadioButtonPage():

    def __init__(self,driver):
        self.driver = driver

        self.input_radio_one_xpath = Locators.input_radio_one_xpath
        self.input_radio_two_xpath = Locators.input_radio_two_xpath
        self.input_radio_three_xpath = Locators.input_radio_three_xpath

    def radio_button_one_click(self):
        self.driver.find_element(By.XPATH, self.input_radio_one_xpath).click()

    def radio_button_two_click(self):
        self.driver.find_element(By.XPATH, self.input_radio_two_xpath).click()

    def radio_button_three_click(self):
        self.driver.find_element(By.XPATH, self.input_radio_three_xpath).click()

    def radio_button_one_selected(self):
        return self.driver.find_element(By.XPATH, self.input_radio_one_xpath).is_selected()

    def radio_button_two_selected(self):
        return self.driver.find_element(By.XPATH, self.input_radio_two_xpath).is_selected()

    def radio_button_three_selected(self):
        return self.driver.find_element(By.XPATH, self.input_radio_three_xpath).is_selected()


