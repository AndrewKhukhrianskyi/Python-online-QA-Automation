from selenium.webdriver.common.by import By
from selenium import webdriver

import logging

class PageObject:
    # Открываем браузер через __init__
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://5element-dnepr.promobud.ua/")
    '''
        get_text() позволяет вытащить текст из блока
        block_name - имя блока (название тега, способ поиска тега (ЕСЛИ ИЩЕМ ЧЕРЕЗ XPATH) и тд)
        search - способ поиска (т.е каким образом будем искать нужный нам элемент)
    '''
    def get_text(self, block_name, search = 'class'):
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