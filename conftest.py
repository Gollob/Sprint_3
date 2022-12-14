
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver

    driver.quit()

@pytest.fixture
def email():
    return '701@gmail.cc'

@pytest.fixture
def password():
    return '123456'

@pytest.fixture
def login(driver, email, password):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка «Войти в аккаунт»
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(email)  # Поле «email» пердаем email
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(password) # Поле «password» пердаем password
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click() # Кнопка «Войти»

    yield driver

    return driver

@pytest.fixture
def login_test(driver, email, password):
    yield driver
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(email) # Поле «email» пердаем email
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(password) # Поле «password» пердаем password
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click() # Кнопка «Войти»
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))  # Локатор кнопка «Оформить заказ»
    return driver

@pytest.fixture
def fake_email(): #генерация email
    fake = Faker()
    return fake.email()

@pytest.fixture
def fake_name(): #генерация имени
    fake = Faker()
    return fake.first_name()

@pytest.fixture
def fake_password(): #генерация пароля
    fake = Faker()
    return fake.password(length=6)


