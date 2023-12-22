import pytest
from Pages.buttonsPage import ButtonsPage
from Utilities.readProperties import ReadConfig
import time
#autouse=True fixtures are run before each test_* method runs automatically. test_* doesn't have to request for fixtures explicitly
#@pytest.mark.usefixtures("setup") -> setup is made autouse=True
class Test_ButtonPage:
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'buttons')

    #Testing first row buttons
    def test_01_first_row_buttons(self):

        #self.driver.get(self.baseURL + 'buttons')
        button_first_row = ButtonsPage(self.driver)
        button_first_row.first_row_button_primary()
        assert button_first_row.first_row_button_primary_enabled()
        button_first_row.first_row_button_success()
        assert button_first_row.first_row_button_success_enabled()
        button_first_row.first_row_button_info()
        assert button_first_row.first_row_button_info_enabled()
        button_first_row.first_row_button_warning()
        assert button_first_row.first_row_button_warning_enabled()
        button_first_row.first_row_button_danger()
        assert button_first_row.first_row_button_danger_enabled()
        button_first_row.first_row_button_link()
        assert button_first_row.first_row_button_link_enabled()

    #Testing second row buttons

    def test_02_second_row_buttons(self):
        #self.driver.get(self.baseURL + 'buttons')
        button_second_row = ButtonsPage(self.driver)
        button_second_row.second_row_button_left()
        assert button_second_row.second_row_button_left_enabled()
        button_second_row.second_row_button_middle()
        assert button_second_row.second_row_button_middle_enabled()
        button_second_row.second_row_button_right()
        assert button_second_row.second_row_button_right_enabled()


    def test_03_third_row_buttons(self):
        #self.driver.get(self.baseURL + 'buttons')

        button_third_row = ButtonsPage(self.driver)
        button_third_row.third_row_button_one()
        assert button_third_row.third_row_button_one_enabled()
        button_third_row.third_row_button_two()
        assert button_third_row.third_row_button_two_enabled()
        button_third_row.third_row_button_dropdown()
        assert button_third_row.third_row_button_dropdown_enabled()
        button_third_row.third_row_button_dropdown_one()
        assert button_third_row.third_row_button_dropdown_one_enabled()
        time.sleep(2)
        button_third_row.third_row_button_dropdown()
        assert button_third_row.third_row_button_dropdown_enabled()
        time.sleep(2)
        button_third_row.third_row_button_dropdown_two()
        assert button_third_row.third_row_button_dropdown_two_enabled()











