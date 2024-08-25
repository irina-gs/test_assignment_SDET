from pages.practice_form_page import PracticeFormPage


def test_compliting_of_practice_form(browser):
    first_name = "Ivan"
    last_name = "Petrov"
    email = "name@example.com"
    mobile = "1234567890"
    subjects = "Maths"
    current_address = "Saransk"

    url = "https://demoqa.com/automation-practice-form"

    page = PracticeFormPage(browser, url)
    page.open()
    page.fill_in_first_name_field(first_name)
    page.fill_in_last_name_field(last_name)
    page.fill_in_email_field(email)
    page.select_checkbox_gender()
    page.fill_in_mobile_field(mobile)
    page.fill_in_date_of_birth_field()
    page.fill_in_subjects_field(subjects)
    page.upload_picture('data/picture.jpg')
    page.fill_in_current_address_field(current_address)
    page.submit_practice_form()
    page.should_be_pop_up_window()
