
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

    #05 Drag and Drop locators

    drag_img_id = "image"
    drop_box_id = "box"
    dropped_text_xpath = '//div[@id="box"]/p'

    #06 DropDown locators

    button_dropdown_page_id = 'dropdownMenuButton'
    a_dropdown_autocomplete_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Autocomplete')]"
    a_dropdown_buttons_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Buttons')]"
    a_dropdown_checkbox_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Checkbox')]"
    a_dropdown_datepicker_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Datepicker')]"
    a_dropdown_draganddrop_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Drag and Drop')]"

    a_dropdown_dropdown_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Dropdown')]"
    a_dropdown_enabledisableelements_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Enabled and disabled elements')]"
    a_dropdown_fileupload_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'File Upload')]"
    a_dropdown_filedownload_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'File Download')]"
    a_dropdown_keymousepress_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Key and Mouse Press')]"

    a_dropdown_modal_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Modal')]"
    a_dropdown_pagesroll_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Page Scroll')]"
    a_dropdown_radiobutton_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Radio Button')]"
    a_dropdown_switchwindow_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Switch Window')]"
    a_dropdown_completewebform_xpath = "//div[@class='dropdown-menu show']//a[@class='dropdown-item'][contains(text(),'Complete Web Form')]"

    #07 Enabled and Disabled elements

    input_disabled_id = 'disabledInput'
    input_enabled_id = 'input'

    #08 File Upload
    file_loc = '/Users/Raghu/qa_formy_app_pytest_sele_html/Locators/test_file.txt'
    input_file_upload_field_id = 'file-upload-field'
    button_upload_choose_xpath = "//button[contains(text(),'Choose')]"
    button_upload_reset_xpath = "//button[contains(text(),'Reset')]"

    #09 Keyboard and Mouse Input

    input_fullName_id = 'name'
    button_clickbutton_id = 'button'

    #10 Modal Page locators

    button_modal_id = 'modal-button'
    div_modal_id = 'exampleModal'
    close_button_id = 'close-button'

    # 11) Scroll page locators
    input_scroll_name_id = 'name'
    input_scroll_date_id = 'date'

    # 12) Radio buttons page locators
    input_radio_one_xpath = "//input[@value='option1']"
    input_radio_two_xpath = "//input[@value='option2']"
    input_radio_three_xpath = "//input[@value='option3']"

    # 13) Switch windows page locators
    button_switchWindow_newTab_id = 'new-tab-button'
    button_switchWindow_alert_id = 'alert-button'
































