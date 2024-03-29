from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
