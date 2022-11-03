from selenium.webdriver.common.by import By

class Test_login:
    def test_login_by_login_button_on_main_page(self, login_test):
        login_test.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()  # Кнопка «Войти в аккаунт»

    def test_login_by_personal_account_button(self, login_test):
        login_test.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click() # Кнопка «Личный Кабинет»

    def test_login_through_button_in_registration_page(self, login_test):
        login_test.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click() # Кнопка «Личный Кабинет»
        login_test.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click() # Кнопка «Зарегистрироваться»
        login_test.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click() # Кнопка «Войти»


    def test_login_through_button_in_forgot_password_page(self, login_test):
        login_test.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()  # Кнопка «Личный Кабинет»
        login_test.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()  # Кнопка «Восстановить пароль»
        login_test.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()   # Кнопка «Войти»


