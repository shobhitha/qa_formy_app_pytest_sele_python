from selenium.webdriver.common.by import By

from Utilities.readProperties import ReadConfig
from Pages.modalPage import ModalPage
import time
import pytest


class Test_modalPage:
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'modal')

    #Test of the Modal window gets poped up on lcicking the button and close it
    def test_01_modal_title(self):
        modal_obj = ModalPage(self.driver)
        modal_obj.modal_button_click()
        time.sleep(1)
        assert self.driver.find_element(By.ID, 'exampleModalLabel')
        modal_obj.modal_close_click()