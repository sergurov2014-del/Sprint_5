from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


import pytest
import locators
from selenium import webdriver
from random import randint
class LoginPageDoska:
    
    def __init__(self, driver): 
        self.driver = driver

    def registration(self,email,password): #метод - регистрации
    #Нажимаем на две кнопки
        self.driver.find_element(*locators.LOGIN_BUTTON).click()
        self.driver.find_element(*locators.NO_ACC_BUTTON).click()
    #вводим почту и пароль дважды, после чего кликнули на кнопку
        self.driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*locators.SUBMIT_PASSWORD_BUTTON).send_keys(password)
        self.driver.find_element(*locators.CREATE_ACC_BUTTON).click()

    def login(self, email, password): #метод - логина
        self.driver.find_element(*locators.LOGIN_BUTTON).click()
        self.driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*locators.ENTERY_BUTTON).click()

    def logout(self): #метод - выхода из приложения
        self.driver.find_element(*locators.LOGOUT_BUTTON).click()

    def post_an_ad_click(self): #метод - кликаем на кнопку «Разместить объявление» 
        self.driver.find_element(*locators.POST_AN_AD_BUTTON).click()

    def fill_in_ad_fields(self,name,description): #метода для заполнения полей объявления это не тест а издевательство!!!!!
        self.driver.find_element(*locators.AD_NAME_INPUT).send_keys(name) # заполняем название
        self.driver.find_element(*locators.AD_DESCRIPTION_INPUT).send_keys(description) # заполняем описание
        self.driver.find_element(*locators.AD_COST_INPUT).send_keys(randint(1,100000)) # заполняем цену рандомным числом в диапазоне от 1 до 100000
        self.driver.find_element(*locators.AD_CATEGORY_DROP_DOWN).click() #кликаем на стрелочк - открываем грёбаные категории
        self.driver.find_element(*locators.AD_BOOK_OF_CATEGORY_DROP_DOWN).click() #в категориях выбираем книгу, выбор  рандомной категории из списка неполучилось прикрутить
        self.driver.find_element(*locators.AD_CITY_DROP_DOWN).click() #кликаем на стрелочк - открываем грёбаные города
        self.driver.find_element(*locators.AD_CITY_KAZAN_DROP_DOWN).click() #в городах выбираем казань, выбор  рандомного города из списка неполучилось прикрутить
        self.driver.find_element(*locators.AD_STATE_RADIO_BUTTON_OLD).click()#Выбрать RabioButton «Состояние товара» б/у
                
    def click_publish(self): #метод для нажатия на кнопку «Опубликовать».
        self.driver.find_element(*locators.PUBLISH_BUTTON).click()       
       
    def  go_to_profile(self):   #Перейти в профиль пользователя.
        user_name_field= self.driver.find_element(*locators.USER_NAME_FIELD) # так как тут тест падал с ошибка из-за области видимости добавил прокрутку на верх к имени юзера
        self.driver.execute_script("arguments[0].scrollIntoView(true);", user_name_field)
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locators.GO_TO_USER_PROFILE_BUTTON)) #- ждём появления имени пользователя
        self.driver.find_element(*locators.GO_TO_USER_PROFILE_BUTTON).click()
        