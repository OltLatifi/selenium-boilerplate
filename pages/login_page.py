from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "id_username")
    PASSWORD_INPUT = (By.ID, "id_password")
    LOGIN_BUTTON = (By.ID, "login_button")

    def enter_username(self, username: str):
        self.enter_text(*self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.enter_text(*self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_title(self):
        return self.driver.title
