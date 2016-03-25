from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys; sys.dont_write_bytecode = True
import os
sys.path.append('{0}'.join(os.path.dirname(__file__).split(os.path.sep)[0:-2]).format(os.path.sep))# add project home path
from constants import *
from uimaps import signuppagemap
from pages.basepage import BasePage,IncorrectPageException

class SignUpPage(BasePage):
    def __init__(self, driver):
        super(SignUpPage, self).__init__(driver)
    
    def _verify_page(self):
        try:
            self.wait_for_element_visibility(50, 'xpath', signuppagemap["SignUpTabXpath"])
        except:
            raise IncorrectPageException
    
    def email_register(self):
        self.find_element('xpath', signuppagemap["SignUpTabXpath"]).click()
        self.wait_for_element_visibility(50, 'xpath', signuppagemap["SignUpEmailXapth"])
        if self.find_element('xpath', signuppagemap["CookieAlertXpath"]):
            self.find_element('xpath', signuppagemap["CookieAlertXpath"]).click()
        try:
            self.wait_for_element_visibility(50, 'xpath', signuppagemap["SignUpEmailXapth"])
        except:
            self.driver.get(general_constants["base_url"]+'register')
        self.wait_for_element_visibility(50, 'xpath', signuppagemap["SignUpEmailXapth"])
        self.click(10, 'xpath', signuppagemap["SignUpEmailXapth"])
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(\
            (By.XPATH,signuppagemap["SignUpEmailUsernameXpath"])))
        self.driver.find_element_by_xpath(signuppagemap["SignUpEmailUsernameXpath"]).\
            send_keys(SignUpPageConstants.login_constants["username"])
        self.driver.find_element_by_xpath(signuppagemap["SignUpEmailEmailXpath"]).\
            send_keys(SignUpPageConstants.login_constants["email"])
        self.driver.find_element_by_xpath(signuppagemap["SignUpEmailPasswordXpath"]).\
            send_keys(SignUpPageConstants.login_constants["password"])
        self.driver.find_element_by_xpath(signuppagemap["SignUpEmailPasswordConfirmXpath"]).\
            send_keys(SignUpPageConstants.login_constants["password"])
        self.click(50, 'xpath', signuppagemap["SignUpEmailSubmitXpath"])
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(
            (By.XPATH,signuppagemap["SignUpEmailAccountTabXpath"])))
        return True if bool(self.driver.find_elements_by_xpath(\
            signuppagemap["SignUpEmailAccountTabXpath"])) else False
        
    def facebook_register(self):
        self.find_element('xpath', signuppagemap["SignUpTabXpath"]).click()
        self.wait_for_element_visibility(50, 'xpath', signuppagemap["SignUpEmailXapth"])
        if self.find_element('xpath', signuppagemap["CookieAlertXpath"]):
            self.find_element('xpath', signuppagemap["CookieAlertXpath"]).click()
        try:
            self.wait_for_element_visibility(50, 'xpath', signuppagemap["SignUpEmailXapth"])
        except:
            self.driver.get(general_constants["base_url"]+'register')
        self.wait_for_element_visibility(50, 'xpath', signuppagemap["SignUpEmailXapth"])
        self.click(20,'xpath', signuppagemap["SignUpFacebookXpath"])
        WebDriverWait(self.driver,20).until(lambda x: len(x.window_handles)>1)
        self.driver.switch_to_window(self.driver.window_handles[-1])  
        self.driver.find_element_by_xpath(signuppagemap["SignUpFacebookUsernameXpath"]).send_keys\
            (SignUpPageConstants.faceebook_login_constants["username"])
        self.driver.find_element_by_xpath(signuppagemap["SignUpFacebookUsernameXpath"]).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(signuppagemap["SignUpFacebookPasswordXpath"]).click()
        self.driver.find_element_by_xpath(signuppagemap["SignUpFacebookPasswordXpath"]).\
            send_keys(SignUpPageConstants.faceebook_login_constants["password"])
        self.driver.find_element_by_xpath(signuppagemap["SignUpFacebookLoginXpath"]).click()
        self.driver.switch_to_window(self.driver.window_handles[0])
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(\
            (By.XPATH,signuppagemap["SignUpFacebookAccountTabXpath"])))        
        return True if bool(self.driver.find_elements_by_xpath(
            signuppagemap["SignUpFacebookAccountTabXpath"])) else False