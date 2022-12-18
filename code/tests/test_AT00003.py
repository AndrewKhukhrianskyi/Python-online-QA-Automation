import pytest
import sys
# adding page_class to the system path

import importlib.util

'''
Date: 17.12.22
Tester Name: Vladislav Maksiutenko
Ticket: АТ00003
Short Description: Check the name of the site on the main page
Component: PT0000
'''
def test_AT00003():
    # passing the file name and path as argument
    spec = importlib.util.spec_from_file_location(
  "page_class", "Ваш путь до - page_class.py")
    page_cls = importlib.util.module_from_spec(spec) 
    spec.loader.exec_module(page_cls)
    website = page_cls.PageObject()
    website.assert_text_in_block('пятый элемент-днепр',
                                 "//div[@class='c-name']/h1",
                                 'xpath')
