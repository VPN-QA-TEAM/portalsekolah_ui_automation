import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages - It contains all the generic methods and utilities for all the pages"""

class MyGenericMethods:

    def __init__(self, driver):
        self.driver = driver

    def click_to(self, input_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator)).click()

    def sendkeys_to(self, input_locator, input_text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator)).send_keys(input_text)

    def get_element_text(self, input_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator))
        return element.text

    def is_visible(self, input_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator))
        return bool(element)

    # def scroll_down_page(self):
    #     self.driver.execute_script("window.scrollTo(190, document.documentElement.scrollHeight);")
    #     time.sleep(1.5)  # Add a short delay to allow content loading (adjust as needed)
    #
    # def scroll_up_page(self):
    #     # Scroll up to the top of the page
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #     time.sleep(1.5)

    def scroll_down_page(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1.5)  # Add a short delay to allow content loading (adjust as needed)

    def scroll_up_page(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP).perform()
        time.sleep(1.5)  # Add a short delay to allow content loading (adjust as needed)
