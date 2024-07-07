from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestStellarBurgersMenuScroll:

    def test_scroll_to_sauce_scrolled(self, driver):
        driver.find_element(*Locators.SAUCE_LINK).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(Locators.CURRENT_MENU_LINK, "Соусы"))

    def test_scroll_to_fillings_scrolled(self, driver):
        driver.find_element(*Locators.FILLINGS_LINK).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(Locators.CURRENT_MENU_LINK, "Начинки"))

    def test_scroll_to_buns_scrolled(self, driver):
        driver.find_element(*Locators.SAUCE_LINK).click()
        driver.find_element(*Locators.BUNS_LINK).click()
        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(Locators.CURRENT_MENU_LINK, "Булки"))