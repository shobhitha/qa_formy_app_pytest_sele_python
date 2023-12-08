This project automates testing of UI application formy_app(https://formy-project.herokuapp.com/). The entire framework is based on Page Object Model (POM) which reduces code duplication and increases the ease of test framework maintenance.

**Page Object Model(POM) structure for this projects is as follows:**

    Locators - locators directory
    Pages - project pages directory
    Tests - project tests directory
    Reports - HTML reports directory
    Utilities - Getting configurations directory
    Configurations - Variables configurations directory
    
**Technologies used for automation framework are:**

    Python : Programming language
    Selenium Webdriver : Automation framework for web-applications
    pytest :  Python testing framework
    pytest-html: plugin for pytest that generates a HTML report for test results

**Packages and its dependencies can be installed by running:**  

pipenv install  or pipenv install --dev ( for development environment)

**To run all tests at once, goto Tests directory and run:**

pytest -v -s  --html=Reports/checkbox_reports.html Tests/test_*

**To run a particular test:**

pytest -v -s  --html=Reports/checkbox_reports.html Tests/test_checkboxes.py

