from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testswitching:
    def test_go_to_account_page(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]")))
