from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from main import LoginPageDoska


class TestLoginPageDoska:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-desk.education-services.ru/")

    def test_login_user(self,correct_mail,password):
        login_page=LoginPageDoska(self.driver)                                  # создаём аккаунт -после этого происходит автоматический вход 
        login_page.registration(correct_mail,password)
        web_element_user_name=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_FIELD)) #- ждём появления имени пользователя
        login_page.logout() #после чего жмём по кнопке выхода и выходим
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON)) #- ждём появления имени пользователя
        login_page.login(correct_mail,password)
        web_element_user_name_exist=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_FIELD))               
        assert web_element_user_name_exist.is_displayed()

    def test_logout_user(self,correct_mail,password):
        login_page=LoginPageDoska(self.driver)                                  # создаём аккаунт -после этого происходит автоматический вход 
        login_page.registration(correct_mail,password)
        web_element_user_name=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_FIELD)) #- ждём появления имени пользователя
        login_page.logout() #после чего жмём по кнопке выхода и выходим
        web_element_Log_in_sign_up=WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON)) #- ждём появления имени пользователя
        assert web_element_Log_in_sign_up.is_displayed() #проверяем отображение кнопки «Вход и регистрация».

    
    def teardown_method(self):
        self.driver.quit()

