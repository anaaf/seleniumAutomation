from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from LoginTesting import LoginTesting
from DashboardTesting import DashboardTesting
from dataDriven import DataDriven
import time
import uuid 

dd = DataDriven()
report = dd.reportDF()

lt = LoginTesting("https://www.linkedin.com/home")
dt = DashboardTesting(report)
driver = lt.getDriver()

reportRows = []



userData = dd.data("./data.csv")
list1 = [['anaafabba00', 'abba2009'],['anaafabba00', 'abba2009'],['anaafabba00', 'abba2009']]


def messageTester(testCases):
     lt.login('anaafmendha@gmail.com', 'workondreams123')

def testCaseDriver(testCaseID, testCase, driver):

        if testCaseID == 'TC1':
            try:
               reportRows.append({'TestCaseID': testCaseID, 'Result': "", 'Status': ""})
               reportRows.append(lt.login(lt.getDriver(), testCase[0], testCase[1]))
               reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "passed"})
            except:
                reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "failed"})

        elif testCaseID == 'TC7':
            reportRows.append({'TestCaseID': testCaseID, 'Result': "", 'Status': ""})
            reportRows.append(lt.login(lt.getDriver(), testCase[0], testCase[1]))
            reportRows.append(dt.messageSendingTest(lt.getDriver(), testCase[2], "Hello Ali this is a automated msg"))
            reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "passed"})

        elif testCaseID == 'TC2':
            reportRows.append({'TestCaseID': testCaseID, 'Result': "", 'Status': ""})
            reportRows.append(lt.login(lt.getDriver(), testCase[0], testCase[1]))
            reportRows.append(lt.logout(lt.getDriver()))
            reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "passed"})
        
        elif testCaseID == 'TC5':
            reportRows.append({'TestCaseID': testCaseID, 'Result': "", 'Status': ""})
            reportRows.append(lt.login(lt.getDriver(), testCase[0], testCase[1]))
            reportRows.append(dt.viewProfileTest(lt.getDriver()))
            reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "passed"})

        elif testCaseID == 'TC3':
            reportRows.append({'TestCaseID': testCaseID, 'Result': "", 'Status': ""})
            reportRows.append(lt.wrongInput(lt.getDriver(), testCase[0], testCase[1], 'email'))
            reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "passed"})
        
        elif testCaseID == 'TC4':
            reportRows.append({'TestCaseID': testCaseID, 'Result': "", 'Status': ""})
            reportRows.append(lt.wrongInput(lt.getDriver(), testCase[0], testCase[1], 'password'))
            reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "passed"})
        
        elif testCaseID == 'TC6':
            reportRows.append({'TestCaseID': testCaseID, 'Result': "", 'Status': ""})
            reportRows.append(lt.login(lt.getDriver(), testCase[0], testCase[1]))
            time.sleep(2)
            reportRows.append( dt.postingTest(lt.getDriver(), testCase[2]))
            reportRows.append({'TestCaseID': "", 'Result': "", 'Status': "passed"})


def testDriver(testCases, rows, testCaseID):
    for index in range(rows):
            lt.driverInitializer()
            lt.driverGet()
            time.sleep(2)
            print(testCases[index][3])
            testCaseDriver(testCases[index][3], testCases[index], driver)
            lt.driverQuit()
            time.sleep(4)
    dd.reportGen(report, reportRows)
     


testDriver(userData, len(userData), 'TC7')












































































#   options = webdriver.ChromeOptions()
#         options.add_argument('--headless')
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')