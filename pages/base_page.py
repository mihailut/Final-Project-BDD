from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class Basepage(Browser, unittest.TestCase):
    def wait_for_elem(self, by, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))

    def verify_url_sign_up(self):
        expected = "https://jules.app/sign-up"
        actual = self.chrome.current_url
        self.assertEqual(actual, expected, 'The Page is not open correct')

    def verify_url_sign_in(self):
        actual = self.chrome.current_url
        expected = "https://jules.app/sign-in"
        self.assertEqual(actual, expected, 'The Page is not open correct')