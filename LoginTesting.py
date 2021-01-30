from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

class LoginTesting(object):

    def __init__(self, driverLink):
        pass
        self.driver = ""
        self.driverLink = driverLink

    def driverInitializer(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
      
    def driverGet(self):
        self.driver.get(self.driverLink)

    def driverQuit(self):
        self.driver.quit()
    
    def getDriver(self):
        return self.driver


# Login test methods

    def login(self, driver, username, password):            
            try:
                driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
                nameField = driver.find_element_by_xpath("//input[@id='username']")
                passField = driver.find_element_by_xpath("//input[@id='password']")
                passField.clear()
                nameField.clear()
                nameField.send_keys(username)
                passField.send_keys(password)
                driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
                time.sleep(1)
                if( driver.find_element_by_xpath("//div[@class='profile-rail-card__actor-link t-16 t-black t-bold']").get_attribute('innerHTML') is not None):
                   return {'TestCaseID': "", 'Result': "login passed", 'Status': ""}
            except:
                return {'TestCaseID': "", 'Result': "login failed", 'Status': ""}
               
    
    def logout(self, driver): 
        try:
            time.sleep(2)
            driver.find_element_by_xpath("//header[@class='msg-overlay-bubble-header']").click()
            time.sleep(2)
            driver.find_element_by_xpath("//header[@id='global-nav']//div[2]//nav[1]//ul[1]//li[6]/div[1]//button[1]").click()
            time.sleep(1) 
            driver.find_element_by_xpath("//header[@id='global-nav']//div[2]//nav[1]//ul[1]//li[6]/div[1]//div[1]/div[1]//ul[1]//li[3]//a[1]").click()
            return {'TestCaseID': "", 'Result': "logout passed", 'Status': ""}
        except:
             return {'TestCaseID': "", 'Result': "logout failed", 'Status': ""}

    def wrongInput(self,driver, username, password, wrongInput):
        try:
            driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
            nameField = driver.find_element_by_xpath("//input[@id='username']")
            passField = driver.find_element_by_xpath("//input[@id='password']")
            passField.clear()
            nameField.clear()
            nameField.send_keys(username)
            passField.send_keys(password)
            driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()

            if wrongInput == "email":
                time.sleep(5)
                isTrue = driver.find_element_by_xpath("//a[normalize-space()='Join now']").get_attribute('innerHTML') is not None                
                print(isTrue) 
                if isTrue:
                    return {'TestCaseID': "", 'Result': "wrong email passed", 'Status': ""}
            
            elif wrongInput == 'password':
                isTrue = driver.find_element_by_xpath("//div[@id='error-for-password']") is not None
                if isTrue: 
                   return {'TestCaseID': "", 'Result': "wrong password passed", 'Status': ""}
        except Exception as e:
            print(e)
            return {'TestCaseID': "", 'Result': "wrong input failed", 'Status': ""}




































            # if wrongInput == "email":
            #     isTrue = driver.find_element_by_xpath("//a[normalize-space()='Join now']").get_attribute('innerHTML') == "Join Now" 
            #     if isTrue:
            #         return {'TestCaseID': "", 'Result': "wrong email passed", 'Status': ""}