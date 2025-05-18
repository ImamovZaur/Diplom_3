import requests
import pytest
from selenium import webdriver
from urls import URL, CREATE_USER, DELETE_USER
from helpers import generate_users
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.authorization_page import AuthorizationPage
from pages.personal_account_page import PersonalAccountPage
from pages.password_recovery_page import PasswordRecoveryPage


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    driver = None
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get(URL)
    yield driver
    driver.quit()

@pytest.fixture()
def create_and_delete_user():
    payload = generate_users()
    response = requests.post(CREATE_USER, data=payload)
    yield response, payload
    access_token = response.json()['accessToken']
    requests.delete(DELETE_USER, headers={'Authorization': access_token})

@pytest.fixture
def for_constructor(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    auth = AuthorizationPage(browser)
    constructor = ConstructorPage(browser)
    order_feed_page = OrderFeedPage(browser)
    yield response, email, password, auth, constructor, order_feed_page

@pytest.fixture()
def for_order(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    auth = AuthorizationPage(browser)
    order_feed_page = OrderFeedPage(browser)
    personal_account = PersonalAccountPage(browser)
    constructor = ConstructorPage(browser)
    yield response, email, password, auth, order_feed_page, personal_account, constructor

@pytest.fixture()
def for_recovery_password(browser):
    recovery_page = PasswordRecoveryPage(browser)
    yield recovery_page

@pytest.fixture()
def for_personal_account(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    personal_account = PersonalAccountPage(browser)
    auth = AuthorizationPage(browser)
    yield response, email, password, personal_account, auth