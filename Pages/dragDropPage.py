from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DragDropPage:

    def __init__(self,driver):
        self.driver = driver
        self.drag_img_id = Locators.drag_img_id
        self.drop_box_id = Locators.drop_box_id
        self.dropped_text_xpath = Locators.dropped_text_xpath

    def drag_image(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.drag_img_id)))

    def drop_box(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, self.drop_box_id)))




