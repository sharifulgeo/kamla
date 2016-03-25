from selenium import webdriver
from constants import  *
import unittest

class BaseTestCase(object):
    
    def setUp(self):
        if general_constants['browser'].lower() == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif general_constants['browser'].lower() == 'chrome':
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        elif general_constants['browser'].lower() == 'ie':
            self.driver = webdriver.Ie()
            self.driver.maximize_window()                
        else:
            raise Exception ('This driver is not supported!')
        
    def navigate_to_page(self, url):
        self.driver.get(url)
        
    def tearDown(self):
        self.driver.quit()