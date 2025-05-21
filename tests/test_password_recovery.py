import allure
from pages.password_recovery_page import PasswordRecoveryPage
from urls import RESET_PASSWORD, FORGOT_PASSWORD, LOGIN


class TestPasswordRecovery:
    @allure.step('Переход на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_password_recovery_page(self, browser):
        recover_password = PasswordRecoveryPage(browser)
        recover_password.open(LOGIN)
        recover_password.click_recover_password()
        assert recover_password.get_current_url() == FORGOT_PASSWORD

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_password_reset_email_submission(self, browser):
        recovery_page = PasswordRecoveryPage(browser)
        recovery_page.open(FORGOT_PASSWORD)
        recovery_page.send_text_email()
        recovery_page.click_recovery_button()
        recovery_page.wait_for_page_load(RESET_PASSWORD)
        assert recovery_page.get_current_url() == RESET_PASSWORD

    @allure.title('Клик по кнопке показать/скрыть пароль')
    def test_show_activates_password_field(self, browser):
        recovery_page = PasswordRecoveryPage(browser)
        recovery_page.open(LOGIN)
        recovery_page.click_recover_password()
        recovery_page.send_text_email()
        recovery_page.click_recovery_button()
        recovery_page.wait_for_page_load(RESET_PASSWORD)
        recovery_page.click_show_hide_button()
        assert 'input_status_active' in recovery_page.get_show_password().get_attribute('class')