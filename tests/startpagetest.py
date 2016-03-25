# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from commonworker import CommonWorker


class StartupPageCheck(unittest.TestCase):    
    @classmethod
    def setUpClass(cls):
        cls.instance_driver = webdriver.Chrome()
        cls.instance_driver.maximize_window()
        cls.url = 'http://wgcast:7JxwZkCwK@wgcast2013.webfactional.com/'
        cls.test_url = url
        cls.city_name = 'Berlin, Deutschland'
        cls.login_name = 'testuser@yahoo.com'
        cls.login_pass = '1234'        
        
    @classmethod  
    def tearDownClass(cls):
        cls.instance_driver.quit()
        
    def test_email_login(self):
        test_url = self.test_url
        user_name = self.login_name
        user_password = self.login_pass
        self.instance_driver.get(test_url)
        CommonWorker(self.instance_driver).waitforLoading("//li/a[contains(text(),'Sign In')]", 'Error Logging in Page')
        self.instance_driver.find_element_by_xpath("//li/a[contains(text(),'Sign In')]").click()
        try:
            self.instance_driver.find_element_by_xpath("//a[@class = 'cc_btn cc_btn_accept_all']").click()
        except:
            pass
        CommonWorker(self.instance_driver).waitforLoading("//h2[contains(text(),'Login using email and password')]", 'Error in Getting Login Form')
        self.instance_driver.find_element_by_xpath("//input[@name = 'email']").send_keys(user_name)
        self.instance_driver.find_element_by_xpath("//input[@name = 'password']").send_keys(user_password)
        self.instance_driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
        CommonWorker(self.instance_driver).waitforLoading("//span[contains(text(),'Account')]", 'Error getting logged in')
        return 0    
        
    def test_city_search(self):
        test_url = self.test_url
        city_name = self.city_name
        self.instance_driver.get(test_url)
        self.instance_driver.find_element_by_xpath("//input[contains(@placeholder,'Enter a location')]").send_keys(city_name)
        time.sleep(2)
        self.instance_driver.find_element_by_xpath("//input[contains(@placeholder,'Enter a location')]").send_keys(Keys.DOWN)
        time.sleep(2)
        self.instance_driver.find_element_by_xpath("//input[contains(@placeholder,'Enter a location')]").send_keys(Keys.ENTER)
        CommonWorker(self.instance_driver).waitforLoading("//h1[contains(text(),'Room offers in Berlin')]", 'Error in Searching city')
        return 0
    
if __name__ == "__main__":
    unittest.main()
    #suite = unittest.TestSuite()
    #suite.addTest(StartupPageCheck("test_email_login"))
    #suite.addTest(StartupPageCheck("test_city_search"))
    #unittest.TextTestRunner(verbosity=2).run(suite)