from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
from Config.dataconfig import TestData
from Pages.LoginPage import Login
from Pages.DashboardPage import DashboardStudent


class AssessmentAssertion(MyGenericMethods):

    """Locators Assessment Assertion"""
    LOC_BTN_ASSESMENT_SIDEBAR = (By.XPATH, '//li[@class="menu-item icon-ujian"]')
    LOC_ASSESSMENT_TITLE_ASSERTION = (By.XPATH, '//h6[.="' + TestData.ASSESSMENT_TITLE + '"]')
    LOC_ASSESSMENT_CARD = (By.XPATH, '//h6[.="' + TestData.ASSESSMENT_TITLE + '"]/parent::div')
    LOC_ASSESSMENT_INSTRUCTION = (By.XPATH, '//p[.="'+TestData.ASSESSMENT_TITLE+'"]')
    LOC_ASSESSMENT_TUTORIAL_MODAL_CLOSE_BTN =(By.XPATH, '//button[@title="Tutup"]')

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Assessment Assertion Function"""

    def do_verify_assessment_created_successfully_teacher(self):
        create_assessment_page_title = self.get_element_text(self.LOC_ASSESSMENT_TITLE_ASSERTION)
        assert TestData.ASSESSMENT_TITLE in create_assessment_page_title, "No matching assessment appear"
        print('Assessment ' + TestData.ASSESSMENT_TITLE + ' successfully published and appear on teacher side')

    def do_verify_assessment_created_successfully_student(self):
        login = Login(self.driver)
        dashboard_student = DashboardStudent(self.driver)
        login.do_login(TestData.USERID_STUDENT9, TestData.VALID_PASSWORD)
        dashboard_student.is_modal_email_after_login_visible()
        self.click_to(self.LOC_BTN_ASSESMENT_SIDEBAR)
        get_assessment_page_title = self.get_element_text(self.LOC_ASSESSMENT_TITLE_ASSERTION)
        assert TestData.ASSESSMENT_TITLE in get_assessment_page_title, "No matching assessment appear"
        print('Assessment ' + TestData.ASSESSMENT_TITLE + ' successfully published and appear on student side')
        self.click_to(self.LOC_ASSESSMENT_TUTORIAL_MODAL_CLOSE_BTN)
        self.click_to(self.LOC_ASSESSMENT_CARD)
        get_assessment_instruction_text = self.get_element_text(self.LOC_ASSESSMENT_INSTRUCTION)
        assert TestData.ASSESSMENT_TITLE in get_assessment_instruction_text, "Assessment Instruction Text Not Match"
        print("Assessment Instruction Text Is Match")

