from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import logging

class PageObject:
    # Открываем браузер через __init__
    def __init__(self):
        self.options = Options()
        self.options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        self.browser = webdriver.Firefox(executable_path=r'C:/Users/Андрей/Desktop/Код/Python-online-QA-Automation/code/framework/geckodriver.exe',
                                         options=self.options)
        self.browser.get("https://5element-dnepr.promobud.ua/")
    
    '''
        get_block достает искомую панель на странице
        block_name - название блока
        search_type - тип поиска (class, ID, XPATH и тд.)
    '''
    def get_block(self, block_name, search_type = 'class'):
        finds = ['class', 'id', 'xpath']
        if search_type == 'class': 
            block = self.browser.find_element(by = By.CLASS_NAME, value = block_name)
        else:
            if search_type == 'id':
                block = self.browser.find_element(by = By.ID, value = block_name)
            elif search_type == 'xpath':
                block = self.browser.find_element(by = By.XPATH, value = block_name)
            else:
                logging.error('Ошибка: Обращаемся к несуществующей характеристике!')
                logging.warning(f'Доступные варианты поиска блока: {finds}!')
                return None
        return block
    '''
        get_object_text() позволяет вытащить выражение из блока. Под выражением стоит понимать текст, ссылку и тд.
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def get_object_text(self, block_name, search_type):
        block = self.get_block(block_name, search_type)
        return block.text
    '''
        assert_text_in_block проверяет наличие текста в блоке
        expected_text - ожидаемый текст
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search_type - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def assert_text_in_block(self, expected_text, block_name, search):
        given_text = self.get_block(block_name, search).text
        if expected_text == given_text:
            assert True
        else:
            assert False
        print(given_text)
    '''
        get_link достает ссылку сайта
    '''
    def get_link(self):
        return self.browser.current_url
    '''
        assert_block_on_page проверяет наличие панели на веб-странице
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search_type - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def assert_block_on_page(self, block_name, search_type):
        block, new_block = '', ''
        new_block = self.get_block(block_name, search_type)
        if block != new_block:
            assert True
        else:
            assert False

    '''
        Функция, которая достает с боковой панели сайта кол-во товара
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search_type - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def get_item_number_from_page(self, block_name, search_type):
        number = self.get_block(block_name, search_type)
        for wrong_element in '()':
            number = number.replace(wrong_element)
        return int(number)
    """
        Функция, которая достает цену товара с главной панели
        block_name - имя блока
        Предупреждение: Способ поиска работает ТОЛЬКО через XPATH. Попытка использования других вариантов
        приведет к ошибке!
    """
    def get_price_from_item(self, block_name):
        price = self.get_block(block_name, 'xpath')
        return int(price)
    '''
       Функция, которая достает список цен товаров
       block_list_name - список названия блоков
       Имейте в виду, что поиск выполняется ТОЛЬКО через xpath 
    '''
    def get_price_list(self, block_name_list):
        price_list = []
        for block_name in block_name_list:
            price = self.get_block(block_name, 'xpath')
            price_list.append(int(price))
        return price_list

    '''
       Функция, которая регистрирует пользователя на сайте
       email - электронная почта
       name - имя
       phone_number - номер телефона
    '''
    def register_user(self, email, name, phone_number):
        name_list = {'email' : email, 'name' : name, 'phone' : phone_number}
        button = self.get_block('gui-button-blue', 'class')
        button.click()
        register_link = self.get_block('//div[@class="gui-window-content"]/div[1]/form/div/div/a[1]',
                                        'xpath')
        register_link.click()
        for field_type, value in name_list.items():
            field = self.get_block(f'//div[@class="gui-field-input"]/input[@name="{field_type}"]',
                                    'xpath')
            field.send_keys(value)
        save_button = self.get_block('//div[@class="gui-form-footer"]/a',
                                    'xpath')
        save_button.click()
        close_button = self.get_block('//div[@class="gui-window-controls"]/a')
        close_button.click()

    '''
       Функция, которая записывает текст в поле
       block_name - имя блока
       search_type - тип поиска
       text - передаваемый текст в поле
    '''
    def send_data_to_block(self, block_name, search_type, text):
        block = self.get_block(block_name, search_type)
        login_fiels = ['login', 'password']
        

    '''
        Метод, который будет логинить пользователя в систему:
        1. data - словарь с почтой и паролем
    '''
    def user_login(self, data):
        button = self.get_block('gui-button-blue', 'class') 
        button.click()
        for key, value in data.items():
            if value is None:
                assert False
        text_field = self.get_block(f'//div[@class="gui-field-input"]/input[@name="login"]')
        text_field.send_keys(data['email'])

        text_field = self.get_block(f'//div[@class="gui-field-input"]/input[@name="password"]')
        text_field.send_keys(data['password'])

        button.click()       
