from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_login:
    def test_login_by_login_button_on_main_page(self, login_test):
        login_test.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

    def test_login_by_personal_account_button(self, login_test):
        login_test.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

    def test_login_through_button_in_registration_page(self, login_test):
        login_test.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        login_test.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        login_test.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()


    def test_login_through_button_in_forgot_password_page(self, login_test):
        login_test.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        login_test.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        login_test.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()


