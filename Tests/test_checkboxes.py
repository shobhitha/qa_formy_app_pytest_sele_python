from Utilities.readProperties import ReadConfig
from Pages.checkboxPage import CheckboxPage
import pytest
#autouse=True fixtures are run before each test_* method runs automatically. test_* doesn't have to request for fixtures explicitly
#@pytest.mark.usefixtures("setup") -> setup is made autouse=True
class Test_checkboxes():
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'checkbox')

    #click the checkboxes and checks if checkboxes are selected
    def test_01_checkboxes_is_selected(self):
        #self.driver.get(self.baseURL + 'checkbox')
        checkboxes = CheckboxPage(self.driver)
        checkboxes.checkbox_one_click()
        checkboxes.checkbox_two_click()
        checkboxes.checkbox_three_click()

        assert checkboxes.checkbox_one_selected()
        assert checkboxes.checkbox_two_selected()
        assert checkboxes.checkbox_three_selected()




