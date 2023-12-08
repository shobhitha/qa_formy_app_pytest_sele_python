from selenium.webdriver.common.by import By
from Locators.locators import Locators

class AutocompletePage:

    def __init__(self,driver):
        self.driver = driver
        self.input_autocomplete_id = Locators.input_autocomplete_id
        self.dropdown_autocomplete_class = Locators.dropdown_autocomplete_class
        self.input_street_number_id = Locators.input_street_number_id
        self.input_route_id = Locators.input_route_id
        self.input_locality_id = Locators.input_locality_id
        self.input_administrative_area_level_1_id = Locators.input_administrative_area_level_1_id
        self.input_postal_code_id = Locators.input_postal_code_id
        self.input_country_id = Locators.input_country_id
        self.full_address_text = Locators.full_address_text

    def autocomplete_field(self, autocomplete):
        self.driver.find_element(By.ID, self.input_autocomplete_id).send_keys(autocomplete)

    def autocomplete_dropdown_click(self):
        self.driver.find_element(By.CLASS_NAME, self.dropdown_autocomplete_class).click()

    def autocomplete_street_number(self):
        self.driver.find_element(By.ID, self.input_street_number_id)

    def autocomplete_route(self):
        self.driver.find_element(By.ID, self.input_route_id)

    def autocomplete_locality(self):
        self.driver.find_element(By.ID, self.input_locality_id)

    def autocomplete_administrative_area_level(self):
        self.driver.find_element(By.ID, self.input_administrative_area_level_1_id)

    def autocomplete_postal_code(self):
        self.driver.find_element(By.ID, self.input_postal_code_id)

    def autocomplete_country(self):
        self.driver.find_element(By.ID, self.input_country_id)
