import pytest
from Config.dataconfig import TestData
from Pages.LoginPage import Login

@pytest.mark.usefixtures("setup_scope_function")
class TestLoginScenario:
    def test_login_teacher_wrong_password(self):
        login = Login(self.driver)
        login.do_login(TestData.USERID_TEACHER_K13, TestData.INVALID_PASSWORD)
        login.do_verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_login_teacher_success(self):
        login = Login(self.driver)
        login.do_login(TestData.USERID_TEACHER_K13, TestData.VALID_PASSWORD)
