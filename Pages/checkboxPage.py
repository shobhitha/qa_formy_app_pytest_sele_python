from selenium.webdriver.common.by import By
from Locators.locators import Locators
class CheckboxPage:

    def __init__(self, driver):
        self.driver = driver
        self.checkbox_one_id = Locators.checkbox_one_id
        self.checkbox_two_id = Locators.checkbox_two_id
        self.checkbox_three_id = Locators.checkbox_three_id

    def checkbox_one_click(self):
        self.driver.find_element(By.ID,self.checkbox_one_id).click()

    def checkbox_two_click(self):
        self.driver.find_element(By.ID, self.checkbox_two_id).click()

    def checkbox_three_click(self):
        self.driver.find_element(By.ID, self.checkbox_three_id).click()

    def checkbox_one_selected(self):
        return self.driver.find_element(By.ID,self.checkbox_one_id).is_selected()

    def checkbox_two_selected(self):
       return self.driver.find_element(By.ID, self.checkbox_two_id).is_selected()

    def checkbox_three_selected(self):
        return self.driver.find_element(By.ID, self.checkbox_three_id).is_selected()







