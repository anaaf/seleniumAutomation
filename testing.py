from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
# from chromedriver_py import binary_path 

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://adactinhotelapp.com/")

nameField = driver.find_element_by_id('username')
nameField.send_keys('Anaaf')
passField = driver.find_element_by_id('password')
passField.send_keys('abba109')
click = driver.find_element_by_id('login').click()


driver.find_element_by_xpath("//a[normalize-space()='New User Register Here']").click()
# ('login_register')[0].click()
