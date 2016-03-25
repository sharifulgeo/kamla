# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CommonWorker:
    def __init__(self, common_instance_driver_parameter):
        self.common_instance_driver = common_instance_driver_parameter
    def waitforLoading(self, element_xpath, exception_message):
        try:
            WebDriverWait(self.common_instance_driver, 50).until(EC.presence_of_element_located((
                By.XPATH, element_xpath)))
        except:
            raise Exception(exception_message)
        return 0