import allure
from data import ingredient_detail, ingredient_count, default_order_number
from urls import LOGIN, FEED, URL


class TestConstructor:
    @allure.title('Переход по клику на «Лента заказов»')
    def test_navigate_to_order_feed(self, browser, for_constructor):
        response, _, _, _, constructor, order_feed_page = for_constructor
        constructor.open(LOGIN)
        order_feed_page.click_order_feed_button()
        assert constructor.get_current_url() == FEED

    @allure.title('Клик по ингредиенту, вызывает окно Детали ингредиента')
    def test_click_ingredient_displays_popup_with_details(self, browser, for_constructor):
        _, _, _, _, constructor, _ = for_constructor
        constructor.open()
        constructor.click_ingredient()
        assert constructor.get_window_ingredient_detail() == ingredient_detail

    @allure.title('Окно Детали ингредиента закрывается кликом по крестику')
    def test_ingredient_popup_close(self, browser, for_constructor):
        _, _, _, _, constructor, _ = for_constructor
        constructor.open()
        constructor.click_ingredient()
        constructor.click_close_window_ingredient_detail()
        assert 'Modal_modal__P3_V5' in constructor.get_modal_class()

    @allure.step('При добавлении ингредиента, счётчик этого ингредиента увеличивается')
    def test_count_ingredient_when_ingredient_added(self, browser, for_constructor):
        _, _, _, _, constructor, _ = for_constructor
        constructor.open()
        ingredient = constructor.get_ingredient()
        burger_constructor = constructor.get_burger_constructor()
        constructor.drag_and_drop_element(ingredient, burger_constructor)
        assert constructor.get_ingredient_count() == ingredient_count

    @allure.step('Залогиненный пользователь может оформить заказ.')
    def test_user_can_place_order(self, browser, for_constructor):
        _, email, password, auth, constructor, _ = for_constructor
        auth.login(email, password)
        constructor.wait_for_page_load(URL)
        constructor.create_burger_and_place_order()
        constructor.wait_loading_visibility(browser)
        constructor.wait_loading_invisibility(browser)
        assert constructor.get_modal_order_text() != default_order_number