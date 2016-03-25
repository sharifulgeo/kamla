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

class CreateOfferPage(BasePage):
    def __init__(self, driver):
        super(CreateOfferPage, self).__init__(driver)
    
    def _verify_page(self):
        try:
            self.wait_for_element_visibility(50, 'xpath', loginpagemap["SignInTabXpath"])
        except:
            raise IncorrectPageException
        
    def createmyoffer(self):
        self.instance_driver.find_element_by_xpath("//span[contains(text(),'Find Roommates')]").click()
        offer_web_element = self.instance_driver.find_element_by_xpath("//a[contains(text(),'Create Offer')]")
        #time.sleep(2)
        #self.instance_driver.find_element_by_xpath("//a[contains(text(),'Create Offer')]").click()
        #self.instance_driver.find_element_by_xpath("//a[contains(text(),'Create Offer')]").send_keys(Keys.ENTER)
        self.instance_driver.get(offer_web_element.get_attribute('href'))
        commonWorker(self.instance_driver).waitforLoading("//h2[contains(text(),'Address')]", 'Error Creating Offer')
        return 0

    def filladdress(self, address, district, floor):
        try:
            address.decode('utf-8')
        except:
            pass       
        self.instance_driver.find_element_by_xpath("//input[@placeholder = 'Address']").send_keys(address)
        time.sleep(2)
        self.instance_driver.find_element_by_xpath("//input[@placeholder = 'Address']").send_keys(Keys.DOWN)
        time.sleep(2)
        self.instance_driver.find_element_by_xpath("//input[@placeholder = 'Address']").send_keys(Keys.ENTER)

        #self.instance_driver.find_element_by_xpath("//input[@placeholder = 'District']").send_keys(district)
        self.instance_driver.find_element_by_xpath("//select[@name = 'floor']").click()
        self.instance_driver.find_element_by_xpath("(//select[@name = 'floor']//option)[3]").click()
        return 0

    def filltheroom(self, from_dateRoom, room_size, to_dateRoom, room_rent):
        self.instance_driver.find_element_by_xpath("//span[contains(text(),'Free from')]/ancestor::label/following-sibling::input[1]").click()
        self.instance_driver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(from_dateRoom)).click()
        self.instance_driver.find_element_by_xpath("//input[@name = 'room_size']").send_keys(room_size)

        self.instance_driver.find_element_by_xpath("//select[@name = 'roommates']").click()
        self.instance_driver.find_element_by_xpath("(//select[@name = 'roommates']//option)[3]").click()
        self.instance_driver.find_element_by_xpath("//select[@name = 'roommates_female']").click()
        self.instance_driver.find_element_by_xpath("(//select[@name = 'roommates_female']//option)[3]").click()
        self.instance_driver.find_element_by_xpath("//select[@name = 'roommates_male']").click()
        self.instance_driver.find_element_by_xpath("(//select[@name = 'roommates_male']//option)[3]").click()

        self.instance_driver.find_element_by_xpath("//span[contains(text(),'Free until')]/ancestor::label/following-sibling::input[1]").click()
        self.instance_driver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(to_dateRoom)).click()
        self.instance_driver.find_element_by_xpath("//input[@name = 'rent']").send_keys(room_rent)

        return 0

    def filltheflat(self, from_dateFlat, flat_size, number_rooms, to_dateFlat, flat_rent):
        self.instance_driver.find_element_by_xpath("//button[contains(text(),'Apartment')]").click()
        self.instance_driver.find_element_by_xpath("//span[contains(text(),'Free from')]/ancestor::label/following-sibling::input[1]").click()
        self.instance_driver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(from_dateFlat)).click()
        self.instance_driver.find_element_by_xpath("//input[@name = 'flat_size']").send_keys(flat_size)
        self.instance_driver.find_element_by_xpath("//input[@name = 'room_count']").send_keys(number_rooms)

        self.instance_driver.find_element_by_xpath("//span[contains(text(),'Free until')]/ancestor::label/following-sibling::input[1]").click()
        self.instance_driver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(to_dateFlat)).click()
        self.instance_driver.find_element_by_xpath("//input[@name = 'rent']").send_keys(flat_rent)
        self.instance_driver.find_element_by_xpath("//button[contains(text(), 'Next Step')]").click()
        commonWorker(self.instance_driver).waitforLoading("//label[contains(text(),'Offer title')]", 'Error Filling Description Information')
        return 0

    def filldescription(self, description_title, location_description_label, flat_description):
        self.instance_driver.find_element_by_xpath("//div[@class = 'form-group form-group-depth-1']//input[@name='title']").send_keys(description_title)
        self.instance_driver.find_element_by_xpath("//div[@class = 'tab-content']//textarea[@name='description_location']").send_keys(location_description_label)
        self.instance_driver.find_element_by_xpath("//div[@class = 'form-group form-group-depth-1']/following-sibling::div[1]//a[contains(text(),'Flat')]").click()
        self.instance_driver.find_element_by_xpath("//div[@class = 'form-group form-group-depth-1']/following-sibling::div[1]//textarea[@name='description_flat']").send_keys(flat_description)
        return 0
    
    def fillhighlights(self, highlight_1, highlight_2, highlight_3):
        self.instance_driver.find_element_by_xpath("(//div[@class = 'col-md-8']//input)[1]").send_keys(highlight_1)
        self.instance_driver.find_element_by_xpath("(//div[@class = 'col-md-8']//input)[2]").send_keys(highlight_2)
        self.instance_driver.find_element_by_xpath("(//div[@class = 'col-md-8']//input)[3]").send_keys(highlight_3)
        self.instance_driver.find_element_by_xpath("//button[contains(text(), 'Next Step')]").click()
        commonWorker(self.instance_driver).waitforLoading("//h2[contains(text(),'Offer questions')]", 'Error Filling Description Information')
        return 0

    def filllookingfor(self, question_1, question_2, question_3):
        self.instance_driver.find_element_by_xpath("//input[@label='Question 1']").send_keys(question_1)
        self.instance_driver.find_element_by_xpath("//input[@label='Question 2']").send_keys(question_2)
        self.instance_driver.find_element_by_xpath("//input[@label='Question 3']").send_keys(question_3)
        self.instance_driver.find_element_by_xpath("//button[contains(text(), 'Next Step')]").click()
        commonWorker(self.instance_driver).waitforLoading("//button[contains(text(),'Done!')]", 'Error Filling Looking For Information')
        return 0
    
    def uploadimage(self, image_path):
        self.instance_driver.find_element_by_xpath("//input[@type = 'file']").send_keys(image_path)
        commonWorker(self.instance_driver).waitforLoading("//a[@class='fancybox-thumb thumbnail']", 'Error Uploading Image')
        self.instance_driver.find_element_by_xpath("//button[contains(text(), 'Done!')]").click()
        commonWorker(self.instance_driver).waitforLoading("//div[@id='tabs-list']", 'Error Uploading Image')
        return 0