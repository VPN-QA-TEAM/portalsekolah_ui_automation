import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages - It contains all the generic methods and utilities for all the pages"""


class MyGenericMethods:

    def __init__(self, driver):
        self.driver = driver

    def click_to(self, input_locator_or_element):
        if isinstance(input_locator_or_element, tuple):
            WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located(input_locator_or_element)).click()
        elif isinstance(input_locator_or_element, WebElement):
            input_locator_or_element.click()
        else:
            raise ValueError("Invalid input. harus masukin tuple(locator) atau WebElement ya bro!!!")

    def sendkeys_to(self, input_locator, input_text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator)).send_keys(input_text)

    def clear_field(self, input_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator)).clear()

    def get_element_text(self, input_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator))
        return element.text

    def get_elements_text(self, input_locator_plural):
        elements = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(input_locator_plural))
        return elements

    def is_visible(self, input_locator):
        element = WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located(input_locator))
        return bool(element)

    def find_element(self, input_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(input_locator))
        return element

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

    def move_to_element(self, input_locators):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(input_locators)).perform()
        time.sleep(1.5)

    def switch_frame(self, input_locator):
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(input_locator))

    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()

    def accept_alert(self):
        alert_msg = self.driver.switch_to.alert
        alert_msg.accept()