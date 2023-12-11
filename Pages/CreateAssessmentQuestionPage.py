from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
from Config.dataconfig import TestData


class CreateQuestion(MyGenericMethods):

    """Locators Assessment page"""
    LOC_QUESTION_FRAME = (By.XPATH, '//form[@class="question-form"]/div[1]//iframe')
    LOC_QUESTION_ANSWER_A_FRAME = (By.XPATH, '//form[@class="question-form"]/div[2]//iframe')
    LOC_QUESTION_ANSWER_B_FRAME = (By.XPATH, '//form[@class="question-form"]/div[3]//iframe')
    LOC_QUESTION_ANSWER_C_FRAME = (By.XPATH, '//form[@class="question-form"]/div[4]//iframe')
    LOC_QUESTION_ANSWER_D_FRAME = (By.XPATH, '//form[@class="question-form"]/div[5]//iframe')
    LOC_QUESTION_ANSWER_E_FRAME = (By.XPATH, '//form[@class="question-form"]/div[6]//iframe')
    LOC_FRAME_TEXT_FIELD = (By.XPATH, '//body[@id="tinymce"]')
    LOC_ANSWER_D_DELETE_BTN = (By.XPATH, '//form[@class="question-form"]/div[5]//button[@class="btn btn-link btn-delete-field"]')
    LOC_MCQ_ANSWER_BTN = '//form[@class="question-form"]/div[{}]//div[@class="input-group-prepend cursorPointer"]'
    LOC_ADD_CHOICES_BTN = (By.XPATH, '//span[@class="ml-4 btn btn-link text-primary"]')
    LOC_CREATE_QUESTION_BTN = (By.XPATH, '//button[@class="btn btn-sm btn-primary font-weight-semibold mr-3 px-3 py-2"]')
    LOC_QUESTION_TYPE_DROPDOWN = (By.XPATH, '//button[@class="btn btn-outline-options btn-sm dropdown-toggle"]')
    LOC_ESSAY_TYPE_DROPDOWN_BTN = (By.XPATH, '//div[@class="dropdown-menu show"]//button[2]')
    LOC_TYPE_MCC_BTN = (By.XPATH, '//div[@class="dropdown-menu show"]//button[6]')
    LOC_CHECKBOX_MCC = "//form[1]/div[{}]/div[1]"   # div[{index}] :  2=A, 3=B, 4=C, 5=D, dst...

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def create_mcq_question(self, number_of_question, number_of_choices, choose_correct_answers):  # Function for create MCQ type question
        answers = ["A", "B", "C", "D", "E"]
        choices = number_of_choices

        def mcq_3_answers_options():  # Function for create MCQ with 3 choices answers
            for i in range(number_of_question):
                # LOC_ANSWERS = (By.XPATH, '//span[.="' + answers[i] + '"]')
                self.click_to(self.LOC_ANSWER_D_DELETE_BTN)
                self.switch_frame(self.LOC_QUESTION_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan PG ' + str(i + 1))
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_A_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_A)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_B_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_B)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_C_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_C)
                self.switch_to_default_frame()
                self.click_to((By.XPATH, self.LOC_MCQ_ANSWER_BTN.format(answers.index(choose_correct_answers) + 2)))
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        def mcq_4_answers_options():  # Function for create MCQ with 4 choices answers
            for i in range(number_of_question):
                # LOC_ANSWERS = (By.XPATH, '//span[.="' + answers[i] + '"]')
                self.switch_frame(self.LOC_QUESTION_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan PG ' + str(i+1))
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_A_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_A)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_B_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_B)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_C_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_C)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_D_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_D)
                self.switch_to_default_frame()
                # self.click_to(LOC_ANSWERS)
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        def mcq_5_answers_options():  # Function for create MCQ with 5 choices answers
            for i in range(number_of_question):
                # LOC_ANSWERS = (By.XPATH, '//span[.="' + answers[i] + '"]')
                self.move_to_element(self.LOC_ADD_CHOICES_BTN)
                self.click_to(self.LOC_ADD_CHOICES_BTN)
                self.move_to_element(self.LOC_QUESTION_FRAME)
                self.switch_frame(self.LOC_QUESTION_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan PG ' + str(i+1))
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_A_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_A)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_B_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_B)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_C_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_C)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_D_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_D)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_E_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_E)
                self.switch_to_default_frame()
                # self.click_to(LOC_ANSWERS)
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        mcq_3_answers_options()

        # if choices == 3:
        #     mcq_3_answers_options()
        # elif choices == 4:
        #     mcq_4_answers_options()
        # elif choices == 5:
        #     mcq_5_answers_options()
        # else:
        #     print("Invalid Input Only Accept 3/4/5")

    def create_essay_question(self, number_of_question):
        for i in range(number_of_question):
            self.click_to(self.LOC_QUESTION_TYPE_DROPDOWN)
            self.click_to(self.LOC_ESSAY_TYPE_DROPDOWN_BTN)
            self.switch_frame(self.LOC_QUESTION_FRAME)
            self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan ESSAY ' + str(i + 1))
            self.switch_to_default_frame()
            self.click_to(self.LOC_CREATE_QUESTION_BTN)

    def create_mcc_question(self, number_of_question, number_of_choices, choose_correct_answers):  # Function for create MCC type question
        answers = ["A", "B", "C", "D", "E"]

        def mcc_3_answers_options():
            for i in range(number_of_question):
                self.click_to(self.LOC_QUESTION_TYPE_DROPDOWN)
                self.click_to(self.LOC_TYPE_MCC_BTN)
                self.click_to(self.LOC_ANSWER_D_DELETE_BTN)
                self.switch_frame(self.LOC_QUESTION_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan MCC ' + str(i + 1))
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_A_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_A)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_B_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_B)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_C_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_C)
                self.switch_to_default_frame()
                for x in range(len(choose_correct_answers)):
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(answers.index(choose_correct_answers[x])+2)))
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        def mcc_4_answers_options():
            for i in range(number_of_question):
                self.click_to(self.LOC_QUESTION_TYPE_DROPDOWN)
                self.click_to(self.LOC_TYPE_MCC_BTN)
                self.switch_frame(self.LOC_QUESTION_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan MCC ' + str(i + 1))
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_A_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_A)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_B_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_B)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_C_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_C)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_D_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_D)
                self.switch_to_default_frame()
                for x in range(len(choose_correct_answers)):
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(answers.index(choose_correct_answers[x])+2)))
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        def mcc_5_answers_options():
            for i in range(number_of_question):
                self.click_to(self.LOC_QUESTION_TYPE_DROPDOWN)
                self.click_to(self.LOC_TYPE_MCC_BTN)
                self.move_to_element(self.LOC_ADD_CHOICES_BTN)
                self.click_to(self.LOC_ADD_CHOICES_BTN)
                self.move_to_element(self.LOC_QUESTION_FRAME)
                self.switch_frame(self.LOC_QUESTION_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan MCC ' + str(i + 1))
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_A_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_A)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_B_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_B)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_C_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_C)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_D_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_D)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_E_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_E)
                self.switch_to_default_frame()
                for x in range(len(choose_correct_answers)):
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(answers.index(choose_correct_answers[x])+2)))
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        if number_of_choices == 3:
            mcc_3_answers_options()
        elif number_of_choices == 4:
            mcc_4_answers_options()
        elif number_of_choices == 5:
            mcc_5_answers_options()