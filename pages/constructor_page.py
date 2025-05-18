import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.constructor_locator import *
from locators.order_feed_locator import completed_all_time
from pages.base_page import BasePage
from pages.order_feed_page import OrderFeedPage
from urls import URL


class ConstructorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимает на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_element(constructor_button)

    @allure.step('Нажимает на ингредиент')
    def click_ingredient(self):
        self.click_element(ingredient)

    @allure.step('Возвращает количество ингредиентов')
    def get_ingredient_count(self):
        return self.get_element_text(count_ingredient)

    @allure.step('Возвращает окно Детали ингредиента')
    def get_window_ingredient_detail(self):
        return self.get_element_text(modal_window_ingredient)

    @allure.step('Возвращает класс модального окна')
    def get_modal_class(self):
        return self.get_attribute_element(close_modal, 'class')

    @allure.step('Нажимает на крестик в окне Детали ингредиента')
    def click_close_window_ingredient_detail(self):
        self.click_element(close_modal_window_ingredient)

    @allure.step('Возвращает ингредиент')
    def get_ingredient(self):
        return self.find(ingredient)

    @allure.step('Возвращает булку')
    def get_buns(self):
        return self.find(buns)

    @allure.step('Возвращает конструктор бургера')
    def get_burger_constructor(self):
        return self.find(constructor_burger)

    @allure.step('Перетаскивает элемент из одного места в другое')
    def drag_and_drop_element(self, source, target):
        self.actions.drag_and_drop(source, target).perform()

    @allure.step('Нажимает Оформить заказ')
    def click_order_button(self):
        self.click_element(arrange_order_button)

    @allure.step('Возвращает крестик для закрытия окна с заказом')
    def get_close_modal_order(self):
        self.click_element(close_modal_order)

    @allure.step('Создает бургер и оформляет заказ')
    def create_burger_and_place_order(self):
        ingredients = self.get_ingredient()
        bun = self.get_buns()
        burger_constructor = self.get_burger_constructor()
        self.drag_and_drop_element(bun, burger_constructor)
        self.drag_and_drop_element(ingredients, burger_constructor)
        self.click_order_button()

    def wait_loading_visibility(self, browser):
        self.wait.until(EC.visibility_of_element_located(LOADING))

    def wait_loading_invisibility(self, browser):
        self.wait.until(EC.invisibility_of_element_located(LOADING))

    @allure.step('Создает заказ и проверят Ленту заказов')
    def create_order_and_check_in_feed(self, browser):
        order_feed_page = OrderFeedPage(self.browser)
        user_order_history = ConstructorPage(browser)
        self.click_constructor_button()
        order_feed_page.wait_for_page_load(URL)
        self.create_burger_and_place_order()
        user_order_history.wait_loading_visibility(browser)  #delete
        user_order_history.wait_loading_invisibility(browser) #delete
        self.get_close_modal_order()
        order_feed_page.click_order_feed_button()
        order_feed_page.find(completed_all_time)

    @allure.step('Возвращает номер заказа')
    def get_modal_order_text(self):
        return self.get_element_text(modal_order)

    def wait_for_order_item(self, locator):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, locator)))