from data import Person, RandomData
from locators import RegistrationPageLocators, AuthPageLocators
from urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationPage:

    def test_registration_success(self, driver):
        """Проверка регистрации пользователя"""
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomData.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()

        assert (
            driver.current_url == URLS.AUTH_PAGE_URL
            and WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(AuthPageLocators.login_account_btn)
            )
        )

    def test_registration_incorrect_password_check_error(self, driver):
        """Проверка регистрации пользователя с некорректным паролем (менее 6 символов)"""
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(12345)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()

        assert (
            driver.current_url == URLS.REG_PAGE_URL
            and WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(RegistrationPageLocators.error_message_incorrect_password)
            )
        )

    def test_double_registration_check_error(self, driver):
        """Проверка повторной регистрации пользователя"""
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()

        assert (
            driver.current_url == URLS.REG_PAGE_URL
            and WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(RegistrationPageLocators.error_message_double_reg)
            )
        )