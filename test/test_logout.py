from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Testlogout:
    def test_logout(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]")))
        login.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/login'
