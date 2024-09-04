from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_eight_components():
    driver = setup()
    try:
        print("Accessing the page title...")
        title = driver.title
        print(f"Page title is: {title}")
        assert title == "Web form"

        driver.implicitly_wait(1)  # Implicit wait duration corrected to 1 second

        print("Finding text box element...")
        text_box = driver.find_element(by=By.NAME, value="my-text")

        print("Finding submit button element...")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        print("Entering text...")
        text_box.send_keys("Selenium")

        print("Clicking the submit button...")
        submit_button.click()

        print("Finding confirmation message...")
        message = driver.find_element(by=By.ID, value="message")

        value = message.text
        assert value == "Received!"
    finally:
        teardown(driver)


def setup():
    print("Setting up the web driver...")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    print("Page loaded successfully.")
    return driver


def teardown(driver):
    print("Tearing down the driver...")
    driver.quit()


# Run the test
if __name__ == "__main__":  # Corrected __name__ and __main__
    test_eight_components()