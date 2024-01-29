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
    LOC_MCQ_CORRECT_ANSWER_CHOICES = '//div[@class="form-group row mb-1"][{}]'
    LOC_TRUE_FALSE_CORRECT_ANSWER_CHOICES = '//div[@class="form-control optionValBox standaloneOpt cursorPointer mb-3 "][{}]'
    LOC_SHORT_ANSWER_INPUT_FIELD = (By.XPATH, '//input[@class="form-control fillInInput"]')
    LOC_MCC_CORRECT_ANSWER_CHOICES = '//div[@class="form"]/div[@class="form-group row mb-1 mx-0"][{}]'
    LOC_MATCHING_DROP_ANSWER_TARGET = '//div[@class="col-md-8"]/div[@class="row mb-3"][{}]//div[@class="droppable "]'
    LOC_MATCHING_DRAG_CHOICES_ANSWER = '//div[@class="col-md-4"]/div[@class="matching-option"][{}]'
    LOC_GET_TOTAL_MATCHING_SET = (By.XPATH, '//div[@class="col-md-4"]/div')
    LOC_NEXT_BTN = (By.XPATH, '//button[@class="btn btn-primary"]')
    LOC_SUBMIT_BTN = (By.XPATH, ' //div[@class="assessment-submit-modal"]/button[@class="btn btn-blue-primary"]')
    LOC_CONFIRM_SUBMIT_BTN = (By.XPATH, '//div[@class="modal-content p-4"]//button[@class="btn btn-blue-primary"]')
    LOC_CANCEL_SUBMIT_BTN = (By.XPATH, '//button[@class="btn btn-outline-edit"]')

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

    def student_answer_assessment(self, input_mcq_answer, input_true_false_answer, input_short_essay_answer, input_mcc_answer):
        answers = ["A", "B", "C", "D", "E"]
        time.sleep(0.5)
        total_question = int(self.get_element_text(self.LOC_TOTAL_QUESTION))

        def mcq_question_type():
            self.click_to((By.XPATH, self.LOC_MCQ_CORRECT_ANSWER_CHOICES.format(answers.index(input_mcq_answer) + 1)))

        def true_false_question_type():
            if input_true_false_answer == "true":
                self.click_to((By.XPATH, self.LOC_TRUE_FALSE_CORRECT_ANSWER_CHOICES.format(1)))
            elif input_true_false_answer == "false":
                self.click_to((By.XPATH, self.LOC_TRUE_FALSE_CORRECT_ANSWER_CHOICES.format(2)))

        def short_answer_question_type():
            self.sendkeys_to(self.LOC_SHORT_ANSWER_INPUT_FIELD, input_short_essay_answer)

        def mcc_question_type():
            for x in range(len(input_mcc_answer)):
                self.click_to(
                    (By.XPATH, self.LOC_MCC_CORRECT_ANSWER_CHOICES.format(answers.index(input_mcc_answer[x]) + 1)))

        def matching_question_type():
            total_matching_set = self.count_element(self.LOC_GET_TOTAL_MATCHING_SET)

            for x in range(total_matching_set):
                time.sleep(3)
                choices = self.get_element_text((By.XPATH, self.LOC_MATCHING_DRAG_CHOICES_ANSWER.format(x + 1)))

                if choices == "A":
                    self.drag_drop_element((By.XPATH, self.LOC_MATCHING_DRAG_CHOICES_ANSWER.format(x+1)), (By.XPATH, self.LOC_MATCHING_DROP_ANSWER_TARGET.format(1)))
                    print(x + 1, choices)
                elif choices == "B":
                    self.drag_drop_element((By.XPATH, self.LOC_MATCHING_DRAG_CHOICES_ANSWER.format(x+1)), (By.XPATH, self.LOC_MATCHING_DROP_ANSWER_TARGET.format(2)))
                    print(x + 1, choices)
                elif choices == "C":
                    self.drag_drop_element((By.XPATH, self.LOC_MATCHING_DRAG_CHOICES_ANSWER.format(x+1)), (By.XPATH, self.LOC_MATCHING_DROP_ANSWER_TARGET.format(3)))
                    print(x + 1, choices)
                elif choices == "D":
                    self.drag_drop_element((By.XPATH, self.LOC_MATCHING_DRAG_CHOICES_ANSWER.format(x+1)), (By.XPATH, self.LOC_MATCHING_DROP_ANSWER_TARGET.format(4)))
                    print(x + 1, choices)
                elif choices == "E":
                    self.drag_drop_element((By.XPATH, self.LOC_MATCHING_DRAG_CHOICES_ANSWER.format(x+1)), (By.XPATH, self.LOC_MATCHING_DROP_ANSWER_TARGET.format(5)))
                    print(x + 1, choices)

            print("Matching Question Done")

        for i in range(total_question):
            time.sleep(2)
            question_type = self.get_element_text(self.LOC_QUESTION_TYPE)  # Value : PG, BS, ..., PGK, ><

            if question_type == "PG":
                mcq_question_type()
            elif question_type == "BS":
                true_false_question_type()
            elif question_type == "...":
                short_answer_question_type()
            elif question_type == "PGK":
                mcc_question_type()
            elif question_type == "><":
                matching_question_type()

            if i == total_question - 1:
                self.click_to(self.LOC_SUBMIT_BTN)
            else:
                self.click_to(self.LOC_NEXT_BTN)

        # self.click_to(self.LOC_CONFIRM_SUBMIT_BTN)
