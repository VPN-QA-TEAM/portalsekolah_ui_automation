from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
from Config.dataconfig import TestData


class TeacherVerifyAssessment(MyGenericMethods):

    """Locators For Teacher Verify Assessment"""
    LOC_ASSESSMENT_PAGE_TITLE = (By.XPATH, '//span[@class="active"]')
    LOC_CLOSE_ASSESSMENT_TUTOR_MODAL = (By.XPATH, '//button[@title="Tutup"]')
    LOC_COMPLETED_ASSESSMENT_TAB = (By.XPATH, '//a[@href="#Completed"]')
    LOC_ASSESSMENT = (By.XPATH, '//div[@title="'+TestData.ASSESSMENT_TITLE+'"]')
    LOC_ASSESSMENT_TITLE = (By.XPATH, '//h5[@class="mt-0 font-weight-semibold text-label-dark-gray d-flex align-items-center"]')

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Function For Teacher Verify Assessment"""
    def verify_assessment_list_page(self):
        assessment_page_title = self.get_element_text(self.LOC_ASSESSMENT_PAGE_TITLE)
        assert "Penilaian" or "Assessment" in assessment_page_title, "Judul Halaman Tidak Sesuai"
        print("Success Go To Assessment Page")

    def teacher_choose_assessment_to_verify(self):
        try:
            self.click_to(self.LOC_CLOSE_ASSESSMENT_TUTOR_MODAL)
            self.click_to(self.LOC_ASSESSMENT)
        except AssertionError:
            self.click_to(self.LOC_ASSESSMENT)
        except:
            self.click_to(self.LOC_COMPLETED_ASSESSMENT_TAB)
            self.click_to(self.LOC_ASSESSMENT)




    def techer_verify_chosen_assessment_title(self):
        assessment_title = self.get_element_text(self.LOC_ASSESSMENT_TITLE)
        assert TestData.ASSESSMENT_TITLE in assessment_title, "Judul Assessment Beda Nih!!!"
        print("Oke! Judul Assessment Udah Bener")