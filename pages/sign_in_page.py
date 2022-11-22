from selenium.webdriver.common.by import By
from pages.base_page import Basepage


# sectiune de identificare a elementelor
class Sign_In_Page(Basepage):
    EMAIL_INPUT = (By.XPATH, f'//input[@placeholder="Enter your email"]')
    PWD_INPUT = (By.XPATH, f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PWD = (By.LINK_TEXT, "Forgot password?")

    def navigate_to_sign_in_page(self):
        self.chrome.get('https://jules.app/')

    def set_email(self, email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_pwd(self, pwd):
        self.chrome.find_element(*self.PWD_INPUT).send_keys(pwd)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def clik_forgot_pwd_link(self):
        self.chrome.find_element(*self.FORGOT_PWD).click()

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://jules.app/sign-in'
        self.assertEqual(actual_url, expected_url, "The URL doesn't match")
