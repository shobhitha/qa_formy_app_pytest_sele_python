from selenium.webdriver.common.by import By
from Locators.locators import Locators


class PageScroll:
    def __init__(self,driver):

        self.driver = driver

        self.input_scroll_name_id = Locators.input_scroll_name_id
        self.input_scroll_date_id = Locators.input_scroll_date_id

    def scroll_name_ele(self):
        return self.driver.find_element(By.ID, Locators.input_scroll_name_id)

    def scroll_name_input(self, name):
        self.driver.find_element(By.ID,self.input_scroll_name_id).send_keys(name)

    def scroll_date_input(self, date):
        self.driver.find_element(By.ID, self.input_scroll_date_id).send_keys(date)
