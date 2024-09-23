from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_layout_html_rendering():
    driver = webdriver.Chrome()

    try:
        driver.get("https://docs.kedro.org/")

        # Simulate Cmd+K / Ctrl+K keypress
        action = ActionChains(driver)
        action.key_down(Keys.COMMAND).send_keys('k').key_up(Keys.COMMAND).perform()  # For Mac

        # Retrieve all links under the wy-main-nav class with a tag
        links = driver.find_elements(By.CSS_SELECTOR, ".wy-main-nav a")

        # Get the current URL
        current_url = driver.current_url

        active_link = None

        for link in links:
            if 'active' in link.get_attribute('class').split():
                active_link = link
                break
            
        assert active_link is not None, "No active link found under wy-main-nav class."

    finally:
        driver.quit()