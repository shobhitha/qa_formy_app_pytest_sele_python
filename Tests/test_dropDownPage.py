from Utilities.readProperties import ReadConfig
from Pages.dropDownPage import dropDownPage
import time
from selenium.webdriver.common.by import By
import pytest

class Test_dropDownPage:

    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'dropdown')

    # Autocomplete dropdown button click test
    def test_01_autocomplete_dropdown_click(self):

        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.autocomplete_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Autocomplete')]")
        self.driver.back()
        time.sleep(1)

    # Buttons dropdown button click test
    def test_02_buttons_dropdown_click(self):

        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.buttons_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//button[contains(text(), 'Primary')]")
        self.driver.back()
        time.sleep(1)


    # Checkbox dropdown buttons click test
    def test_03_checkbox_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.checkbox_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Checkboxes')]")
        self.driver.back()
        time.sleep(1)

    # DatePicker dropdown buttons click test
    def test_04_datepicker_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.datepicker_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Datepicker')]")
        self.driver.back()
        time.sleep(1)

    # Dragdrop dropdown buttons click test
    def test_05_draganddrop_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.draganddrop_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Drag the image into the box')]")
        self.driver.back()
        time.sleep(1)

    # Dropdown dropdown buttons click test
    def test_06_dropdown_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.dropdown_dropdown_button_click()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Dropdown')]")
        time.sleep(1)

    # Enable Disable elems dropdown buttons click test
    def test_07_enabledisableelems_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.enabledisableelems_dropdown_button_click()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Enabled and Disabled elements')]")
        self.driver.back()
        time.sleep(1)

    # File upload dropdown buttons click test
    def test_08_file_upload_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.fileupload_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'File upload')]")
        self.driver.back()
        time.sleep(1)

    # File download dropdown buttons click test
    def test_09_file_download_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.filedownload_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//p[contains(text(), 'You may have mistyped the address or the page may have moved.')]")
        self.driver.back()
        time.sleep(1)

    # Key mouse press dropdown buttons click test
    def test_10_keymousepress_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.keymousepress_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Keyboard and Mouse Input')]")
        self.driver.back()
        time.sleep(1)

    # Modal dropdown buttons click test
    def test_11_modal_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.modal_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Modal')]")
        self.driver.back()
        time.sleep(1)

    # Page scroll dropdown buttons click test
    def test_12_pagescroll_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.pagescroll_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Large page content')]")
        self.driver.back()
        time.sleep(1)

    # Radio button dropdown buttons click test
    def test_13_radiobutton_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.radiobutton_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Radio buttons')]")
        self.driver.back()
        time.sleep(1)

    # Switch window dropdown buttons click test
    def test_14_switchwindow_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.switchwindow_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Switch Window')]")
        self.driver.back()
        time.sleep(1)

    # Complete web form  dropdown buttons click test
    def test_15_completewebform_dropdown_click(self):
        dropDownButtonObj = dropDownPage(self.driver)
        dropDownButtonObj.dropdown_button_click()
        time.sleep(1)
        dropDownButtonObj.completewebform_dropdown_button_click()
        time.sleep(1)

        assert self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Complete Web Form')]")
        self.driver.back()
        time.sleep(1)







