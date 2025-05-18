import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.personal_account_locator import button_personal_account
from urls import URL
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)
        self.wait = WebDriverWait(self.browser, 20)

    @allure.step('Метод для получения атрибута элемента')
    def get_attribute_element(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)

    @allure.step("Ожидание пока элемент не станет кликабельным")
    def wait(self, locator):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        return self.browser.find_element(*locator)

    @allure.step('Ожидание загрузки страницы')
    def wait_for_page_load(self, url):
        WebDriverWait(self.browser, 10).until(EC.url_to_be(url))

    @allure.step('Поиск элемента')
    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    @allure.step('Метод для поиска элемента')
    def find(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.find(locator).click()

    @allure.step('Ввода данных')
    def send_text(self, locator, text):
        self.find(locator).send_keys(text)

    @allure.step('Открывает главную страницу')
    def open(self, url=None):
        if url is not None:
            self.browser.get(url)
        else:
            self.browser.get(URL)

    @allure.step('Возвращаем текущую страницу')
    def get_current_url(self):
        return self.browser.current_url

    @allure.step('Получения текста элемента')
    def get_element_text(self, locator):
        return self.find(locator).text

    @allure.step('Нажимает на кнопку "Личный кабинет')
    def click_personal_account(self):
        self.click_element(button_personal_account)