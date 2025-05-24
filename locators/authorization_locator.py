from selenium.webdriver.common.by import By

email_input = (By.XPATH, "//input[@type='text']")
password_input = (By.XPATH, ".//input[@type='password']")
button_enter = (By.XPATH, '//button[contains(text(), "Войти")]')