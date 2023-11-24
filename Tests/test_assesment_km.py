import pytest
from Config.dataconfig import TestData
from Pages.LoginPage import Login
from Pages.DashboardPage import Dashboard
from Pages.AssessmentKmPage import AssessmentKM
import time

@pytest.mark.usefixtures("setup_scope_function")
class TestAssessmentKM:

    @pytest.mark.smoke
    def test_tc_km01(self):
        login = Login(self.driver)
        login.do_login(TestData.USERID_TEACHER_K13, TestData.VALID_PASSWORD)
        dashboard = Dashboard(self.driver)
        dashboard.is_modal_email_after_login_visible()
        dashboard.click_assesment_sidebars_btn()
        assessment_km = AssessmentKM(self.driver)
        assessment_km.do_verify_create_assessment_page("Buat Penilaian")
        assessment_km.click_grade_dropdown_field()

