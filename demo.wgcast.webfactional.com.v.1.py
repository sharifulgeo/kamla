import time,random,string
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#data containers

user = []
passwrd = []
emailaddress = []
#url_ = 'http://wgcast2013.webfactional.com/'

url_ = 'http://wgcast:7JxwZkCwK@wgcast2013.webfactional.com/'
driver = webdriver.Chrome()
driver.maximize_window()

class accessManagement:
    def __init__(self,drver):
        self.drver = driver
    def register(self,url):
        self.drver.get(url)
        try:
            WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'Sign Up')]")))
        except:
            raise Exception('Error loading sign-up page')
        self.drver.find_element_by_xpath("//a[contains(text(),'Sign Up')]").click()
        try:
            WebDriverWait(self.drver,10).until(lambda drver : drver.title.startswith('Register - WGcast'))
        except:
            raise Exception('Error loading registration forms')
        self.drver.find_element_by_xpath("//span[contains(text(),'Login using email and password')]").click()
        #Used try block to avoid race condition
        try:
            WebDriverWait(self.drver,50).until(EC.presence_of_element_located((By.XPATH,"//input[contains(@name,'username')]")))
        except:
            raise Exception('Error loading sign-up forms')   
        #fill up forms
        usr = ''.join(random.sample(string.ascii_lowercase, 3))
        eml = usr+'@yahoo.com'
        pas = ''.join(random.sample(string.digits, 3))
        self.drver.find_element_by_xpath("//input[contains(@name,'username')]").send_keys(usr)
        self.drver.find_element_by_xpath("//input[contains(@name,'email')]").send_keys(eml)
        self.drver.find_element_by_xpath("//input[contains(@name,'password')]").send_keys(pas)
        self.drver.find_element_by_xpath("//input[contains(@name,'password_confirmation')]").send_keys(pas)
        #cc_btn cc_btn_accept_all
        try:
            self.drver.find_element_by_xpath("//a[@class = 'cc_btn cc_btn_accept_all']").click()
        except:
            pass
        self.drver.find_element_by_xpath("//button[contains(text(),'Register')]").click()
        try:
            WebDriverWait(self.drver,50).until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Account')]")))
        except:
            raise Exception('Error getting Registered')
        user.append(usr)
        passwrd.append(pas)
        emailaddress.append(eml) 
        return 0
    
    def registerWithFacebook(self, url):
        self.drver.get(url)
        return 0
    
    def logout(self, url_parameter):        
        self.drver.get(url_parameter+'logout')
        try:
            WebDriverWait(self.drver, 50).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Sign Up')]")))
        except:
            raise Exception('Error logging out')
        return 0
    
    def login(self,user_name,pass_word):
        url_paramtr = 'http://'+user_name+':'+pass_word+'@wgcast2013.webfactional.com/'
        self.drver.get(url_paramtr)
        try:
            WebDriverWait(self.drver,50).until(EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'Sign Up')]")))
        except:
            raise Exception('Error logging out')
        return 0
    def citySearch(self):
        pass

class createOffer:
    def __init__(self,drver):
        self.drver = driver

    def createMyoffer(self):
        self.drver.find_element_by_xpath("//span[contains(text(),'Find Roommates')]").click()
        offer_web_element = self.drver.find_element_by_xpath("//a[contains(text(),'Create Offer')]")
        #time.sleep(2)
        #self.drver.find_element_by_xpath("//a[contains(text(),'Create Offer')]").click()
        #self.drver.find_element_by_xpath("//a[contains(text(),'Create Offer')]").send_keys(Keys.ENTER)
        self.drver.get(offer_web_element.get_attribute('href'))
        try:
            WebDriverWait(self.drver, 50).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Address')]")))
        except:
            raise Exception('Error Creating Offer')
        return 0

    def fillAddress(self, address, district, floor):
        self.drver.find_element_by_xpath("//input[@placeholder = 'Address']").send_keys(address)
        time.sleep(2)
        self.drver.find_element_by_xpath("//input[@placeholder = 'Address']").send_keys(Keys.DOWN)
        self.drver.find_element_by_xpath("//input[@placeholder = 'Address']").send_keys(Keys.DOWN)
        time.sleep(2)
        self.drver.find_element_by_xpath("//input[@placeholder = 'Address']").send_keys(Keys.ENTER)

        self.drver.find_element_by_xpath("//input[@placeholder = 'District']").send_keys(district)
        #self.drver.find_element_by_xpath("(//input[@name = 'District']//option)[3]").click()
        self.drver.find_element_by_xpath("//select[@name = 'floor']").click()
        self.drver.find_element_by_xpath("(//select[@name = 'floor']//option)[3]").click()
        return 0

    def fillTheroom(self, from_dateRoom, room_size, to_dateRoom, room_rent):
        self.drver.find_element_by_xpath("//span[contains(text(),'Free from')]/ancestor::label/following-sibling::input[1]").click()
        self.drver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(from_dateRoom)).click()
        self.drver.find_element_by_xpath("//input[@name = 'room_size']").send_keys(room_size)

        self.drver.find_element_by_xpath("//select[@name = 'roommates']").click()
        self.drver.find_element_by_xpath("(//select[@name = 'roommates']//option)[3]").click()
        self.drver.find_element_by_xpath("//select[@name = 'roommates_female']").click()
        self.drver.find_element_by_xpath("(//select[@name = 'roommates_female']//option)[3]").click()
        self.drver.find_element_by_xpath("//select[@name = 'roommates_male']").click()
        self.drver.find_element_by_xpath("(//select[@name = 'roommates_male']//option)[3]").click()

        self.drver.find_element_by_xpath("//span[contains(text(),'Free until')]/ancestor::label/following-sibling::input[1]").click()
        self.drver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(to_dateRoom)).click()
        self.drver.find_element_by_xpath("//input[@name = 'rent']").send_keys(room_rent)

        return 0

    def fillTheflat(self, from_dateFlat, flat_size, number_rooms, to_dateFlat, flat_rent):
        self.drver.find_element_by_xpath("//span[contains(text(),'Free from')]/ancestor::label/following-sibling::input[1]").click()
        self.drver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(from_dateFlat)).click()
        self.drver.find_element_by_xpath("//input[@name = 'flat_size']").send_keys(flat_size)
        self.drver.find_element_by_xpath("//input[@name = 'room_count']").send_keys(number_rooms)

        self.drver.find_element_by_xpath("//span[contains(text(),'Free until')]/ancestor::label/following-sibling::input[1]").click()
        self.drver.find_element_by_xpath("//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]".format(to_dateFlat)).click()
        self.drver.find_element_by_xpath("//input[@name = 'rent']").send_keys(flat_rent)
        #self.drver.find_element_by_xpath("//button[@id = 'viewOffersBtn']").click()
        self.drver.find_element_by_xpath("//button[contains(text(), 'Next Step')]").click()
        return 0

for i in range(100):
    print i
    wrker = accessManagement(driver)
    offer = createOffer(driver)
    wrker.register(url_)
    offer.createMyoffer()
    offer.fillAddress("Berlin","Germany","2")
    offer.fillTheroom(11, 2345, 25, 2340)
    offer.fillTheflat(13, 1234, 2, 12, 20)

    #wrker.logout(url_)

driver.quit()


