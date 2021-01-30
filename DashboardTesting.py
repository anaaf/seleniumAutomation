import time
import uuid 

class DashboardTesting(object):

    def  __init__(self, report):
            self.report = report
    

    def messageSendingTest(self, driver, navigateUrl, message):
        try:
            currentURL = driver.current_url
            print(currentURL)
            navigateURL = currentURL.replace('feed/?trk=guest_homepage-basic_nav-header-signin', navigateUrl )
            driver.get(navigateURL)
            time.sleep(5)
            driver.find_element_by_xpath("//button[@class='msg-overlay-bubble-header__button truncate ml2']").click()
            driver.find_element_by_xpath("//a[normalize-space()='Message']").click()
            driver.find_element_by_xpath("//div[@aria-label='Write a message…']").send_keys(message)
            time.sleep(2)
            driver.find_element_by_xpath("//button[normalize-space()='Send']").click()   
            return {'TestCaseID': "", 'Result': "message send passed", 'Status': ""}
        except:
          return {'TestCaseID': "", 'Result': "message send failed", 'Status': ""}



    def viewProfileTest(self, driver):
        try:
            time.sleep(2)
            driver.find_element_by_xpath("//button[@class='msg-overlay-bubble-header__button truncate ml2']").click()
            time.sleep(5)
            driver.find_element_by_xpath("//header[@id='global-nav']//div[2]//nav[1]//ul[1]//li[6]/div[1]//button[1]").click()
            time.sleep(2)
            driver.find_element_by_xpath("//header[@id='global-nav']//div[2]//nav[1]//ul[1]//li[6]/div[1]//div[1]//div[1]//header[1]//a[2]").click()
            time.sleep(2)
            isOpened = driver.find_element_by_xpath("//li[@class='inline t-24 t-black t-normal break-words']") is not None
            if isOpened:
                return {'TestCaseID': "", 'Result': "profile open passed", 'Status': ""}
        except Exception as e :
            print(e)
            return {'TestCaseID': "", 'Result': "profile open failed", 'Status': ""}
        
    def postingTest(self, driver, postContent):
        try:
            time.sleep(2)
            driver.find_element_by_xpath("//button[normalize-space()='Start a post']").click()
            print(postContent)
            driver.find_element_by_xpath("//div[@aria-label='What do you want to talk about?']").send_keys(postContent+ " " +str(uuid.uuid1()))
            time.sleep(0.5)
            driver.find_element_by_xpath("//div[@id='artdeco-modal-outlet']//div[1]//div[1]//div[2]//div[1]//div[2]//div[3]//button[1]").click()
            time.sleep(2)
            isTrue = driver.find_element_by_xpath("//p[@role='alert']//span[1]").get_attribute('innerHTML') is not None 
            if isTrue :
                return {'TestCaseID': "", 'Result': "posting test passed", 'Status': ""}
        except:
                return {'TestCaseID': "", 'Result': "posting test failed", 'Status': ""}