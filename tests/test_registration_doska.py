from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from main import LoginPageDoska


class TestRegistrationPageDoska:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-desk.education-services.ru/")

    def test_registration_with_correct_email(self,correct_mail,password): # тест на регистрацию с корректным email
         login_page=LoginPageDoska(self.driver)
         login_page.registration(correct_mail,password)
         web_element_user_name_exist=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_FIELD))
         web_element_user_avatar_exist=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_AVATAR_PHOTO))
         assert  web_element_user_name_exist.is_displayed() and web_element_user_avatar_exist.is_displayed()
 
    def test_registration_with_incorrect_email_mask(self,incorrect_mail,password): # не нашёл отдельного стиля отвечающего за красный цвет проверю только наличие ошибки
         login_page=LoginPageDoska(self.driver)
         login_page.registration(incorrect_mail,password)
         web_element_error_test=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.RED_ERROR_AFTER_REGISTRATION))
         assert web_element_error_test.is_displayed()    

    def test_registration_with_already_exsist_user(self,correct_mail,password):
        login_page=LoginPageDoska(self.driver)                                  # создаём аккаунт -после этого происходит автоматический вход 
        login_page.registration(correct_mail,password)
        web_element_user_name=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_FIELD)) #- ждём появления имени пользователя
        login_page.logout() #после чего жмём по кнопке выхода и выходим
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON)) #- ждём появления кнопки логина
        login_page.registration(correct_mail,password) #пытаемся зарегаться ещё раз с темже пользователем
        web_element_exsist_user_error_test=WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.RED_ERROR_AFTER_REGISTRATION))
        assert web_element_exsist_user_error_test.is_displayed() # проверяем появление ошибки, с цветами я без понятия что делать, проверяющий подскажи пожалуйста

    def teardown_method(self):
        self.driver.quit()

