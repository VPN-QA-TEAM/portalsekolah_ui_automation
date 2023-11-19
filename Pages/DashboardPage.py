from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods

class Dashboard(MyGenericMethods):

    """Locators Dashboard page"""
    LOC_WELCOME = (By.XPATH, '//div[@class="pageHeading"]/p/em')
    LOC_MODAL_INPUT_EMAIL = (By.XPATH, '//div[@class="modal-content email-change-modal"]')
    LOC_BTN_LEWATI_ON_MODAL = (By.XPATH, '//button[text()="Lewati sekarang"]')

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
            # Wait for the modal to be visble
            self.is_visible(self.LOC_MODAL_INPUT_EMAIL)

            # If modal is visible, click the "Lewati" button
            self.click_to(self.LOC_BTN_LEWATI_ON_MODAL)
            self.do_verify_welcome_text("Selamat datang")
        except:
            self.do_verify_welcome_text("Selamat datang")
            print("modal input email tidak muncul")

