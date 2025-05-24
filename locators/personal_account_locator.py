from selenium.webdriver.common.by import By

button_personal_account = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
order_history_link = (By.XPATH, "//a[@href='/account/order-history']")
exit_button = (By.XPATH, '//button[text()="Выход"]')
title_authorizations = (By.XPATH, "//h2[text()='Вход]")
order_history_last_item = (By.XPATH,"//div[contains(@class, 'OrderHistory_orderHistory')]/ul/li/a/div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text') and contains(@class, 'text_type_digits-default')]")