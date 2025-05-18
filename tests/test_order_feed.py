from locators.order_feed_locator import number, completed_all_time
from locators.personal_account_locator import order_history_last_item
from urls import URL, PROFILE
from pages.base_page import *
import allure


class TestOrderFeed:
    @allure.title('При клике на заказ, открывается всплывающее окно с деталями')
    def test_open_order_details_popup(self, browser, for_order):
        _, _, _, _,order_feed_page, _, _ = for_order
        order_feed_page.open()
        order_feed_page.click_order_feed_button()
        order_feed_page.click_first_order()
        assert order_feed_page.get_order_popup().is_displayed()

    @allure.step('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_history_displayed_on_order_feed(self, browser, for_order):
        _, email, password, auth, order_feed_page, personal_account, constructor = for_order
        auth.login(email, password)
        constructor.wait_for_page_load(URL)
        constructor.create_burger_and_place_order()
        constructor.wait_loading_visibility(browser)
        constructor.wait_loading_invisibility(browser)
        constructor.get_close_modal_order()
        constructor.click_personal_account()
        constructor.wait_for_page_load(PROFILE)
        personal_account.click_order_history_button()
        personal_account.wait_order_load(order_history_last_item)
        last_order_number = personal_account.get_last_order_number()
        order_feed_page.click_order_feed_button()
        personal_account.wait_order_load(number)
        order_numbers_in_feed = order_feed_page.get_all_orders_number()
        assert last_order_number in order_numbers_in_feed


    @allure.title('При создании заказа счётчик Выполнено за всё время увеличивается')
    def test_orders_module_all_time_counter_increases(self, browser, for_order):
        _, email, password, auth, order_feed_page, _, constructor = for_order
        auth.login(email, password)
        order_feed_page.click_order_feed_button()
        order_feed_page.find(completed_all_time)
        count_number = order_feed_page.get_all_orders_count()
        constructor.create_order_and_check_in_feed(browser)
        assert order_feed_page.get_all_orders_count != count_number


    @allure.title('При создании заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_new_order_increases_today_counter(self, browser, for_order):
        _, email, password, auth, order_feed_page, _, constructor = for_order
        auth.login(email, password)
        constructor.wait_for_page_load(URL)
        order_feed_page.click_order_feed_button()
        order_feed_page.find(completed_all_time)
        count_number = order_feed_page.get_today_orders_count()
        constructor.create_order_and_check_in_feed(browser)
        assert order_feed_page.get_today_orders_count() != count_number

    @allure.title('После оформления заказа его номер появляется в разделе "В работе".')
    def test_new_order_number_appears_in_work_section(self, browser, for_order):
        _, email, password, auth, order_feed_page, _, constructor = for_order
        auth.login(email, password)
        constructor.wait_for_page_load(URL)
        constructor.create_burger_and_place_order()
        constructor.wait_loading_visibility(browser)
        constructor.wait_loading_invisibility(browser)
        number_order ='0'+ constructor.get_modal_order_text()
        constructor.get_close_modal_order()
        order_feed_page.click_order_feed_button()
        count_number = order_feed_page.get_orders_in_work()
        assert count_number == number_order