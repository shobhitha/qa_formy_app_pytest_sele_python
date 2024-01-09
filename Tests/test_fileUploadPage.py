from Utilities.readProperties import ReadConfig
from Pages.fileUploadPage import FileUploadPage
import time
import pytest
from Locators.locators import Locators

class Test_fileUploadPage:

    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'fileupload')

    def test_01_file_upload_reset(self):

        file_upload_obj = FileUploadPage(self.driver)
        file_upload_obj.file_upload_input_send_keys(Locators.file_loc)
        time.sleep(1)
        file_upload_obj.file_upload_reset_buttn_click()
