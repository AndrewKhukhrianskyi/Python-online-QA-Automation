import pytest
import sys

sys.path.append("Python-online-QA-Automation/code/framework/page_class.py")

from page_class import PageObject
'''
Date: 04/12/22
Tester Name: Ivan Ivanov
Ticket: РТ10001
Short Description: Check that user can open the main page of the website.
Component: PT0000
'''
def test_AT00001():
    website = PageObject()
    expected_text = 'https://5element-dnepr.promobud.ua/'
    actual_text = website.get_link()
    assert expected_text == actual_text