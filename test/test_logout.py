from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Testlogout:
    def test_logout(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()  # Кнопка «Личный Кабинет»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выход')]")))  # явное ожидание по кнопке «Выход»
        login.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()    # Кнопка «Выход»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))  # явное ожидание по кнопке «Войти»
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/login'   # проверяем корректный url
