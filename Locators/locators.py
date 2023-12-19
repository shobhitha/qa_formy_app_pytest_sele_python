
class Locators:

    # 01) Autocomplete page locators
    input_autocomplete_id = 'autocomplete'
    dropdown_autocomplete_class = 'pac-icon'
    input_street_number_id = 'street_number'
    input_route_id = 'route'
    input_locality_id = 'locality'
    input_administrative_area_level_1_id = 'administrative_area_level_1'
    input_postal_code_id = 'postal_code'
    input_country_id = 'country'
    full_address_text = 'Komarova steet, 1, Chernivtsi, Ukraine'

    #02) Button Page locators

    #First row locators
    button_primary_xpath = "//button[contains(text(), 'Primary')]"
    button_success_xpath = "//button[contains(text(), 'Success')]"
    button_info_xpath = "//button[contains(text(), 'Info')]"
    button_warning_xpath = "//button[contains(text(),'Warning')]"
    button_danger_xpath = "//button[contains(text(),'Danger')]"
    button_link_xpath = "//button[contains(text(),'Link')]"

    #Second row locators
    button_left_xpath = "//button[contains(text(), 'Left')]"
    button_middle_xpath = "//button[contains(text(), 'Middle')]"
    button_right_xpath = "//button[contains(text(), 'Right')]"

    #Third row locators
    button_one_xpath = "//button[contains(text(),'1')]"
    button_two_xpath = "//button[contains(text(),'2')]"
    button_dropdown_id = "btnGroupDrop1"
    a_dropdown_one_xpath = "//a[contains(text(), 'Dropdown link 1')]"
    a_dropdown_two_xpath = "//a[contains(text(), 'Dropdown link 2')]"

    #03) Checkbox Page locators

    checkbox_one_id = "checkbox-1"
    checkbox_two_id = "checkbox-2"
    checkbox_three_id = "checkbox-3"

    #04 Date Picker locators

    input_datepicker_id = "datepicker"
    datepicker_today_xpath = '//td[@class = "today active day"]'
    datepicker_other_date_xpath ='//td[@class="active day"]'
















