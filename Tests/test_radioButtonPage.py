from Utilities.readProperties import ReadConfig
from Pages.radioButtonsPage import RadioButtonPage
import pytest


class Test_pageScrollPage:
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'radiobutton')

    def test_01_radio_button_one(self):
        radiobutton_obj = RadioButtonPage(self.driver)
        radiobutton_obj.radio_button_one_click()

        assert radiobutton_obj.radio_button_one_selected()
        assert not radiobutton_obj.radio_button_two_selected()
        assert not radiobutton_obj.radio_button_three_selected()

    def test_02_radio_button_one(self):
        radiobutton_obj = RadioButtonPage(self.driver)
        radiobutton_obj.radio_button_two_click()

        assert not radiobutton_obj.radio_button_one_selected()
        assert radiobutton_obj.radio_button_two_selected()
        assert not radiobutton_obj.radio_button_three_selected()

    def test_03_radio_button_one(self):
        radiobutton_obj = RadioButtonPage(self.driver)
        radiobutton_obj.radio_button_three_click()

        assert not radiobutton_obj.radio_button_one_selected()
        assert not radiobutton_obj.radio_button_two_selected()
        assert radiobutton_obj.radio_button_three_selected()

