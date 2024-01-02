import pytest
from Config.dataconfig import TestData
from Pages.LoginPage import Login
from Pages.DashboardPage import DashboardTeacher
from Pages.AssessmentKmPage import AssessmentKM
from Pages.CreateAssessmentQuestionPage import CreateQuestion
from Pages.LogoutPage import Logout
from Pages.AssessmentAssertion import AssessmentAssertion
import time


@pytest.mark.usefixtures("setup_scope_function")
class TestAssessmentKM:

    @pytest.mark.doing
    def test_tc_km01(self):
        login = Login(self.driver)
        dashboard_teacher = DashboardTeacher(self.driver)
        assessment_km = AssessmentKM(self.driver)
        create_question = CreateQuestion(self.driver)
        assessment_assertion = AssessmentAssertion(self.driver)
        logout = Logout(self.driver)
        login.do_login(TestData.USERID_TEACHER_KM, TestData.VALID_PASSWORD)
        dashboard_teacher.is_modal_email_after_login_visible()
        dashboard_teacher.click_sidebar_assessment_menu()

        '''--------------------- THIS IS ASSESSMENT CREATOR SECTION PAGE:----------------------------------------'''
        assessment_km.do_verify_create_assessment_page("Buat Penilaian")
        assessment_km.choose_grade_course("7 KM TKJ - BIOLOGI")
        assessment_km.input_title(TestData.ASSESSMENT_TITLE)
        assessment_km.choose_assessment_category("formative")  # input category = formative / summative
        assessment_km.set_semester("1")  # semester = 1 / 2
        assessment_km.set_post_to(["7-A", "7-B", "7-C"])  # Parameter Type : String List, Input list of class_name inside the list
        assessment_km.set_date_time_deadline(2, 10, 30)
        assessment_km.set_post_result_time_dropdown_list("automatic_on_deadline")  # input time option = automatic_on_deadline / manual / scheduled
        assessment_km.set_result_type_dropdown_list("grade_with_submission_detail")  # result type input = grade_with_submission_detail / grade_only
        assessment_km.set_publish_schedule("publish_immediately")  # public schedule input : publish_immediately / publish_for_future
        assessment_km.input_instruction(TestData.ASSESSMENT_TITLE)
        assessment_km.click_create_question_new()

        '''--------------------- THIS IS QUESTION CREATOR SECTION PAGE:----------------------------------------'''

        '''MCQ Creator - parameter input : 
        number_of_question = 1 / 2 / 3, number_choices = 3 / 4 / 5
        # List of answer option for 3 choices answer is limited only A - C
        # List of answer option for 3 choices answer is limited only A - D
        # List of answer option for 3 choices answer is limited only A - E '''
        # create_question.create_mcq_question(
        #     3,
        #     3,
        #     "A")

        '''ESSAY Creator - parameter input : number_of_question = 1 / 2 / 3'''
        # create_question.create_essay_question(10)

        '''MCC Creator - Parameter Input : 
        # number_of_question= Masukkan Jumlah Soal MCC yang akan dibuat(bebas, format:angka)
        # number_choices = untuk saat ini hanya bisa input angka 3, 4, dan 5 
        # choose_correct_answer = Contoh penginputan -> ['A'] : untuk jawaban benar A, 
                                                        ['A','B'] utk jawaban benar A & B   
        # List of answer option for 3 choices answer is limited only A - C
        # List of answer option for 3 choices answer is limited only A - D
        # List of answer option for 3 choices answer is limited only A - E '''
        # create_question.create_mcc_question(
        #     2,
        #     5,
        #     ['E', 'A', 'C'])

        '''True/False Creator - parameter input :
                # number_of_question = 1 / 2 / 3
                # correct_answer = true / false (Case Sensitive) '''
        # create_question.create_truefalse_question(3, "false")

        '''Matching Creator - parameter input :
                # number_of_question = 1 / 2 / 3
                # number_of_question = 3 / 4 / 5 '''
        create_question.create_matching_question(2, 3)

        '''Matching Creator - parameter input :
                # number_of_question = 1 / 2 / 3
                # question_text = input any question
                # answer_text = Answer or Answer1|Answer2|Answer3 (for multiple answer)'''
        # create_question.create_short_answer_question(
        #     10,
        #     "Pertanyaan",
        #     "Jawaban1|Jawaban2|Jawaban3")

        '''--------------------- END OF QUESTION CREATOR SECTION PAGE:----------------------------------------'''

        create_question.click_publish_btn()
        assessment_assertion.do_verify_assessment_created_successfully_teacher()
        logout.do_logout()
        assessment_assertion.do_verify_assessment_created_successfully_student()

        time.sleep(5)
