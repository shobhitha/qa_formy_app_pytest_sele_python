
from Locators.locators import Locators
from selenium.webdriver.common.by import By

class DatePickerPage:

    def __init__(self,driver):
        self.driver = driver

        self.input_datepicker_id = Locators.input_datepicker_id
        self.datepicker_other_date_xpath = Locators.datepicker_other_date_xpath
        self.datepicker_today_xpath = Locators.datepicker_today_xpath

    def datepicker_input(self, send_date):
        dp = self.driver.find_element(By.ID, self.input_datepicker_id)
        dp.clear()
        dp.click()
        dp.send_keys(send_date)


    def datepicker_today_date(self):
        self.driver.find_element(By.XPATH, self.datepicker_today_xpath).click()

    def datepicker_other_date(self):
       self.driver.find_element(By.XPATH, self.datepicker_other_date_xpath).click()

