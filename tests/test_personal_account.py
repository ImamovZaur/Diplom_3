import allure
import pytest
from urls import LOGIN, HISTORY


class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_personal_cabinet_navigation(self, browser, for_personal_account):
        _, _, _, personal_account, _ = for_personal_account
        personal_account.open()
        personal_account.click_personal_account()
        assert personal_account.get_current_url() == LOGIN

    @allure.title('Переход в раздел «История заказов»')
    def test_navigate_to_order_history(self, browser, for_personal_account):
        _, email, password, personal_account, auth = for_personal_account
        auth.login(email, password)
        personal_account.click_personal_account()
        personal_account.click_order_history_button()
        assert personal_account.get_current_url() == HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout_your_account(self, browser, for_personal_account):
        _, email, password, personal_account, auth = for_personal_account
        auth.login(email, password)
        personal_account.click_personal_account()
        personal_account.click_exit_button()
        personal_account.wait_for_page_load(LOGIN)
        assert personal_account.get_current_url() == LOGIN