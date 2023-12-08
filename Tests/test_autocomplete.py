import time
import pytest
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Pages.autocompletePage import AutocompletePage
from Locators.locators import Locators

#autouse=True fixtures are run before each test_* method runs automatically. test_* doesn't have to request for fixtures explicitly
@pytest.mark.usefixtures("setup")
class Test_Autocomplete:
    baseURL = ReadConfig.getApplicationURL()

    def test_01_autocomplete_dropdown_address(self):
        print(self.driver)

        self.driver.get(self.baseURL + 'autocomplete')
        autocomplete = AutocompletePage(self.driver)
        autocomplete.autocomplete_field(autocomplete.full_address_text)
        time.sleep(2)
        autocomplete.autocomplete_dropdown_click()
        time.sleep(1)


    # Verifying if the form field were autocompleted
    def test_02_autocompleted_fields(self):

        self.driver.get(self.baseURL + 'autocomplete')
        autocompleted_fields = AutocompletePage(self.driver)

        fields_list = [
            self.driver.find_element(By.ID, autocompleted_fields.input_autocomplete_id).get_attribute("value"),
            self.driver.find_element(By.ID, autocompleted_fields.input_street_number_id).get_attribute("value"),
            self.driver.find_element(By.ID, autocompleted_fields.input_route_id).get_attribute("value"),
            self.driver.find_element(By.ID, autocompleted_fields.input_postal_code_id).get_attribute("value"),
            self.driver.find_element(By.ID, autocompleted_fields.input_locality_id).get_attribute("value"),
            self.driver.find_element(By.ID, autocompleted_fields.input_administrative_area_level_1_id).get_attribute("value"),
            self.driver.find_element(By.ID, autocompleted_fields.input_country_id).get_attribute("value")
        ]

        for input_field in fields_list:
            assert len(input_field) > 0