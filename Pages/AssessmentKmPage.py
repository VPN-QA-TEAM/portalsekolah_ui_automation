from selenium.webdriver.common.by import By
from Pages.BaseMethod import MyGenericMethods
from datetime import datetime, timedelta, date
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
    LOC_TITLE_INPUT_FIELD = (By.XPATH, '//input[@id="titleIB"]')

    LOC_CATEGORY_DROPDOWN_FIELD = (By.XPATH, '//form[@class="pr-2 creation-field"]/div[4]/select[@id="inputState"]')
    def LOC_CATEGORY_DROPDOWN_LIST(self, assessment_category):
        locators = (By.XPATH, '//select[@id="inputState"]//option[@value="'+assessment_category+'"]')
        return locators

    LOC_SEMESTER_DROPDOWN_FIELD = (By.XPATH, '//form[@class="pr-2 creation-field"]/div[5]/select[@id="inputState"]')
    def LOC_SEMESTER_DROPDOWN_LIST(self, semester):
        locators = (By.XPATH, '//select[@id="inputState"]//option[@value="'+semester+'"]')
        return locators

    LOC_POSTTO_DROPDOWN_FIELD = (By.XPATH, '//label[@for="inputState"]/following-sibling::div[@id="videoSelection"]')
    def LOC_POSTTO_DROPDOWN_LIST(self, class_name):
        locators = (By.XPATH, '//div[@class="dropdown-item "]//span[.="'+class_name+'"]')
        return locators

    def LOC_DATE_PICKER(self, day, month, year):
        locators = (By.XPATH, '//td[@data-value="'+day+'" and @data-month="'+month+'" and @data-year="'+year+'"]')
        return locators

    LOC_RESULT_POSTING_DATE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="mb-0 form-row"]//select[@id="inputState"]')
    def LOC_RESULT_POSTING_DATE_DROPDOWN_LIST(self, post_time_option):
        locators = (By.XPATH, '//option[@value="'+post_time_option+'"]')
        return locators

    LOC_RESULT_TYPE_DROPDOWN_FIELD = (By.XPATH, '//form[@class="pr-2 creation-field"]/div[11]/select[@id="inputState"]')
    def LOC_RESULT_TYPE_DROPDOWN_LIST(self, result_type):
        locators = (By.XPATH, '//select[@id="inputState"]//option[@value="'+result_type+'"]')
        return locators

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def do_verify_create_assessment_page(self, input_page_title):
        create_assessment_page_title = self.get_element_text(self.LOC_ASSESMENT_PAGE_TITLE)
        assert input_page_title in create_assessment_page_title, "Verify title page tidak sesuai!"
        print(create_assessment_page_title)

    def choose_grade_dropdown_list(self, input_grade):
        self.click_to(self.LOC_GRADE_DROPDOWN_FIELD)
        self.click_to(self.LOC_GRADE_DROPDOWN_LIST(input_grade))

    def input_title(self, input_title):
        self.sendkeys_to(self.LOC_TITLE_INPUT_FIELD, input_title)

    def set_assessment_category(self, assessment_category):
        self.click_to(self.LOC_CATEGORY_DROPDOWN_FIELD)
        self.click_to(self.LOC_CATEGORY_DROPDOWN_LIST(assessment_category))

    def set_semester(self, semester):
        self.click_to(self.LOC_SEMESTER_DROPDOWN_FIELD)
        self.click_to(self.LOC_SEMESTER_DROPDOWN_LIST(semester))

    def set_post_to(self, class_name):
        self.click_to(self.LOC_POSTTO_DROPDOWN_FIELD)
        self.click_to(self.LOC_POSTTO_DROPDOWN_LIST(class_name))

    def click_deadline_field(self):
        self.click_to(self.LOC_DEADLINE_FIELD)

    def set_plus1_date_deadline(self):
        today_date = date.today()
        get_day = str(int(today_date.strftime("%d")) + 1)
        get_month = str(int(today_date.strftime("%m")) - 1)
        get_year = today_date.strftime("%Y")
        self.click_to(self.LOC_DATE_PICKER(get_day, get_month, get_year))

    def set_plus2_date_deadline(self):
        today_date = date.today()
        get_day = str(int(today_date.strftime("%d")) + 2)
        get_month = str(int(today_date.strftime("%m")) - 1)
        get_year = today_date.strftime("%Y")
        self.click_to(self.LOC_DATE_PICKER(get_day, get_month, get_year))

    def set_min1_date_deadline(self):
        today_date = date.today()
        get_day = str(int(today_date.strftime("%d")) - 1)
        get_month = str(int(today_date.strftime("%m")) - 1)
        get_year = today_date.strftime("%Y")
        self.click_to(self.LOC_DATE_PICKER(get_day, get_month, get_year))

    def set_min2_date_deadline(self):
        today_date = date.today()
        get_day = str(int(today_date.strftime("%d")) - 2)
        get_month = str(int(today_date.strftime("%m")) - 1)
        get_year = today_date.strftime("%Y")
        self.click_to(self.LOC_DATE_PICKER(get_day, get_month, get_year))

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

    def set_post_result_time_dropdown_list(self, post_time_option):
        self.click_to(self.LOC_RESULT_POSTING_DATE_DROPDOWN_FIELD)
        self.click_to(self.LOC_RESULT_POSTING_DATE_DROPDOWN_LIST(post_time_option))

    def set_result_type_dropdown_list(self, result_type):
        self.click_to(self.LOC_RESULT_TYPE_DROPDOWN_FIELD)
        self.click_to(self.LOC_RESULT_TYPE_DROPDOWN_LIST(result_type))