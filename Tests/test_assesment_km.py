import pytest
from Config.dataconfig import TestData
from Pages.LoginPage import Login
from Pages.DashboardPage import Dashboard
from Pages.AssessmentKmPage import AssessmentKM
import time


@pytest.mark.usefixtures("setup_scope_function")
class TestAssessmentKM:

    @pytest.mark.doing
    def test_tc_km01(self):
        login = Login(self.driver)
        dashboard = Dashboard(self.driver)
        assessment_km = AssessmentKM(self.driver)
        login.do_login(TestData.USERID_TEACHER_KM, TestData.VALID_PASSWORD)
        dashboard.is_modal_email_after_login_visible()
        dashboard.click_sidebar_assessment_menu()
        assessment_km.do_verify_create_assessment_page("Buat Penilaian")
        assessment_km.choose_grade_course("7-MERDEKA - Biologi 7KM")
        assessment_km.input_title(TestData.ASSESSMENT_TITLE)
        assessment_km.choose_assessment_category("formative")  # input category = formative / summative
        time.sleep(7)
        assessment_km.set_semester("1")  # semester = 1 / 2
        assessment_km.set_post_to("A - KM")  # class name : example = A - KM
        assessment_km.set_date_time_deadline(2, 10, 30)
        assessment_km.set_post_result_time_dropdown_list("manual")  # input time option = automatic_on_deadline / manual / scheduled
        assessment_km.set_result_type_dropdown_list("grade_with_submission_detail")  # result type input = grade_with_submission_detail / grade_only
        time.sleep(5)