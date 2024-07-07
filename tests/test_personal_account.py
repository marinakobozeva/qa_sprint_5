from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

class TestStellarBurgersPersonalAccount:

    def test_go_to_personal_account_from_main_page_not_registred_moved(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        current_url = driver.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_go_to_to_personal_account_from_main_page_registred_moved(self, driver):
        driver.find_element(*Locators.SIGN_TO_ACCOUNT_BTN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BTN).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_LINK)).click()
        current_url = driver.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_to_go_to_constructor_from_personal_account_page_moved(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*Locators.CONSTRUCTOR_BTN).click()
        current_url = driver.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_on_logo_from_personal_account_page_moved(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*Locators.LOGO_BTN).click()
        current_url = driver.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/"


