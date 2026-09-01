from selenium.webdriver.common.by import By


LOGIN_BUTTON=(By.XPATH, ".//button[text()='Вход и регистрация']") #Кнопка входа и регистрации
NO_ACC_BUTTON=(By.XPATH, "//button[contains(text(), 'Нет аккаунта')]") #Кнопка Нет аккаунта
EMAIL_INPUT=(By.NAME,"email") # поле для ввода email при регистрации
PASSWORD_INPUT=(By.NAME ,"password") # поле для ввода пароля при регистрации
SUBMIT_PASSWORD_BUTTON=(By.NAME,"submitPassword") # поле для подтверждения пароля при регистрации
CREATE_ACC_BUTTON=(By.XPATH, "//button[contains(text(), 'Создать аккаунт')]") #Кнопка создания нового аккаунта
USER_NAME_FIELD=(By.CLASS_NAME, "profileText") # Поле с именем юзера для проверки теста регистрации
USER_AVATAR_PHOTO=(By.CLASS_NAME, "svgSmall") #фото юзера для проверки  
RED_ERROR_AFTER_REGISTRATION=(By.XPATH,"//span[text()='Ошибка']") #локатор ошибки при некорректной регистрации,  как проверить красные кнопки я не понял надо ли это и насколько корректно непонятно
ENTERY_BUTTON=(By.XPATH, "//button[text()='Войти']") #кнопка входа при регистрации
LOGOUT_BUTTON=(By.XPATH, "//button[text()='Выйти']") #кнопка выхода из аккаунта
ERROR_AFTER_REGISTRATION_EXIST_USER=(By.XPATH, "//font[text()='Пароли не произошло']")
POST_AN_AD_BUTTON=(By.XPATH, "//button[text()='Разместить объявление']") #кнопка добавления объявления
FOR_POST_AD_AUTHORIZE_BUTTON=(By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']") # локатор заголовка модельного окна «Чтобы разместить объявление, авторизуйтесь».
AD_NAME_INPUT=(By.NAME,"name") #поле названия объявляения
AD_DESCRIPTION_INPUT=(By.XPATH, "//textarea[@placeholder='Описание товара']") # поле с описанием
AD_COST_INPUT=(By.NAME, "price") #поле с ценой
AD_CATEGORY_DROP_DOWN=(By.XPATH,"//input[@name='category']/following-sibling::button") # выпадающее поле с выбором категории //input[@name='category']/following-sibling::button[contains(@class,'dropDownMenu')]
AD_BOOK_OF_CATEGORY_DROP_DOWN=(By.XPATH, "//span[text()='Книги']/parent::button") #пытался сделать с автоматической подстановкой из списка AD_BOOK_OF_CATEGORY_DROP_DOWN=(By.XPATH, '//span[text()=f"{list_of_shit_categorys}"]/parent::button') не вышло :(#это фиговый вариант -//div[contains(@class,'dropDownMenu_dropMenu')] тут два списка 
#при необходимости сюда легко можно добавить локаторы других категорий, но надо ли это?
AD_CITY_DROP_DOWN=(By.XPATH,"//input[@name='city']/following-sibling::button")# выпадающее поле с выбором города 
AD_CITY_KAZAN_DROP_DOWN=(By.XPATH, "//span[text()='Казань']/parent::button") #пытался сделать с автоматической подстановкой из списка AD_BOOK_OF_CATEGORY_DROP_DOWN=(By.XPATH, '//span[text()=f"{list_of_shit_categorys}"]/parent::button') не вышло :(#это фиговый вариант -//div[contains(@class,'dropDownMenu_dropMenu')] тут два списка 
#при необходимости сюда легко можно добавить локаторы других городов, но надо ли это?
AD_STATE_RADIO_BUTTON_OLD=(By.XPATH, "//input[@name='condition' and @value='Б/У']/following-sibling::div")# кнопка выбора состояния товара Б/У при необходимости легко добавить локатор Новый AD_STATE_RADIO_BUTTON_NEWPUBLISH_BUTTON заменив @value='Новый'
PUBLISH_BUTTON=(By.XPATH, "//button[text()='Опубликовать']") #Локатор кнопки опубликовать объявление
GO_TO_USER_PROFILE_BUTTON=(By.XPATH, "//button[@class='circleSmall']")#локатор аватарки при нажатии на которую происходит переход в профиль польователя
ADDED_AD_IN_MY_PROFILE=(By.XPATH, "//div[@class='about']") #локатор описания объявления добавленного в профиль
