from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods


class Logout(MyGenericMethods):

    """Locators Login page"""
    LOC_PROFILE_SIDEBAR_BTN = (By.XPATH, '//li[@class="menu-item avatar-left"]')
    LOC_PROFILE_LOGOUT_OPTION_LIST = (By.XPATH, '//button[@class="profile-item highlight false"]')

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Login Functions"""
    def do_logout(self):
        self.click_to(self.LOC_PROFILE_SIDEBAR_BTN)
        self.click_to(self.LOC_PROFILE_LOGOUT_OPTION_LIST)