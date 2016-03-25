from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys; sys.dont_write_bytecode = True
import os
from abc import ABCMeta, abstractmethod
sys.path.append('{0}'.join(os.path.dirname(__file__).split(os.path.sep)[0:-1]).format(os.path.sep))# add project home path
from  constants import locators

class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.verify_page()
        
    @abstractmethod 
    def verify_page(self):
        """
        Does Nothing
        """
    def wait_for_element_visibility(self, waittime, locatormode, locator):
        element = None
        if locatormode == locators.ID:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.visibility_of_element_located((By.ID,locator)))
        elif locatormode == locators.NAME:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.visibility_of_element_located((By.NAME,locator)))
        elif locatormode == locators.XPATH:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.visibility_of_element_located((By.XPATH,locator)))
        elif locatormode == locators.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.visibility_of_element_located((By.CSS_SELECTOR,locator)))
        else:
            raise Exception('Unsupported locator strategy')
        return element
    
    def wait_until_element_clickable(self, waittime, locatormode, locator):
        element = None
        if locatormode == locators.ID:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.element_to_be_clickable((By.ID,locator)))
        elif locatormode == locators.NAME:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.element_to_be_clickable((By.NAME,locator)))
        elif locatormode == locators.XPATH:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.element_to_be_clickable((By.XPATH,locator)))
        elif locatormode == locators.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waittime).\
                until(EC.element_to_be_clickable((By.CSS_SELECTOR,locator)))
        else:
            raise Exception('Unsupported locator strategy')
        return element        
    
    def swith_to_window(self, window_handle):
        self.driver.switch_to_window(window_handle)
        
    def find_element(self, locatormode, locator):
        element = None
        if locatormode == locators.ID:
            element = self.driver.find_element_by_id(locator)
        elif locatormode == locators.NAME:
            element = self.driver.find_element_by_name(locator)
        elif locatormode == locators.XPATH:
            element = self.driver.find_element_by_xpath(locator)
        elif locatormode == locators.CSS_SELECTOR:
            element = self.driver.find_element_by_class_name(locator)
        else:
            raise Exception('Unsupported locator strategy')
        return element
    
    def fill_out_field(self, locatormode, locator, text):
        self.find_element(locatormode, locator).clear()
        self.find_element(locatormode, locator).send_keys(text)
    
    def click(self, waittime, locatormode, locator):
        self.wait_until_element_clickable(waittime, locatormode, locator).click()
    
class IncorrectPageException(Exception):
    '''
    This exception will be thrown when trying to instatiate the wrong page.
    '''