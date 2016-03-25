# -*- coding: utf-8 -*-
import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys; sys.dont_write_bytecode = True
import os
sys.path.append('{0}'.join(os.path.dirname(__file__).split(os.path.sep)[0:-1]).format(os.path.sep))# add project home path

from basetestcase import BaseTestCase
from constants import *
from uimaps import loginpagemap
from pages.basepage import BasePage
from pages.signin.loginpage import LogInPage
from pages.findroommates.createofferpage import CreateOfferPage
#unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)

class CreateOfferTest(BaseTestCase, unittest.TestCase):
    
    def setUp(self):
        super(CreateOfferTest, self).setUp()
        self.navigate_to_page(general_constants["base_url"])
        log_in_page_object = LogInPage(self.driver)
        log_in_page_object._verify_page()
        log_in_page_object.email_login()
    
    def test_createoffer(self):
        log_in_page_object = LogInPage(self.driver)
        log_in_page_object._verify_page()
        try:
            self.assertTrue(log_in_page_object.email_login())
        except:
            self.fail("Error in Nomal Login")
            

    def tearDown(self):
        super(LoginTest, self).tearDown()
 
if __name__ == "__main__":
    unittest.main()