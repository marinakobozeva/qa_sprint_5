from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import Locators

fake_data = Faker("ru_RU")

class TestStellarBurgersRegistration:

    def test_registration_correct_input_registered(self, driver):
        user_name = fake_data.name()
        user_email = fake_data.email()
        user_password = "qwerty"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*Locators.SIGN_UP_LINK).click()
        driver.find_element(*Locators.INPUT_NAME).send_keys(user_name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user_password)
        driver.find_element(*Locators.SIGN_UP_BTN).click()
        flag = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SIGN_IN_TITLE)).text
        assert flag == "Вход"

    def test_registration_incorrect_input_not_registered(self, driver):
        user_name = fake_data.name()
        user_email = fake_data.email()
        user_password = "123"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*Locators.SIGN_UP_LINK).click()
        driver.find_element(*Locators.INPUT_NAME).send_keys(user_name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user_password)
        driver.find_element(*Locators.SIGN_UP_BTN).click()
        flag = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_WRONG_PASSWORD)).text
        assert flag == "Некорректный пароль"



