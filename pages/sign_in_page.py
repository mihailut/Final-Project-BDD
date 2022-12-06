from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Basepage


# sectiune de identificare a elementelor
class Sign_In_Page(Basepage):
    EMAIL_INPUT = (By.XPATH, f'//input[@placeholder="Enter your email"]')
    PWD_INPUT = (By.XPATH, f'//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    FORGOT_PWD = (By.LINK_TEXT, "Forgot password?")
    MESSAGE_INPUT_CORRECT_PASS = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained"]')

    def navigate_to_sign_in_page(self):
        self.chrome.get("https://jules.app/sign-in")

    def set_email(self, email_correct):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email_correct)

    def set_pwd(self, pwd):
        self.chrome.find_element(*self.PWD_INPUT).send_keys(pwd)
        pwd_input = self.chrome.find_element(*self.PWD_INPUT)
        pwd_input.send_keys(Keys.CONTROL + 'a')
        pwd_input.send_keys(Keys.BACKSPACE)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def clik_forgot_pwd_link(self):
        self.chrome.find_element(*self.FORGOT_PWD).click()

    def verify_display_invalid_email(self):
        elem = self.chrome.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p')
        if len(elem) > 0:
            print('Message exists')
        else:
            print('Message do not exists')

    def verify_enable_button(self):
        button_login = self.chrome.find_element(By.XPATH, '//button[@type="submit"]').is_enabled()
        if button_login:
            print('Element is present')
        else:
            print('Element is not present')

    def verify_url_message(self):
        self.verify_url_sign_in()
