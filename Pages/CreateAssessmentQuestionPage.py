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
    LOC_ADD_CHOICES_BTN = (By.XPATH, '//span[@class="ml-4 btn btn-link text-primary"]')
    LOC_CREATE_QUESTION_BTN = (By.XPATH, '//button[@class="btn btn-sm btn-primary font-weight-semibold mr-3 px-3 py-2"]')
    LOC_QUESTION_TYPE_DROPDOWN = (By.XPATH, '//button[@class="btn btn-outline-options btn-sm dropdown-toggle"]')
    LOC_ESSAY_TYPE_DROPDOWN_BTN = (By.XPATH, '//div[@class="dropdown-menu show"]//button[2]')
    LOC_TYPE_MCC_BTN = (By.XPATH, '//div[@class="dropdown-menu show"]//button[6]')
    LOC_CHECKBOX_A_MCC_ANSWER = (By.XPATH, "//form[1]/div[2]/div[1]")
    LOC_CHECKBOX_B_MCC_ANSWER = (By.XPATH, "//form[1]/div[3]/div[1]")
    LOC_CHECKBOX_C_MCC_ANSWER = (By.XPATH, "//form[1]/div[4]/div[1]")
    LOC_CHECKBOX_D_MCC_ANSWER = (By.XPATH, "//form[1]/div[5]/div[1]")
    LOC_CHECKBOX_E_MCC_ANSWER = (By.XPATH, "//form[1]/div[5]/div[1]")
    LOC_CHECKBOX_MCC = "//form[1]/div[{}]/div[1]"   # div[{index}] :  2=A, 3=B, 4=C, 5=D, dst...

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def create_mcq_question(self, number_of_question, number_of_choices):  # Function for create MCQ type question
        answers = ["A", "B", "C", "D", "E"]
        choices = number_of_choices

        def mcq_3_answers_options():  # Function for create MCQ with 3 choices answers
            for i in range(number_of_question):
                LOC_ANSWERS = (By.XPATH, '//span[.="' + answers[i] + '"]')
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
                self.click_to(LOC_ANSWERS)
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        def mcq_4_answers_options():  # Function for create MCQ with 4 choices answers
            for i in range(number_of_question):
                LOC_ANSWERS = (By.XPATH, '//span[.="' + answers[i] + '"]')
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
                self.click_to(LOC_ANSWERS)
                self.click_to(self.LOC_CREATE_QUESTION_BTN)

        def mcq_5_answers_options():  # Function for create MCQ with 5 choices answers
            for i in range(number_of_question):
                LOC_ANSWERS = (By.XPATH, '//span[.="' + answers[i] + '"]')
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
                self.click_to(LOC_ANSWERS)
                self.click_to(self.LOC_CREATE_QUESTION_BTN)
        if choices == 3:
            mcq_3_answers_options()
        elif choices == 4:
            mcq_4_answers_options()
        elif choices == 5:
            mcq_5_answers_options()
        else:
            print("Invalid Input Only Accept 3/4/5")

    def create_essay_question(self, number_of_question):
        for i in range(number_of_question):
            self.click_to(self.LOC_QUESTION_TYPE_DROPDOWN)
            self.click_to(self.LOC_ESSAY_TYPE_DROPDOWN_BTN)
            self.switch_frame(self.LOC_QUESTION_FRAME)
            self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan ESSAY ' + str(i + 1))
            self.switch_to_default_frame()
            self.click_to(self.LOC_CREATE_QUESTION_BTN)

    def create_mcc_question(self, number_of_question, number_of_choices, choose_correct_answers):  # Function for create MCC type question
        for i in range(number_of_question):
            self.click_to(self.LOC_QUESTION_TYPE_DROPDOWN)
            self.click_to(self.LOC_TYPE_MCC_BTN)
            self.switch_frame(self.LOC_QUESTION_FRAME)
            self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, 'Pertanyaan MCC' + str(i + 1))
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
            if number_of_choices == 3:
                A, B, C = 2, 3, 4
                self.click_to(self.LOC_ANSWER_D_DELETE_BTN)
                if set(choose_correct_answers) == {"A"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(A)))
                elif set(choose_correct_answers) == {"B"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(B)))
                elif set(choose_correct_answers) == {"C"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(C)))
                elif set(choose_correct_answers) == {"A", "B"}:
                    for ab in range(2, 4):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ab)))
                elif set(choose_correct_answers) == {"B", "C"}:
                    for bc in range(3, 5):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(bc)))
                elif set(choose_correct_answers) == {"A", "C"}:
                    for ac in range(2, 5, 2):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ac)))
                elif set(choose_correct_answers) == {'A', 'B', 'C'}:
                    for abc in range(2, 5):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abc)))
                else:
                    raise ValueError("Number of Choices anda 3, hanya bs pilih A-C, periksa lagi ya!")

            elif number_of_choices == 4:
                A, B, C, D = 2, 3, 4, 5
                self.switch_frame(self.LOC_QUESTION_ANSWER_D_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_D)
                self.switch_to_default_frame()
                if set(choose_correct_answers) == {"A"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(A)))
                elif set(choose_correct_answers) == {"B"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(B)))
                elif set(choose_correct_answers) == {"C"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(C)))
                elif set(choose_correct_answers) == {"A", "B"}:
                    for ab in range(2, 4):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ab)))
                elif set(choose_correct_answers) == {"B", "C"}:
                    for bc in range(3, 5):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(bc)))
                elif set(choose_correct_answers) == {"A", "C"}:
                    for ac in range(2, 5, 2):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ac)))
                elif set(choose_correct_answers) == {'A', 'B', 'C'}:
                    for abc in range(2, 5):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abc)))
                elif set(choose_correct_answers) == {'A', 'B', 'C' 'D'}:
                    for abcd in range(2, 6):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abcd)))
                elif set(choose_correct_answers) == {'A', 'B', 'D'}:
                    lis = [2, 3, 5]
                    for abd in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abd)))
                elif set(choose_correct_answers) == {'B', 'C', 'D'}:
                    for bcd in range(2, 5):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(bcd)))
                elif set(choose_correct_answers) == {'A', 'C', 'D'}:
                    lis = [2, 4, 5]
                    for acd in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(acd)))
                else:
                    raise ValueError("Number of Choices anda 4, hanya bs pilih A-D, periksa lagi ya!")

            elif number_of_choices == 5:
                A, B, C, D, E = 2, 3, 4, 5, 6
                self.move_to_element(self.LOC_ADD_CHOICES_BTN)
                self.click_to(self.LOC_ADD_CHOICES_BTN)
                self.switch_frame(self.LOC_QUESTION_ANSWER_D_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_D)
                self.switch_to_default_frame()
                self.switch_frame(self.LOC_QUESTION_ANSWER_E_FRAME)
                self.sendkeys_to(self.LOC_FRAME_TEXT_FIELD, TestData.CHOICES_E)
                self.switch_to_default_frame()
                if set(choose_correct_answers) == {"A"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(A)))
                elif set(choose_correct_answers) == {"B"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(B)))
                elif set(choose_correct_answers) == {"C"}:
                    self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(C)))
                elif set(choose_correct_answers) == {"A", "B"}:
                    for ab in range(2, 4):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ab)))
                elif set(choose_correct_answers) == {"B", "C"}:
                    for bc in range(3, 5):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(bc)))
                elif set(choose_correct_answers) == {"A", "C"}:
                    for ac in range(2, 5, 2):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ac)))
                elif set(choose_correct_answers) == {'A', 'B', 'C'}:
                    for abc in range(2, 5):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abc)))
                elif set(choose_correct_answers) == {'A', 'B', 'C' 'D'}:
                    for abcd in range(2, 6):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abcd)))
                elif set(choose_correct_answers) == {'A', 'B', 'C' 'D', 'E'}:
                    for abcde in range(2, 7):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abcde)))
                elif set(choose_correct_answers) == {'A', 'B', 'E'}:
                    lis = [2, 3, 6]
                    for abe in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abe)))
                elif set(choose_correct_answers) == {'A', 'B', 'D'}:
                    lis = [2, 3, 5]
                    for abd in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(abd)))
                elif set(choose_correct_answers) == {'B', 'C', 'D'}:
                    for bcd in range(3, 6):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(bcd)))
                elif set(choose_correct_answers) == {'A', 'C', 'D'}:
                    lis = [2, 4, 5]
                    for acd in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(acd)))
                elif set(choose_correct_answers) == {'A', 'C', 'E'}:
                    for ace in range(2, 7, 2):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ace)))
                elif set(choose_correct_answers) == {'A', 'D', 'E'}:
                    lis = [2, 5, 6]
                    for ade in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ade)))
                elif set(choose_correct_answers) == {'B', 'C', 'E'}:
                    lis = [3, 4, 6]
                    for bce in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(bce)))
                elif set(choose_correct_answers) == {'B', 'D', 'E'}:
                    lis = [3, 5, 6]
                    for bde in lis:
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(bde)))
                elif set(choose_correct_answers) == {'C', 'D', 'E'}:
                    for ace in range(4, 7):
                        self.click_to((By.XPATH, self.LOC_CHECKBOX_MCC.format(ace)))
                else:
                    raise ValueError("Number of Choices anda hanya 5, hanya bs pilih A-E, periksa lagi ya!")
            else:
                raise ValueError(
                    "parameter 'number_of_choices' yang anda input tidak sesuai yang sudah ditentukan(3, 4, or 5)! periksa lagi!")
            self.click_to(self.LOC_CREATE_QUESTION_BTN)