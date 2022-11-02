from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testsectionconstructor:
    def test_section_constructor_bun(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2]").click()
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[1]").click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))

    def test_section_constructor_sauces(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2]").click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Соусы')]")))

    def test_section_constructor_toppings(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[3]").click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Начинки')]")))