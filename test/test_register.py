from selenium.webdriver.common.by import By
import time

class Test_register:

    def test_registarion(self, driver, fake_name, fake_email, fake_password):
        driver.find_element(By.XPATH, "//header/nav[1]/a[1]").click() # Кнопка «личный кабинет»
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click() # Кнопка «Зарегистрироваться»
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(fake_name)  # ввод имени
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(fake_email) # ввод email
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys(fake_password) # ввод password
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click() # Кнопка «Зарегистрироваться»

    def test_registarion_error(self, driver, fake_name, fake_email):
        driver.find_element(By.XPATH, "//header/nav[1]/a[1]").click() # Кнопка «личный кабинет»
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click() # Кнопка «Зарегистрироваться»
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(fake_name)   # ввод имени
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(fake_email)  # ввод email
        driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("1")  # ввод некорректного пароля
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click() # Кнопка «Зарегистрироваться»
        time.sleep(1)
        assert driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'   # проверка что появилось сообщение





