import allure
from locators.personal_account_locator import *
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PersonalAccountPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на кнопку История заказов')
    def click_order_history_button(self):
        self.click_element(order_history_link)

    @allure.step('Нажимает на кнопку Выйти')
    def click_exit_button(self):
        self.click_element(exit_button)

    @allure.step('Ожидание загрузки заказов')
    def wait_order_load(self, locator):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Получение последнего заказа из истории')
    def get_last_order_number(self):
        return self.get_element_text(order_history_last_item)