import time

from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods

class Dashboard(MyGenericMethods):

    """Locators Dashboard page"""
    LOC_WELCOME = (By.XPATH, '//div[@class="pageHeading"]/p/em')
    LOC_MODAL_INPUT_EMAIL = (By.XPATH, '//div[@class="modal-content email-change-modal"]')
    LOC_BTN_LEWATI_ON_MODAL = (By.XPATH, '//button[.="Lewati sekarang"]')
    LOC_BTN_ASSESMENT_SIDEBAR = (By.XPATH, '//li[@class="menu-item icon-ujian"]')
    LOC_CREATE_ASSESMENT_DROPDOWN = (By.XPATH, '//div[@class="pr-icon icon-add-assessment"]/parent::div[@class="profile-left"]')

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    '''Verify Function : Welcome text'''
    def do_verify_welcome_text(self, input_validation_message):
        welcome_text = self.get_element_text(self.LOC_WELCOME)
        assert input_validation_message in welcome_text, "Gagal nih! welcome text beda!"
        print(welcome_text)

    def is_modal_email_after_login_visible(self):
        try:
            self.is_visible(self.LOC_MODAL_INPUT_EMAIL)
            self.click_to(self.LOC_BTN_LEWATI_ON_MODAL)
            self.do_verify_welcome_text("Selamat datang,")
        except:
            self.do_verify_welcome_text("Selamat datang,")

    def click_sidebar_assessment_menu(self):
        self.scroll_down_page()
        time.sleep(0.5)
        self.click_to(self.LOC_BTN_ASSESMENT_SIDEBAR)
        self.click_to(self.LOC_CREATE_ASSESMENT_DROPDOWN)

