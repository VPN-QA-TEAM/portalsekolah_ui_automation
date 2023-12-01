from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.BaseMethod import MyGenericMethods
from datetime import datetime, timedelta, date
import time


class AssessmentKM(MyGenericMethods):

    """Locators Assessment page"""
    LOC_ASSESMENT_PAGE_TITLE = (By.XPATH, '//span[@class=" active"]')

    LOC_GRADE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="da-teacher-dropdown-toggle"]')
    LOC_GRADE_COURSE_LIST = (By.XPATH, '//div[@class="teacher-gss-dropdown-menu dropdown-menu show"]/div')
    LOC_ASSESMENT_CATEGORY = (By.ID, "inputState")
    LOC_REPLACEMENT_ASSESSMENT_TOGGLE = (By.XPATH, '//input[@id="replacement"]/parent::li//label[@for="replacement"]')
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

    LOC_SESSION_SETTING_TOGGLE = (By.XPATH, '//input[@id="session_switch"]/parent::li//label[@for="session_switch"]')

    LOC_SEMESTER_DROPDOWN_FIELD = (By.XPATH, '//form[@class="pr-2 creation-field"]/div[5]/select[@id="inputState"]')
    def LOC_SEMESTER_DROPDOWN_LIST(self, semester):
        locators = (By.XPATH, '//select[@id="inputState"]//option[@value="'+semester+'"]')
        return locators

    LOC_POSTTO_DROPDOWN_FIELD = (By.XPATH, '//label[@for="inputState"]/following-sibling::div[@id="videoSelection"]')
    def LOC_POSTTO_DROPDOWN_LIST(self, class_name):
        locators = (By.XPATH, '//div[@class="dropdown-item "]//span[.="'+class_name+'"]')
        return locators

    LOC_AUTOSUBMISSION_CHECKBOX = (By.XPATH, '//input[@id="autoSubmission"]')

    LOC_RESULT_POSTING_DATE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="mb-0 form-row"]//select[@id="inputState"]')
    def LOC_RESULT_POSTING_DATE_DROPDOWN_LIST(self, post_time_option):
        locators = (By.XPATH, '//option[@value="'+post_time_option+'"]')
        return locators

    LOC_RESULT_TYPE_DROPDOWN_FIELD = (By.XPATH, '//form[@class="pr-2 creation-field"]/div[11]/select[@id="inputState"]')
    def LOC_RESULT_TYPE_DROPDOWN_LIST(self, result_type):
        locators = (By.XPATH, '//select[@id="inputState"]//option[@value="'+result_type+'"]')
        return locators

    LOC_SUBMISSION_TYPE_TOGGLE = (By.XPATH, '//input[@id="switch"]/following-sibling::label[@class="toggle-switch"]')

    def LOC_DATE_PICKER(self, day, month, year):
        locators = (By.XPATH, '//td[@data-value="'+day+'" and @data-month="'+month+'" and @data-year="'+year+'"]')
        return locators

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def do_verify_create_assessment_page(self, input_page_title):
        create_assessment_page_title = self.get_element_text(self.LOC_ASSESMENT_PAGE_TITLE)
        assert input_page_title in create_assessment_page_title, "Verify title page tidak sesuai!"
        print(create_assessment_page_title)

    def choose_grade_course(self, input_grade_course):
        self.click_to(self.LOC_GRADE_DROPDOWN_FIELD)
        for i in self.get_elements_text(self.LOC_GRADE_COURSE_LIST):
            if i == input_grade_course:
                self.click_to(i)

    def set_replacement_assessment(self):
        self.click_to(self.LOC_REPLACEMENT_ASSESSMENT_TOGGLE)

    def input_title(self, input_title):
        self.sendkeys_to(self.LOC_TITLE_INPUT_FIELD, input_title)

    '''Update dari miftah utk handle dropdown select'''
    def choose_assessment_category(self, input_formative_or_summative):
        dropdown = Select(self.find_element(self.LOC_ASSESMENT_CATEGORY))   # Select(self.LOC_ASSESMENT_CATEGORY)
        dropdown.select_by_value(input_formative_or_summative)

    def set_semester(self, semester):
        self.click_to(self.LOC_SEMESTER_DROPDOWN_FIELD)
        self.click_to(self.LOC_SEMESTER_DROPDOWN_LIST(semester))

    def set_multi_session(self):
        self.click_to(self.LOC_SESSION_SETTING_TOGGLE)

    def set_post_to(self, class_name):
        self.click_to(self.LOC_POSTTO_DROPDOWN_FIELD)
        self.click_to(self.LOC_POSTTO_DROPDOWN_LIST(class_name))


    """SET DEADLINE FUNCTION"""

    def set_date_plus_deadline(self, increment):
        self.click_to(self.LOC_DEADLINE_FIELD)
        today_date = date.today()
        get_day = str(int(today_date.strftime("%d")) + int(increment))
        get_month = str(int(today_date.strftime("%m")) - 1)
        get_year = today_date.strftime("%Y")
        self.click_to(self.LOC_DATE_PICKER(get_day, get_month, get_year))

    def set_date_minus_deadline(self, decrement):
        self.click_to(self.LOC_DEADLINE_FIELD)
        today_date = date.today()
        get_day = str(int(today_date.strftime("%d")) - int(decrement))
        get_month = str(int(today_date.strftime("%m")) - 1)
        get_year = today_date.strftime("%Y")
        self.click_to(self.LOC_DATE_PICKER(get_day, get_month, get_year))

    def set_today_time_plus_deadline(self, increment):
        self.click_to(self.LOC_DEADLINE_FIELD)
        get_current_time = datetime.now()
        get_time_plus = get_current_time + timedelta(minutes=int(increment))
        get_hour = int(get_time_plus.strftime("%H"))
        get_minutes = int(get_time_plus.strftime("%M"))

        self.click_to(self.LOC_SET_TIME_DEADLINE_BTN)

        for x in range(get_hour):
            self.click_to(self.LOC_INCREASE_HOUR_BTN)
        for x in range(get_minutes):
            self.click_to(self.LOC_INCREASE_MINUTES_BTN)

    def set_today_time_minus_deadline(self, decrement):
        self.click_to(self.LOC_DEADLINE_FIELD)
        get_current_time = datetime.now()
        get_time_plus = get_current_time - timedelta(minutes=int(decrement))
        get_hour = int(get_time_plus.strftime("%H"))
        get_minutes = int(get_time_plus.strftime("%M"))

        self.click_to(self.LOC_SET_TIME_DEADLINE_BTN)

        for x in range(get_hour):
            self.click_to(self.LOC_INCREASE_HOUR_BTN)
        for x in range(get_minutes):
            self.click_to(self.LOC_INCREASE_MINUTES_BTN)

    def set_date_time_deadline(self, date_increment, hour, minute):
        self.click_to(self.LOC_DEADLINE_FIELD)

        today_date = date.today()
        get_day = str(int(today_date.strftime("%d")) + int(date_increment))
        get_month = str(int(today_date.strftime("%m")) - 1)
        get_year = today_date.strftime("%Y")
        self.click_to(self.LOC_DATE_PICKER(get_day, get_month, get_year))

        self.click_to(self.LOC_SET_TIME_DEADLINE_BTN)

        for x in range(int(hour)):
            self.click_to(self.LOC_INCREASE_HOUR_BTN)
        for x in range(int(minute)):
            self.click_to(self.LOC_INCREASE_MINUTES_BTN)

    """END OF SET DEADLINE FUNCTION"""

    def set_autosubmission_on(self):
        self.click_to(self.LOC_AUTOSUBMISSION_CHECKBOX)

    def set_post_result_time_dropdown_list(self, post_time_option):
        self.click_to(self.LOC_RESULT_POSTING_DATE_DROPDOWN_FIELD)
        self.click_to(self.LOC_RESULT_POSTING_DATE_DROPDOWN_LIST(post_time_option))

    def set_result_type_dropdown_list(self, result_type):
        self.click_to(self.LOC_RESULT_TYPE_DROPDOWN_FIELD)
        self.click_to(self.LOC_RESULT_TYPE_DROPDOWN_LIST(result_type))

    def set_submission_type(self):
        self.click_to(self.LOC_SUBMISSION_TYPE_TOGGLE)

    def set_assessment_time_limit(self, time_limit):
        self.click_to(self.LOC_ASSESSMENT_TIME_LIMIT_CHECKBOX)
        self.clear_field(self.LOC_ASSESSMENT_TIME_LIMIT_INPUT_FIELD)
        self.sendkeys_to(self.LOC_ASSESSMENT_TIME_LIMIT_INPUT_FIELD, time_limit)

    def set_distribution_schedule(self, distribution_schedule):
        self.click_to(self.LOC_DISTRIBUTION_DROPDOWN_FIELD)
        self.click_to(self.LOC_DISTRIBUTION_DROPDOWN_LIST(distribution_schedule))

    def input_instruction(self, input_instruction):
        self.click_to(self.LOC_INSTRUCTION_FIELD)
        self.sendkeys_to(self.LOC_INSTRUCTION_FIELD, input_instruction)