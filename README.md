This project automates testing of UI application formy_app(https://formy-project.herokuapp.com/) using Python, pytest, selenium sebdriver and pytest-html. The entire framework is based on Page Object Model (POM) which reduces code duplication and increases the ease of test framework maintenance.

**Page Object Model(POM) structure for this projects is as follows:**

    Locators - locators directory
    Pages - project pages directory
    Tests - project tests directory
    Reports - HTML reports directory
    Utilities - Getting configurations directory
    Configurations - Variables configurations directory
    conftest.py - pytest fixtures for etup and teardown
    
**Technologies used for automation framework are:**

    Python : Programming language
    Selenium Webdriver : Automation framework for web-applications
    pytest :  Python testing framework
    pytest-html: plugin for pytest that generates a HTML report for test results

**Packages and its dependencies can be installed by running:**  

pipenv install  or pipenv install --dev ( for development environment)

**To run all tests at once, goto Tests directory and run:**

pytest -v -s  --html=Reports/reports.html Tests/test_*

**To run a particular test:**

pytest -v -s  --html=Reports/buttons_reports.html Tests/test_buttons.py

**To run a test method from a test class:**

pytest -v -s  --html=Reports/reports.html Tests/test_buttons.py::Test_ButtonPage::test_first_row_buttons


**To run individual test from a test class:**

pytest -v -s  --html=Reports/buttons_reports.html Tests/test_buttons.py::Test_ButtonPage::test_first_row_buttons


