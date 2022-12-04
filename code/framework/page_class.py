from selenium.webdriver.common.by import By
from selenium import webdriver

import logging

class PageObject:
    # Открываем браузер через __init__
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://5element-dnepr.promobud.ua/")
    '''
        get_object() позволяет вытащить выражение из блока. Под выражением стоит понимать текст, ссылку и тд.
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def get_object(self, block_name, search = 'class'):
        finds = ['class', 'id', 'xpath']
        if search == 'class': 
            block = self.browser.find_element(by = By.CLASS_NAME, value = block_name)
        else:
            if search == 'id':
                block = self.browser.find_element(by = By.ID, value = block_name)
            elif search == 'xpath':
                block = self.browser.find_element(by = By.XPATH, value = block_name)
            else:
                logging.error('Ошибка: Обращаемся к несуществующей характеристике!')
                logging.warning(f'Доступные варианты поиска блока: {finds}!')
                return None
        return block.text
    '''
        assert_text_in_block проверяет наличие текста в блоке
        expected_text - ожидаемый текст
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def assert_text_in_block(self, expected_text, block_name, search):
        given_text = self.get_object(block_name, search)
        if expected_text == given_text:
            assert True
        assert False
    '''
        get_link достает ссылку сайта
    '''
    def get_link(self):
        return self.browser.current_url
    '''
        TODO: 
        1. Добавить метод, который будет проверять наличие панели на сайте
        2. Добавить метод, который будет доставать количество товара из боковой панели
        3. Добавить метод, который будет доставать цену товара
        4. Добавить метод, который будет логиниться в систему
        5. Добавить метод, который будет регистрировать пользователя в системе
    '''