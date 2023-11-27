from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
import time

class AssessmentKM(MyGenericMethods):

    """Locators Assessment page"""
    LOC_ASSESMENT_PAGE_TITLE = (By.XPATH, '//span[@class=" active"]')
    LOC_GRADE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="da-teacher-dropdown-toggle"]')

    def LOC_GRADE_DROPDOWN_LIST (self, input_grade):
        LOCATOR = '//div[@class="gss-values dropdown-item  dropdown-item" and .="'+input_grade+'"]'
        return

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def do_verify_create_assessment_page(self, input_page_title):
        create_assessment_page_title = self.get_element_text(self.LOC_ASSESMENT_PAGE_TITLE)
        assert input_page_title in create_assessment_page_title, "Buat Penilaian"

    def click_grade_dropdown_field(self):
        self.click_to(self.LOC_GRADE_DROPDOWN_FIELD)
