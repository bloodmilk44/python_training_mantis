from selenium.webdriver.common.by import By
import re
import time


def extract_confirmation_url(text):
    return re.search('http://.*$', text, re.MULTILINE).group(0)


class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        self.app.driver.get(self.app.base_url + "/signup_page.php")
        self.app.driver.find_element(By.NAME, "username").send_keys(username)
        self.app.driver.find_element(By.NAME, "email").send_keys(email)
        self.app.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        time.sleep(3)
        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = extract_confirmation_url(mail)

        self.app.driver.get(url)
        self.app.driver.find_element(By.NAME, "password").send_keys(password)
        self.app.driver.find_element(By.NAME, "password_confirm").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, 'input[value="Update User"]').click()
