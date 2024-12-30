import pytest
from pytest_bdd import scenarios, given, when, then
from main.utils.drivertest import appium_driver  # Import the driver fixture

# Link to the feature file
scenarios("../../resources/features/login.feature")

@given("the user is on the login page")
def test_navigate_to_login_page(appium_driver):
    print("Navigating to the login page")
    # Navigating to the login page and entering the username
    appium_driver.find_element("accessibility id", "test-Username").send_keys("standard_user")

@when("the user enters valid login details")
def enter_login_details(appium_driver):
    print("Entering valid login details")
    # Entering the password
    appium_driver.find_element("accessibility id", "test-Password").send_keys("secret_sauce")

@when("the user clicks on the login button")
def click_login_button(appium_driver):
    print("Clicking the login button")
    # Clicking the login button
    appium_driver.find_element("xpath", "//XCUIElementTypeOther[@name='test-LOGIN']").click()

@then("the user should log in successfully")
def verify_login(appium_driver):
    print("Verifying login success")
    appium_driver.find_element("xpath", "//XCUIElementTypeOther[@name='test-Modal Selector Button']/XCUIElementTypeOther/XCUIElementTypeOther").click()
    appium_driver.find_element("xpath", "(//XCUIElementTypeOther[@name='Horizontal scroll bar, 2 pages'])[2]").click()

    