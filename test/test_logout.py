from selenium.webdriver.common.by import By
import time

class Testlogout:
    def test_test_go_to_account_page(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        time.sleep(1)
        login.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        time.sleep(1)
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/login'
