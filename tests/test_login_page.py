from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestStellarBurgersLogin:
    def test_login_from_button_login_to_account_correct_input_logged_in(self, driver):
        driver.find_element(*Locators.SIGN_TO_ACCOUNT_BTN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BTN).click()
        flag = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE)).text
        assert flag == "Соберите бургер"

    def test_login_from_button_personal_account_correct_input_logged_in(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BTN).click()
        flag = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE)).text
        assert flag == "Соберите бургер"

    def test_login_from_registration_page_correct_input_logged_in(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*Locators.SIGN_UP_LINK).click()
        driver.find_element(*Locators.SIGN_IN_LINK).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BTN).click()
        flag = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE)).text
        assert flag == "Соберите бургер"
