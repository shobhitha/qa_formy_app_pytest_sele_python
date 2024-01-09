from datetime import date
import random
import pytest
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadConfig
from Pages.datePickerPage import DatePickerPage

def today_date():
    dt = date.today()
    dt_format = dt.strftime("%m/%d/%Y")
    return dt_format

def random_date():
    random_day = random.randint(1,28)
    random_month = random.randint(1,12)

    if len(str(random_day)) < 2:
        random_day = "0" + str(random_day)
    if len(str(random_month)) < 2:
        random_month = "0" + str(random_month)
    random_date = str(random_month) + "/" + str(random_day) + "/2023"
    return random_date

#autouse=True fixtures are run before each test_* method runs automatically. test_* doesn't have to request for fixtures explicitly
#@pytest.mark.usefixtures("setup") -> setup is made autouse=True
class Test_datepicker:
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'datepicker')

    #Test if todays date is selected
    def test_01_select_todays_date(self):
        #self.driver.get(self.baseURL + 'datepicker')
        today_date_select = DatePickerPage(self.driver)
        today_date_select.datepicker_input(today_date())
        today_date_select.datepicker_today_date()

        selected_today_date = self.driver.find_element(By.ID, today_date_select.input_datepicker_id).get_attribute("value")
        assert selected_today_date == today_date()

    #Test if a random date is selected
    def test_02_select_random_date(self):
        #self.driver.get(self.baseURL + 'datepicker')
        random_date_select = DatePickerPage(self.driver)
        rd_date = random_date()
        random_date_select.datepicker_input(rd_date)
        random_date_select. datepicker_other_date()

        selected_random_date = self.driver.find_element(By.ID, random_date_select.input_datepicker_id).get_attribute("value")
        assert selected_random_date == rd_date









