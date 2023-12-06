from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.BaseMethod import MyGenericMethods
from datetime import datetime, timedelta, date


class CreateQuestion(MyGenericMethods):

    """Locators Assessment page"""



    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)