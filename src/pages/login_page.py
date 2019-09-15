from .base_page import BasePage

class LoginPage(BasePage):
    
    EMAIL_CONTAINER = "email"
    PASSWORD_CONTAINER = "password"
    LOGIN_BUTTON = "//button[@type='submit']"

    def start(self):
        self.url = "/signin"
        self.load(self.url)

    def login(self, email, password):
        self.send_text_by_id(LoginPage.EMAIL_CONTAINER, email)
        self.send_text_by_id(LoginPage.PASSWORD_CONTAINER, password)
        self.click_button(LoginPage.LOGIN_BUTTON)
    