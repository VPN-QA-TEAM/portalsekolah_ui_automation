from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
from datetime import datetime, timedelta
import time

class AssessmentKM(MyGenericMethods):

    """Locators Assessment page"""
    LOC_ASSESMENT_PAGE_TITLE = (By.XPATH, '//span[@class=" active"]')
    LOC_GRADE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="da-teacher-dropdown-toggle"]')

    def LOC_GRADE_DROPDOWN_LIST (self, input_grade):
        LOCATOR = (By.XPATH, '//div[@class="gss-values dropdown-item  dropdown-item" and .="'+input_grade+'"]')
        return LOCATOR

    LOC_DEADLINE_FIELD = (By.XPATH, '//input[@class="form-control"]')
    LOC_SET_TIME_DEADLINE_BTN = (By.XPATH, '//td[@class="rdtTimeToggle"]')
    LOC_INCREASE_HOUR_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[1]//span[@class="rdtBtn"][1]')
    LOC_DECREASE_HOUR_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[1]//span[@class="rdtBtn"][2]')
    LOC_INCREASE_MINUTES_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[3]//span[@class="rdtBtn"][1]')
    LOC_DECREASE_MINUTES_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[3]//span[@class="rdtBtn"][2]')

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def do_verify_create_assessment_page(self, input_page_title):
        create_assessment_page_title = self.get_element_text(self.LOC_ASSESMENT_PAGE_TITLE)
        assert input_page_title in create_assessment_page_title, "Verify title page tidak sesuai!"
        print(create_assessment_page_title)

    def click_grade_dropdown_field(self):
        self.click_to(self.LOC_GRADE_DROPDOWN_FIELD)
        time.sleep(2)

    def click_grade_dropdown_list(self, input_grade):
        self.click_to(self.LOC_GRADE_DROPDOWN_LIST(input_grade))

    def click_deadline_field(self):
        self.click_to(self.LOC_DEADLINE_FIELD)

    def click_set_time_deadline_btn(self):
        self.click_to(self.LOC_SET_TIME_DEADLINE_BTN)

    def click_increase_hour_btn(self):
        self.click_to(self.LOC_INCREASE_HOUR_BTN)

    def click_increase_minutes_btn(self):
        self.click_to(self.LOC_INCREASE_MINUTES_BTN)

    def set_time_deadline(self):
        get_current_time = datetime.now()
        get_time_plus_5_minutes = get_current_time + timedelta(minutes=5)
        get_hour = int(get_time_plus_5_minutes.strftime("%H"))
        get_minutes = int(get_time_plus_5_minutes.strftime("%M"))

        for x in range(get_hour):
            self.click_increase_hour_btn()

        for x in range(get_minutes):
            self.click_increase_minutes_btn()