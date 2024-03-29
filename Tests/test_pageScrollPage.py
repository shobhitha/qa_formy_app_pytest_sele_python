from selenium.webdriver import ActionChains
from Utilities.readProperties import ReadConfig
from Pages.pageScroll import PageScroll
import pytest
from Tests.test_datepicker import today_date

class Test_pageScrollPage:
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'scroll')

    #Test the page scrolling functionality
    def test_01_pageScroll(self):

        pageScroll_obj = PageScroll(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(pageScroll_obj.scroll_name_ele())
        pageScroll_obj.scroll_name_input('John')
        pageScroll_obj.scroll_date_input(today_date())

