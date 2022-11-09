from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_section_constructor:
    def test_section_constructor_bun(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click() # Кнопка «Конструктор»
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2]").click() # Кнопка «Соусы», нужно для того чтобы кнопка «Булки» была доступна
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[1]").click() # Кнопка «Булки»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))    # явное ожидание по контейнеру «Булки»

    def test_section_constructor_sauces(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()    # Кнопка «Конструктор»
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[2]").click() # Кнопка «Соусы»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Соусы')]")))   # явное ожидание по контейнеру  «Соусы»

    def test_section_constructor_toppings(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click() # Кнопка «Конструктор»
        login.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[3]").click() # Кнопка «Начинки»
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Начинки')]")))   # явное ожидание по контейнеру «Начинки»