from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestStellarBurgersLogout:
    def test_logout_logouted(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BTN).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SIGN_OUT_BTN)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SIGN_IN_TITLE))
        current_url = driver.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/login"