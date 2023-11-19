import pytest
from Config.dataconfig import TestData
from Pages.LoginPage import Login
from Pages.DashboardPage import Dashboard

@pytest.mark.usefixtures("setup_scope_function")
class TestAssessmentKM:

    def test_tc_km01(self):
        login = Login(self.driver)
        login.do_login(TestData.USERID_TEACHER_K13, TestData.VALID_PASSWORD)
        dashboard = Dashboard(self.driver)
        dashboard.is_modal_email_after_login_visible()
        pass
    
