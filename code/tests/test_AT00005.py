import pytest
import sys
# adding page_class to the system path

import importlib.util

'''
Date: 
Tester Name: 
Ticket: АТ10005
Short Description: 
Component: PT0000
'''
def test_AT00005():
    # passing the file name and path as argument
    spec = importlib.util.spec_from_file_location(
  "page_class", "ВАШ ПУТЬ ДО page_class.py")
    page_cls = importlib.util.module_from_spec(spec) 
    spec.loader.exec_module(page_cls)
    # TODO дописать логику