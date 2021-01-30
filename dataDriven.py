import pandas as pd
import numpy as np

class DataDriven():

    def __init__(self):
      pass


    def reportDF(self):
        df = pd.DataFrame(columns= ['TestCaseID', 'Result', 'Status'])
        return df        
    
    def addingRow(self, reportRows, TestCaseID = "", Result = "", Status = ""):
          reportRows.append({'TestCaseID': TestCaseID, 'Result': Result, 'Status': Status})

    def reportGen(self, report333, rows):
          report = pd.DataFrame(rows, columns=['TestCaseID', 'Result', 'Status'])
          report.to_csv (r'C:\Users\Anaaf Mendha\Desktop\seleniumAutomation\report.csv', index = False, header=True)
    
    def data(self, src):
      users = pd.read_csv(src)
      usersList = users.values.tolist()
      return usersList



