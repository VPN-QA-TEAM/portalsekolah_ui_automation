import time

from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
from Config.dataconfig import TestData


class StudentDoAssessment(MyGenericMethods):

    """Locators Login page"""
    LOC_ASSESSMENT_PAGE_TITLE = (By.XPATH, '//h3[@class="text-primary font-weight-semibold m-0"]')
    LOC_START_ASSESSMENT_BTN = (By.XPATH, '//button[@class="mr-2 btn-assessment-start"]')
    LOC_BTN_ASSESMENT_SIDEBAR = (By.XPATH, '//li[@class="menu-item icon-ujian"]')
    LOC_ASSESSMENT_TUTORIAL_MODAL_CLOSE_BTN = (By.XPATH, '//button[@title="Tutup"]')
    LOC_ASSESSMENT_CARD = (By.XPATH, '//h6[.="' + TestData.ASSESSMENT_TITLE + '"]/parent::div')
    LOC_TOTAL_QUESTION = (By.XPATH, '//h6/span[@class="label text-primary"]')
    LOC_QUESTION_TYPE = (By.XPATH, '//div[@class="question-header-label"]/span/span')
    LOC_CORRECT_ANSWER_CHOICES = '//div[@class="form-group row mb-1"][{}]'
    LOC_NEXT_BTN = (By.XPATH, '//button[@class="btn btn-primary"]')
    LOC_SUBMIT_BTN = (By.XPATH, ' //div[@class="assessment-submit-modal"]/button[@class="btn btn-blue-primary"]')

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Doing Assessment Functions"""
    def do_verify_assessment_page(self):
        assessment_page_title = self.get_element_text(self.LOC_ASSESSMENT_PAGE_TITLE)
        assert "Penilaian" or "Assessment" in assessment_page_title, "Gagal nih! judul halaman beda!"
        print("Success Go To Assessment Page")

    def go_to_assessment_page(self):
        self.click_to(self.LOC_BTN_ASSESMENT_SIDEBAR)
        self.do_verify_assessment_page()
        self.click_to(self.LOC_ASSESSMENT_TUTORIAL_MODAL_CLOSE_BTN)

    def click_chosen_assessment(self):
        self.click_to(self.LOC_ASSESSMENT_CARD)

    def student_click_start_assessment(self):
        self.click_to(self.LOC_START_ASSESSMENT_BTN)

    def student_answer_assessment(self, input_correct_answer):
        answers = ["A", "B", "C", "D", "E"]
        time.sleep(0.5)
        total_question = int(self.get_element_text(self.LOC_TOTAL_QUESTION))
        question_type = self.get_element_text(self.LOC_QUESTION_TYPE)

        def mcq_question_type():
            self.click_to((By.XPATH, self.LOC_CORRECT_ANSWER_CHOICES.format(answers.index(input_correct_answer) + 1)))

        for i in range(total_question):
            mcq_question_type()
            time.sleep(2)
            if i == total_question - 1:
                self.click_to(self.LOC_SUBMIT_BTN)
            else:
                self.click_to(self.LOC_NEXT_BTN)