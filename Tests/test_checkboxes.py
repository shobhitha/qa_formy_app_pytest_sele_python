from Utilities.readProperties import ReadConfig
from Pages.checkboxPage import CheckboxPage

class Test_checkboxes():
    baseURL = ReadConfig.getApplicationURL()

    #click the checkboxes and checks if checkboxes are selected
    def test_checkboxes_is_selected(self):
        self.driver.get(self.baseURL + 'checkbox')
        checkboxes = CheckboxPage(self.driver)
        checkboxes.checkbox_one_click()
        checkboxes.checkbox_two_click()
        checkboxes.checkbox_three_click()

        assert checkboxes.checkbox_one_selected()
        assert checkboxes.checkbox_two_selected()
        assert checkboxes.checkbox_three_selected()




