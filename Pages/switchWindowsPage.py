from selenium.webdriver.common.by import By
from Locators.locators import Locators

class SwitchWindowPage():

    def __init__(self,driver):
        self.driver = driver
        self.button_switchWindow_newTab_id = Locators.button_switchWindow_newTab_id
        self.button_switchWindow_alert_id = Locators.button_switchWindow_alert_id

    def open_tab_buttn_click(self):
        self.driver.find_element(By.ID,self.button_switchWindow_newTab_id).click()


    def open_alert_buttn_click(self):
        self.driver.find_element(By.ID,self.button_switchWindow_alert_id).click()