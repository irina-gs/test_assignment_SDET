from selenium.webdriver.common.by import By


class PracticeFormPageLocators():
    First_Name = (By.ID, "firstName")
    Last_Name = (By.ID, "lastName")
    Email = (By.ID, "userEmail")
    Gender = (By.CSS_SELECTOR, "[for=gender-radio-1]")
    Mobile = (By.ID, "userNumber")
    Date_Of_Birth_Select = (By.ID, "dateOfBirthInput")
    Date_Of_Birth_Year = (By.CLASS_NAME, "react-datepicker__year-select")
    Date_Of_Birth_Year_Select = (By.CSS_SELECTOR, "[value='2000']")
    Date_Of_Birth_Month = (By.CLASS_NAME, "react-datepicker__month-select")
    Date_Of_Birth_Month_Select = (By.CSS_SELECTOR, "[value='1']")
    Date_Of_Birth = (By.XPATH, "//div[text()='1']")
    Subjects = (By.ID, "subjectsInput")
    Picture = (By.ID, "uploadPicture")
    Current_Address = (By.ID, "currentAddress")
    Submit = (By.ID, "submit")
    Pop_Up_Window = (By.ID, "example-modal-sizes-title-lg")
