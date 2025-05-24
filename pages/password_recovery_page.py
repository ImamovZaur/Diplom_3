import allure
from locators.password_recovery_locator import *
from pages.base_page import BasePage
from data import login


class PasswordRecoveryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на кнопку Восстановление пароля')
    def click_recover_password(self):
        self.click_element(button_password_recovery)

    @allure.step('Ввод email в поле')
    def send_text_email(self):
        self.send_text(email_input_password_recovery, login)

    @allure.step('Нажимает на кнопку показать\скрыть пароль')
    def click_show_hide_button(self):
        self.click_element(show_hide_button)

    @allure.step('Нажимает на кнопку Восстановить')
    def click_recovery_button(self):
        self.click_element(recovery_button)

    @allure.step('Возвращает кнопку "Показать/Скрыть" пароль')
    def get_show_password(self):
        return self.browser.find_element(*password_field)