from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys; sys.dont_write_bytecode = True
import os
import unittest
sys.path.append('{0}'.join(os.path.dirname(__file__).split(os.path.sep)[0:-2]).format(os.path.sep))# add project home path
from constants import *
from uimaps import loginpagemap
from pages.signin.loginpage import LogInPage

class LoggedInTestCasePage(LogInPage, unittest.TestCase):
    def __init__(self, driver):
        super(LoggedInTestCasePage, self).__init__(driver)
        self.email_login()
    
    def _verify_page(self):
        try:
            self.wait_for_element_visibility(50, 'xpath', loginpagemap["SignInTabXpath"])
        except:
            raise IncorrectPageException
print 'b'