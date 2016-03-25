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
from uimaps import loginpagemap
from pages.basepage import BasePage,IncorrectPageException

class LogInPage(BasePage):
    def __init__(self, driver):
        super(LogInPage, self).__init__(driver)
    
    def _verify_page(self):
        try:
            self.wait_for_element_visibility(50, 'xpath', loginpagemap["SignInTabXpath"])
        except:
            raise IncorrectPageException
        
    def email_login(self):
        self.find_element('xpath', loginpagemap["SignInTabXpath"]).click()
        self.wait_for_element_visibility(50, 'xpath', loginpagemap["LogInFormDivXpath"])
        if self.find_element('xpath', loginpagemap["CookieAlertXpath"]):
            self.find_element('xpath', loginpagemap["CookieAlertXpath"]).click()
        try:
            self.wait_for_element_visibility(50, 'xpath', loginpagemap["LogInFormDivXpath"])
        except:
            self.driver.get(general_constants["base_url"]+'login')
        self.wait_for_element_visibility(50, 'xpath', loginpagemap["LogInFormDivXpath"])
        self.fill_out_field('xpath', loginpagemap["LogInFormEmailXpath"],\
                            LogInPageConstants.login_constants["username"])
        self.fill_out_field('xpath', loginpagemap["LogInFormPasswordXpath"],\
                            LogInPageConstants.login_constants["password"])
        self.click(10, 'xpath', loginpagemap["LogInFormSubmitXpath"])
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(\
            (By.XPATH,loginpagemap["LogInFormAccountTabXpath"])))
        return True if bool(self.driver.find_elements_by_xpath(\
            loginpagemap["LogInFormAccountTabXpath"])) else False
    
    def facebook_login(self):
        self.find_element('xpath', loginpagemap["SignInTabXpath"]).click()
        self.wait_for_element_visibility(50, 'xpath', loginpagemap["LogInFacebookXpath"])
        if self.find_element('xpath', loginpagemap["CookieAlertXpath"]):
            self.find_element('xpath', loginpagemap["CookieAlertXpath"]).click()
        try:
            self.wait_for_element_visibility(50, 'xpath', loginpagemap["LogInFacebookXpath"])
        except:
            self.driver.get(general_constants["base_url"]+'login')
        self.click(5,'xpath', loginpagemap["LogInFacebookXpath"])
        WebDriverWait(self.driver,20).until(lambda x: len(x.window_handles)>1)
        self.driver.switch_to_window(self.driver.window_handles[-1])    
        self.driver.find_element_by_xpath(loginpagemap["LogInFacebookUsernameXpath"]).send_keys\
            (LogInPageConstants.faceebook_login_constants["username"])
        self.driver.find_element_by_xpath(loginpagemap["LogInFacebookUsernameXpath"]).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(loginpagemap["LogInFacebookPasswordXpath"]).click()
        self.driver.find_element_by_xpath(loginpagemap["LogInFacebookPasswordXpath"]).\
            send_keys(LogInPageConstants.faceebook_login_constants["password"])
        self.driver.find_element_by_xpath(loginpagemap["LogInFacebookLoginXpath"]).click()
        self.driver.switch_to_window(self.driver.window_handles[0])
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(\
            (By.XPATH,loginpagemap["LogInFormAccountTabXpath"])))
        return True if bool(self.driver.find_elements_by_xpath(\
            loginpagemap["LogInFormAccountTabXpath"])) else False
