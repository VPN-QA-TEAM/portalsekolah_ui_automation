from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
import time

class Login(MyGenericMethods):

    """Locators Login page"""
    LOC_USERID = (By.ID, 'login')
    LOC_PASSWD = (By.ID, 'password')
    LOC_BTN_LOGIN = (By.XPATH, '//button[@type="submit" and text()="Masuk"]')
    LOC_TOAST = (By.XPATH, '//div[@class="errorMsgBox show"]')

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Login Functions"""
    def do_login(self, userid, password):
        self.sendkeys_to(self.LOC_USERID, userid)
        self.sendkeys_to(self.LOC_PASSWD, password)
        self.click_to(self.LOC_BTN_LOGIN)

    """Verify Function : Failed login toastbar"""
    def do_verify_toast_failed_login(self, input_validation_message):
        text_failed_toast = self.get_element_text(self.LOC_TOAST)
        assert text_failed_toast == input_validation_message, "Gagal nih! Toastbar warning textnya beda!"
        print(text_failed_toast)