import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions

# Fixture to set up the Appium driver
@pytest.fixture(scope="session")
def appium_driver():
    """Setup the Appium driver."""
    # Create XCUITestOptions with the desired capabilities
    options = XCUITestOptions()
    options.set_capability("platformName", "iOS")
    options.set_capability("appium:deviceName", "iPhone 16")
    options.set_capability("appium:platformVersion", "18.2")
    options.set_capability("appium:automationName", "XCUITest")
    options.set_capability("appium:app", "/Users/siri/Desktop/Appium_Automation_ios_android/ipaforiosapp/iOS.Simulator.SauceLabs.Mobile.Sample.app.2.7.1.app")

    # Appium server URL
    appium_server_url = "http://127.0.0.1:4723/wd/hub"

    # Initialize the Appium driver
    driver = webdriver.Remote(command_executor=appium_server_url, options=options)

    # Yield the driver to the testm 
    yield driver

    # Quit the driver after the test is done
    driver.quit()
