import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
from main import LoginPageDoska


class TestAddAdPageDoska:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-desk.education-services.ru/")

    def test_make_ad_unauthorized_user(self):
        login_page=LoginPageDoska(self.driver)         
        login_page.post_an_ad_click()
        web_element_ad_unauthorized_user=WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locators.FOR_POST_AD_AUTHORIZE_BUTTON))
        assert web_element_ad_unauthorized_user.is_displayed()

    def test_make_add_authorized_user(self, correct_mail,password,ad_name, ad_description):
        login_page=LoginPageDoska(self.driver)         
        login_page.registration(correct_mail,password)
        WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_FIELD)) #- ждём появления имени пользователя      
        login_page.post_an_ad_click()
        login_page.fill_in_ad_fields(ad_name, ad_description)
        login_page.click_publish()
        WebDriverWait(self.driver,2).until(expected_conditions.visibility_of_element_located(locators.USER_NAME_FIELD)) 
        login_page.go_to_profile()
        web_element_added_ad_in_my_profile=WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locators.ADDED_AD_IN_MY_PROFILE))       
        add_in_profile= self.driver.find_element(*locators.ADDED_AD_IN_MY_PROFILE) # так как тут тест падал с ошибка из-за области видимости добавил прокрутку к объявлению
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_in_profile)
        
                
        assert  web_element_added_ad_in_my_profile.is_displayed()
        
    def teardown_method(self):
        self.driver.quit()




