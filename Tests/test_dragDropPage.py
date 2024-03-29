from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages.dragDropPage import DragDropPage
import time
import pytest
from Utilities.readProperties import ReadConfig
class Test_dragDropPage:
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(scope='class', autouse=True)
    def getURL(self):
        self.driver.get(self.baseURL + 'dragdrop')

    #Test if drag and drop image action perfomed correctly
    def test_01_dragDropImg(self):

        #self.driver.get(self.baseURL + 'dragdrop')

        dragDropObj = DragDropPage(self.driver)
        image = dragDropObj.drag_image()
        box = dragDropObj.drop_box()

        ActionChains(self.driver).drag_and_drop(image, box).perform()
        time.sleep(2)
        assert (self.driver.find_element(By.XPATH,'//div[@id="box"]/p').get_attribute("innerHTML")) == 'Dropped!'






