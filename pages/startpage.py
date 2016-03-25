from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys; sys.dont_write_bytecode = True
import os
sys.path.append('{0}'.join(os.path.dirname(__file__).split(os.path.sep)[0:-1]).format(os.path.sep))# add project home path
from constants import *
from uimaps import startuppagemap
from pages.startpage import BasePage,IncorrectPageException

class StartUpPage(BasePage):
    def __init__(self, driver):
        super(StartUpPage, self).__init__(driver)
    
    def _verify_page(self):
        try:
            self.wait_for_element_visibility(50, 'xpath', startuppagemap["StartUpPageSignInTabXpath"])
        except:
            raise IncorrectPageException
        
    def city_search(self):
        pass
    
    def offer_mini_form(self):
        pass

