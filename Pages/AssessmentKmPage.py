from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.BaseMethod import MyGenericMethods
from datetime import datetime, timedelta, date


class AssessmentKM(MyGenericMethods):

    """Locators Assessment page"""
    LOC_DISSMISS_DROPDOWN = (By.XPATH, '//label[contains(.,"Semester")]')
    LOC_ASSESMENT_PAGE_TITLE = (By.XPATH, '//span[@class=" active"]')
    LOC_GRADE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="da-teacher-dropdown-toggle"]')
    LOC_GRADE_COURSE_LIST = (By.XPATH, '//div[@class="teacher-gss-dropdown-menu dropdown-menu show"]/div')
    LOC_ASSESSMENT_CATEGORY_DROPDOWN = (By.XPATH, '//div[@class="form-group"][3]//select[@id="inputState"]')
    LOC_SEMESTER_LIST_DROPDOWN = (By.XPATH, '//div[@class="form-group"][4]//select[@id="inputState"]')
    LOC_REPLACEMENT_ASSESSMENT_TOGGLE = (By.XPATH, '//input[@id="replacement"]/parent::li//label[@for="replacement"]')
    LOC_DEADLINE_FIELD = (By.XPATH, '//input[@class="form-control"]')
    LOC_SET_TIME_DEADLINE_BTN = (By.XPATH, '//td[@class="rdtTimeToggle"]')
    LOC_INCREASE_HOUR_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[1]//span[@class="rdtBtn"][1]')
    LOC_DECREASE_HOUR_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[1]//span[@class="rdtBtn"][2]')
    LOC_INCREASE_MINUTES_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[3]//span[@class="rdtBtn"][1]')
    LOC_DECREASE_MINUTES_BTN = (By.XPATH, '//div[@class="rdtCounters"]/div[3]//span[@class="rdtBtn"][2]')
    LOC_TITLE_INPUT_FIELD = (By.XPATH, '//input[@id="titleIB"]')
    LOC_CATEGORY_DROPDOWN_FIELD = (By.XPATH, '//form[@class="pr-2 creation-field"]/div[4]/select[@id="inputState"]')
    LOC_SESSION_SETTING_TOGGLE = (By.XPATH, '//input[@id="session_switch"]/parent::li//label[@for="session_switch"]')
    LOC_POSTTO_DROPDOWN_FIELD = (By.XPATH, '//label[@for="inputState"]/following-sibling::div[@id="videoSelection"]')
    LOC_POSTTO_DROPDOWN_LIST = (By.XPATH, '//div[@class="dropdown-menu show dropdown-bottom"]/div')
    LOC_AUTOSUBMISSION_CHECKBOX = (By.XPATH, '//input[@id="autoSubmission"]/following-sibling::label[@for="autoSubmission"]')
    LOC_RESULT_POSTING_DATE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="form-group"][1]//select[@id="inputState"]')
    LOC_RESULT_TYPE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="form-group"][6]//select[@id="inputState"]')
    LOC_SUBMISSION_TYPE_TOGGLE = (By.XPATH, '//input[@id="switch"]/following-sibling::label[@class="toggle-switch"]')
    LOC_ANTICHEAT_CHECKBOX = (By.XPATH, '//input[@id="antiCheatFeatureCheckbox"]/following-sibling::label[@for="antiCheatFeatureCheckbox"]')
    LOC_ASSESSMENT_TIME_LIMIT_CHECKBOX = (By.XPATH, '//input[@id="customCheck1"]/following-sibling::label[@class="custom-control-label label-time-limits"]')
    LOC_ASSESSMENT_TIME_LIMIT_FIELD = (By.XPATH, '//input[@id="minsPlaceholder" and @name="timeLimit"]')
    LOC_ACCESS_CAMERA_CHECKBOX = (By.XPATH, '//input[@id="accessCameraCheckbox"]/following-sibling::label[@for="accessCameraCheckbox"]')
    LOC_PUBLISH_SCHEDULE_DROPDOWN_FIELD = (By.XPATH, '//div[@class="mt-3 form-row"]//select[@id="inputState"]')
    LOC_SHUFFLE_QUESTION_CHECKBOX = (By.XPATH, '//input[@id="customCheck2"]/following-sibling::label[@for="customCheck2"]')
    LOC_TEXT_EDITOR_FRAME = (By.XPATH, '//iframe[1]')
    LOC_INSTRUCTION_TEXT_FIELD = (By.XPATH, '//body[@id="tinymce"]')
    LOC_CREATE_QUESTION_BTN = (By.XPATH, '//div[@class="btn btn-assessment-create-question btn-primary font-weight-semibold"]')
    LOC_CANCEL_CREATE_ASSESSMENT_BTN = (By.XPATH, '//div[@class="mr-3 btn btn-assessment-cancel btn-outline-secondary font-weight-semibold"]')
    LOC_QUESTION_NEW_BTN = (By.XPATH, '//button[@class="btn add-q "]')
    LOC_QUESTION_TEST_BANK_BTN = (By.XPATH, '//button[@class="btn test-b "]')
    LOC_QUESTION_UPLOAD_BTN = (By.XPATH, '//button[@class="btn upld-q "]')
    LOC_NEXT_CREATE_QUESTION_BTN = (By.XPATH, '//button[@class="btn btn-primary ml-auto font-weight-semibold"]')

    def LOC_DATE_PICKER(self, day, month, year):
        locators = (By.XPATH, '//td[@data-value="'+day+'" and @data-month="'+month+'" and @data-year="'+year+'"]')
        return locators

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def do_verify_create_assessment_page(self, input_page_title):
        create_assessment_page_title = self.get_element_text(self.LOC_ASSESMENT_PAGE_TITLE)
        assert input_page_title in create_assessment_page_title, "Verify title page tidak sesuai!"
        print("Success Go To Create Assessment Page")

    def choose_grade_course(self, input_grade_course):
        self.click_to(self.LOC_GRADE_DROPDOWN_FIELD)
        ele = self.get_elements_text(self.LOC_GRADE_COURSE_LIST)
        for i in ele:
            if i.text == input_grade_course:
                self.click_to(i)
                break

    def set_replacement_assessment(self):
        self.click_to(self.LOC_REPLACEMENT_ASSESSMENT_TOGGLE)

    def input_title(self, input_title):
        self.sendkeys_to(self.LOC_TITLE_INPUT_FIELD, input_title)

    def choose_assessment_category(self, input_formative_or_summative):
        dropdown = Select(self.find_element(self.LOC_ASSESSMENT_CATEGORY_DROPDOWN))   # Select(self.LOC_ASSESMENT_CATEGORY)
        dropdown.select_by_value(input_formative_or_summative)

    def set_semester(self, input_semester):
        dropdown = Select(self.find_element(self.LOC_SEMESTER_LIST_DROPDOWN))
        dropdown.select_by_value(input_semester)

    def set_multi_session(self):
        self.click_to(self.LOC_SESSION_SETTING_TOGGLE)

    def set_post_to(self, class_name):
        self.click_to(self.LOC_POSTTO_DROPDOWN_FIELD)

        ele = self.get_elements_text(self.LOC_POSTTO_DROPDOWN_LIST)
        for i in ele:
            for x in class_name:
                if i.text == x:
                    self.click_to(i)
                    break

        self.click_to(self.LOC_DISSMISS_DROPDOWN)


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

        self.click_to(self.LOC_DISSMISS_DROPDOWN)

    """END OF SET DEADLINE FUNCTION"""

    def set_autosubmission_on(self):
        self.click_to(self.LOC_AUTOSUBMISSION_CHECKBOX)

    def set_post_result_time_dropdown_list(self, post_time_option):
        dropdown = Select(self.find_element(self.LOC_RESULT_POSTING_DATE_DROPDOWN_FIELD))
        dropdown.select_by_value(post_time_option)

    def set_result_type_dropdown_list(self, result_type):
        dropdown = Select(self.find_element(self.LOC_RESULT_TYPE_DROPDOWN_FIELD))
        dropdown.select_by_value(result_type)
        self.click_to(self.LOC_DISSMISS_DROPDOWN)

    def set_offline_submission_type(self):
        self.click_to(self.LOC_SUBMISSION_TYPE_TOGGLE)

    def set_time_limit(self, input_minutes_time_limit):
        self.click_to(self.LOC_ASSESSMENT_TIME_LIMIT_CHECKBOX)
        self.clear_field(self.LOC_ASSESSMENT_TIME_LIMIT_FIELD)
        self.sendkeys_to(self.LOC_ASSESSMENT_TIME_LIMIT_FIELD, int(input_minutes_time_limit))

    def set_anticheat_on(self):
        self.click_to(self.LOC_ANTICHEAT_CHECKBOX)

    def set_access_camera_off(self):
        self.click_to(self.LOC_ACCESS_CAMERA_CHECKBOX)

    def set_publish_schedule(self, publish_schedule):
        self.move_to_element(self.LOC_PUBLISH_SCHEDULE_DROPDOWN_FIELD)
        dropdown = Select(self.find_element(self.LOC_PUBLISH_SCHEDULE_DROPDOWN_FIELD))
        dropdown.select_by_value(publish_schedule)

    def set_shuffle_question_on(self):
        self.click_to(self.LOC_SHUFFLE_QUESTION_CHECKBOX)

    def input_instruction(self, input_instruction):
        self.switch_frame(self.LOC_TEXT_EDITOR_FRAME)
        self.sendkeys_to(self.LOC_INSTRUCTION_TEXT_FIELD, input_instruction)
        self.switch_to_default_frame()

    def cancel_create_assessment(self):
        self.click_to(self.LOC_CANCEL_CREATE_ASSESSMENT_BTN)
        self.accept_alert()

    def click_create_question_new(self):  # Function for create question with create new question option
        self.click_to(self.LOC_CREATE_QUESTION_BTN)
        self.click_to(self.LOC_QUESTION_NEW_BTN)
        self.click_to(self.LOC_NEXT_CREATE_QUESTION_BTN)

    def click_create_question_test_bank(self):  # Function for create question from test bank option
        self.click_to(self.LOC_CREATE_QUESTION_BTN)
        self.click_to(self.LOC_QUESTION_TEST_BANK_BTN)
        self.click_to(self.LOC_NEXT_CREATE_QUESTION_BTN)

    def click_create_question_upload(self):  # Function for create question using upload question file option
        self.click_to(self.LOC_CREATE_QUESTION_BTN)
        self.click_to(self.LOC_QUESTION_UPLOAD_BTN)
        self.click_to(self.LOC_NEXT_CREATE_QUESTION_BTN)