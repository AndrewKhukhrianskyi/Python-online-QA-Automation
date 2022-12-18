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
        get_block достает искомую панель на странице
        block_name - название блока
        search_type - тип поиска (class, ID, XPATH и тд.)
    '''
    def get_block(self, block_name, search_type = 'class'):
    def get_block(self, block_name, search_type = 'class'):
        finds = ['class', 'id', 'xpath']
        if search_type == 'class': 
        if search_type == 'class': 
            block = self.browser.find_element(by = By.CLASS_NAME, value = block_name)
        else:
            if search_type == 'id':
                block = self.browser.find_element(by = By.ID, value = block_name)
            elif search_type == 'xpath':
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
        return block
    '''
        get_object_text() позволяет вытащить выражение из блока. Под выражением стоит понимать текст, ссылку и тд.
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def get_object_text(self, block_name, search_type):
        block = self.get_block(block_name, search_type)
        return block.text