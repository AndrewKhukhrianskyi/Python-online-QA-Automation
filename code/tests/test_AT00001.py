import pytest
import sys
# adding page_class to the system path

import importlib.util

'''
Date: 04/12/22
Tester Name: Example Test
Ticket: РТ10001
Short Description: Check that user can open the main page of the website.
Component: PT0000
'''
def test_AT00001():
    # passing the file name and path as argument
    spec = importlib.util.spec_from_file_location(
  "page_class", "Здесь указываете полный путь к page_class.py")
    page_cls = importlib.util.module_from_spec(spec) 
    spec.loader.exec_module(page_cls)
    website = page_cls.PageObject()
    expected_text = 'https://5element-dnepr.promobud.ua/'
    actual_text = website.get_link()
    assert expected_text == actual_text
