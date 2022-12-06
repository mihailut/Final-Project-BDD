from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Basepage


class Sign_Up_Page(Basepage):
    SIGN_UP_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[4]/a')
    PERSON_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/label/span[2]/span')
    CONTINUE_BUTTON1 = (By.XPATH, '(//button[@type="button"])[2]')
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
    MESSAGE_EMAIL_INPUT = (By.XPATH, f'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')

    def navigate_to_sign_up_page(self):
        self.chrome.get("https://jules.app/sign-up")

    def click_sign_up_button(self):
        self.chrome.find_element(*self.SIGN_UP_BUTTON).click()

    def select_person(self):
        self.chrome.find_element(*self.PERSON_BUTTON).click()
        sleep(1)

    def click_continue_button1(self):
        self.wait_for_elem(*self.CONTINUE_BUTTON1)
        self.chrome.find_element(*self.CONTINUE_BUTTON1).click()
        sleep(1)

    def set_first_name(self, first_name):
        self.wait_for_elem(*self.FIRST_NAME_INPUT)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        sleep(0.5)
        self.chrome.find_element(*self.FIRST_NAME_INPUT).send_keys(Keys.ENTER)
        sleep(1)

    def set_last_name(self, last_name):
        self.wait_for_elem(*self.LAST_NAME_INPUT)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        sleep(0.5)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys(Keys.ENTER)
        sleep(1)

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def verify_display_invalid_email(self):
        actual = self.chrome.find_element(By.XPATH,
                                          f'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p').is_displayed()
        if actual:
            print(f'The email is incorrect !')
        else:
            print(f'The email is correct and the wrong email message is not displayed!')

    def complete_correct_email(self, email_correct):
        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element
                                                     ((By.XPATH, f'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p'),
                                                      "Please enter a valid email address."))
        if actual:
            email_input = self.chrome.find_element(*self.EMAIL_INPUT)
            email_input.send_keys(Keys.CONTROL + 'a')
            email_input.send_keys(Keys.BACKSPACE)
            self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email_correct)
        else:
            print(f'The email is correct and the wrong email message is not displayed!')

    def verify_display_invalid_email1(self):
        elem = self.chrome.find_elements(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')
        if len(elem) > 0:
            print('Message exists')
        else:
            print('Message do not exists')

    def verify_url_message(self):
        self.verify_url_sign_up()