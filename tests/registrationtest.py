# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys; sys.dont_write_bytecode = True
import os
sys.path.append('{0}'.join(os.path.dirname(__file__).split(os.path.sep)[0:-1]).format(os.path.sep))# add project home path
from basetestcase import BaseTestCase
from constants import *
from uimaps import loginpagemap
from pages.basepage import BasePage
from pages.signup.registerpage import SignUpPage
#unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)

class SignUpTest(BaseTestCase, unittest.TestCase):
    
    def setUp(self):
        super(SignUpTest, self).setUp()
        self.navigate_to_page(general_constants["base_url"])
    
    def test_login(self):
        sign_up_page_object = SignUpPage(self.driver)
        sign_up_page_object._verify_page()
        try:
            self.assertTrue(sign_up_page_object.email_register())
        except:
            self.fail("Error in Nomal Signup")
            
    def test_facebook_register(self):
        sign_up_page_object = SignUpPage(self.driver)
        sign_up_page_object._verify_page()
        try:
            self.assertTrue(sign_up_page_object.facebook_register())
        except:
            self.fail("Error in Facebook Signup")

    def tearDown(self):
        super(SignUpTest, self).tearDown()
 
if __name__ == "__main__":
    unittest.main()
#if __name__ == "__main__":
    #suite = unittest.TestSuite()
    #suite.addTest(LoginTest("test_login"))
    #suite.addTest(LoginTest("test_facebook_login"))
    #unittest.TextTestRunner(verbosity=2).run(suite)