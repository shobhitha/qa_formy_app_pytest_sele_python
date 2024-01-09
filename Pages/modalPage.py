from selenium.webdriver.common.by import By
from Locators.locators import Locators

class ModalPage:

    def __init__(self,driver):
        self.driver = driver

        self.button_modal_id = Locators.button_modal_id
        self.div_modal_id = Locators.div_modal_id
        self.close_button_id = Locators.close_button_id

    def modal_button_click(self):
        self.driver.find_element(By.ID,self.button_modal_id).click()

    def modal_close_click(self):
        self.driver.find_element(By.ID,self.close_button_id )