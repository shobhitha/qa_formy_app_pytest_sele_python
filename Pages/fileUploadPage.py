from selenium.webdriver.common.by import By
from Locators.locators import Locators
class FileUploadPage:

    def __init__(self,driver):
        self.driver = driver

        self.input_file_upload_field_id = Locators.input_file_upload_field_id
        self.button_upload_choose_xpath = Locators.button_upload_choose_xpath
        self.button_upload_reset_xpath = Locators. button_upload_reset_xpath


    def file_upload_input(self):
        self.driver.find_element(By.ID, self.input_file_upload_field_id)

    def file_upload_input_send_keys(self, test_file):
        self.driver.find_element(By.ID, self.input_file_upload_field_id).send_keys(test_file)

    def file_upload_choose_buttn_click(self):
        self.driver.find_element(By.XPATH, self.button_upload_choose_xpath).click()

    def file_upload_reset_buttn_click(self):
        self.driver.find_element(By.XPATH, self.button_upload_reset_xpath).click()


