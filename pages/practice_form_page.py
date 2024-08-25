import os
from pages.base_page import BasePage

from pages.locators import PracticeFormPageLocators


class PracticeFormPage(BasePage):
    def fill_in_first_name_field(self, text):
        input_first_name = self.browser.find_element(*PracticeFormPageLocators.First_Name)
        input_first_name.send_keys(text)

    def fill_in_last_name_field(self, text):
        input_last_name = self.browser.find_element(*PracticeFormPageLocators.Last_Name)
        input_last_name.send_keys(text)

    def fill_in_email_field(self, text):
        input_email = self.browser.find_element(*PracticeFormPageLocators.Email)
        input_email.send_keys(text)

    def select_checkbox_gender(self):
        self.browser.find_element(*PracticeFormPageLocators.Gender).click()

    def fill_in_mobile_field(self, text):
        input_number = self.browser.find_element(*PracticeFormPageLocators.Mobile)
        input_number.send_keys(text)

    def fill_in_date_of_birth_field(self):
        self.browser.find_element(*PracticeFormPageLocators.Date_Of_Birth_Select).click()
        self.browser.find_element(*PracticeFormPageLocators.Date_Of_Birth_Year).click()
        self.browser.find_element(*PracticeFormPageLocators.Date_Of_Birth_Year_Select).click()
        self.browser.find_element(*PracticeFormPageLocators.Date_Of_Birth_Month).click()
        self.browser.find_element(*PracticeFormPageLocators.Date_Of_Birth_Month_Select).click()
        self.browser.find_element(*PracticeFormPageLocators.Date_Of_Birth).click()

    def fill_in_subjects_field(self, text):
        input_subjects = self.browser.find_element(*PracticeFormPageLocators.Subjects)
        input_subjects.send_keys(text)

    def upload_picture(self, path):
        input_picture = self.browser.find_element(*PracticeFormPageLocators.Picture)
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, path)
        input_picture.send_keys(file_path)

    def fill_in_current_address_field(self, text):
        input_current_address = self.browser.find_element(*PracticeFormPageLocators.Current_Address)
        input_current_address.send_keys(text)

    def submit_practice_form(self):
        self.browser.find_element(*PracticeFormPageLocators.Submit).click()

    def should_be_pop_up_window(self):
        assert self.browser.find_element(
            *PracticeFormPageLocators.Pop_Up_Window).text == "Thanks for submitting the form", "The practice form has not been sent"
