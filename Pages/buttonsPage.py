from selenium.webdriver.common.by import By
from Locators.locators import Locators

class ButtonsPage:

    def __init__(self, driver):
        self.driver = driver

        # First row buttons
        self.button_primary_xpath = Locators.button_primary_xpath
        self.button_success_xpath = Locators.button_success_xpath
        self.button_info_xpath = Locators.button_info_xpath
        self.button_warning_xpath = Locators.button_warning_xpath
        self.button_danger_xpath = Locators.button_danger_xpath
        self.button_link_xpath = Locators.button_link_xpath

        # Second row buttons
        self.button_left_xpath = Locators.button_left_xpath
        self.button_middle_xpath = Locators.button_middle_xpath
        self.button_right_xpath = Locators.button_right_xpath

        # Third row buttons
        self.button_one_xpath = Locators.button_one_xpath
        self.button_two_xpath = Locators.button_two_xpath
        self.button_dropdown_id = Locators.button_dropdown_id
        self.a_dropdown_one_xpath = Locators.a_dropdown_one_xpath
        self.a_dropdown_two_xpath = Locators.a_dropdown_two_xpath

    # First row buttons
    def first_row_button_primary(self):
        self.driver.find_element(By.XPATH, self.button_primary_xpath).click()

    def first_row_button_primary_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_primary_xpath).is_enabled()

    def first_row_button_success(self):
        self.driver.find_element(By.XPATH, self.button_success_xpath).click()

    def first_row_button_success_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_success_xpath).is_enabled()

    def first_row_button_info(self):
        self.driver.find_element(By.XPATH, self.button_warning_xpath).click()

    def first_row_button_info_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_warning_xpath).is_enabled()

    def first_row_button_warning(self):
        self.driver.find_element(By.XPATH, self.button_warning_xpath).click()

    def first_row_button_warning_enabled(self):
       return self.driver.find_element(By.XPATH, self.button_warning_xpath).is_enabled()

    def first_row_button_danger(self):
        self.driver.find_element(By.XPATH, self.button_danger_xpath).click()

    def first_row_button_danger_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_danger_xpath).is_enabled()

    def first_row_button_link(self):
        self.driver.find_element(By.XPATH, self.button_link_xpath).click()

    def first_row_button_link_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_link_xpath).is_enabled()

    # Second row buttons
    def second_row_button_left(self):
        self.driver.find_element(By.XPATH, self.button_left_xpath).click()

    def second_row_button_left_enabled(self):
       return self.driver.find_element(By.XPATH, self.button_left_xpath).is_enabled()

    def second_row_button_middle(self):
        self.driver.find_element(By.XPATH, self.button_right_xpath).click()

    def second_row_button_middle_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_right_xpath).is_enabled()

    def second_row_button_right(self):
        self.driver.find_element(By.XPATH, self.button_right_xpath).click()

    def second_row_button_right_enabled(self):
       return self.driver.find_element(By.XPATH, self.button_right_xpath).is_enabled()

    # Third row buttons

    def third_row_button_one(self):
        self.driver.find_element(By.XPATH, self.button_one_xpath).click()

    def third_row_button_one_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_one_xpath).is_enabled()

    def third_row_button_two(self):
        self.driver.find_element(By.XPATH, self.button_two_xpath).click()

    def third_row_button_two_enabled(self):
        return self.driver.find_element(By.XPATH, self.button_two_xpath).is_enabled()

    def third_row_button_dropdown(self):
        self.driver.find_element(By.ID, self.button_dropdown_id).click()

    def third_row_button_dropdown_enabled(self):
        return self.driver.find_element(By.ID, self.button_dropdown_id).is_enabled()

    def third_row_button_dropdown_one(self):
        self.driver.find_element(By.XPATH, self.a_dropdown_one_xpath).click()

    def third_row_button_dropdown_one_enabled(self):
        return self.driver.find_element(By.XPATH, self.a_dropdown_one_xpath).is_enabled()

    def third_row_button_dropdown_two(self):
        self.driver.find_element(By.XPATH, self.a_dropdown_two_xpath).click()

    def third_row_button_dropdown_two_enabled(self):
       return self.driver.find_element(By.XPATH, self.a_dropdown_two_xpath).is_enabled()
