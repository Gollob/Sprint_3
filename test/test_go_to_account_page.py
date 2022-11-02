from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Testaccountpage:
    def test_login_by_personal_account_button(self, login):
        login.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//header")))
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/account'
