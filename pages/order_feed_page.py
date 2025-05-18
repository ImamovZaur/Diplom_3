import allure
from locators.order_feed_locator import *
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OrderFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на кнопку Лента заказов')
    def click_order_feed_button(self):
        self.click_element(order_feed_button)

    @allure.step('Получаем список всех заказов')
    def get_all_orders_number(self):
        order = self.find_elements(*number)
        for order_list in order:
            order_text = order_list.text
        return order_text

    @allure.step('Получаем количество всех заказов')
    def get_all_orders_count(self):
        return self.get_element_text(completed_all_time)

    @allure.step('Получаем количество заказов за сегодня')
    def get_today_orders_count(self):
        return self.get_element_text(completed_today)

    @allure.step('Получаем количество заказов в работе')
    def get_orders_in_work(self):
        return self.get_element_text(at_work)

    @allure.step('Нажимает а первый заказ')
    def click_first_order(self):
        self.click_element(order_history)

    @allure.step('Получаем окно с информацией о заказе')
    def get_order_popup(self):
        return self.find(popup_order_history)

    def wait_for_order_item(self, locator):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, locator)))