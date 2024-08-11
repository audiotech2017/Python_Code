#引入selenium库中的 webdriver 模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import time #引入time库
from datetime import datetime 
from selenium.webdriver.support import expected_conditions as EC #配置等待wait until
from selenium.webdriver.support.wait import WebDriverWait #imort webdriver wait
from selenium.webdriver.chrome.options import Options #加载策略
#import os as os #获取系统路径信息
#from selenium.common.exceptions import TimeoutException #exception control
#下面组件是为了使用excel
#import xlrd  # pip install xlrd -i https://pypi.tuna.tsinghua.edu.cn/simple  
import books as books # pip install books -i https://pypi.tuna.tsinghua.edu.cn/simple    
import pandas as pd # pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple 
#import numpy as nd # pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple 
#from openpyxl import load_workbook # pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple 
#Pyinstaller -F -w -i chengzi.ico py_word.py
#from selenium.webdriver.chrome.service import Service

def ReadDataFromExcel():
    #print (os.getcwd ())
    with pd.ExcelFile('020PythonSample-OAAutoInq.xlsx') as xlsx:
        ExcelData = pd.read_excel (xlsx)#打开一个Excel文件
    #print(ExcelData.index) #打印以下所有要做的ESB No
    for column_name, item in ExcelData.iterrows():
        print(column_name)
        print(item)
        print(item[0])
    return ExcelData

def ExcelOutput(ExcelData):
    with pd.ExcelWriter("020PythonSample-OAAutoInqOutput.xlsx",  mode="w",  engine="openpyxl") as writer:
        ExcelData.to_excel(writer, sheet_name="Sheet1")  #extract data into Excel Document PythonSample-OAAutoLoginOutput.xlsx
    print ('*********************')
    for row_Index, row in ExcelData.iterrows():
        print(row_Index)
        print(row)
        print(row['ESB No']) #打印第一列 所有行
        print(row['ESB Log'])
        print(row['ESB Proc Timestamp'])
        for idx,item in row.items():
            print(idx,item)
    for col_Index, col in ExcelData.items():
        print(col_Index)
        print(col[0]) #打印第一行
        print(col[1])
        print(col) #打印整列
    print ('*********************')
    print (ExcelData)

    
def ChormActionScriptInquiry(ExcelData):
    Timeout = 5 
    SmallTimeout = 1
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    url = 'http://oa.cheryjaguarlandrover.com'
    driver = webdriver.Chrome() #D:\CJLR\ChormeDiver\chromedriver-win64\120.0.6099.109\chromedriver.exe 这个要在Path内配置下这样下面的命令就可以用起来了
    driver.get(url) #OA生产环境 admin1.oa/Efastserv&* #考虑到网页打开的速度取决于每个人的电脑和网速，使用time库sleep()方法，让程序睡眠5秒
    driver.maximize_window()
    WebDriverWait(driver, Timeout*60).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="usernameinput"]'))).send_keys('admin1.oa')
    time.sleep(1)
    WebDriverWait(driver, Timeout*60).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password"]'))).send_keys('Efastserv&*')
    #//*[@id="usernameinput"] 用户名输入的地方
    #driver.find_element(By.XPATH,'//*[@id="usernameinput"]').send_keys('admin1.oa')
    #driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('Efastserv&*')
    time.sleep(SmallTimeout)
    driver.find_element(By.XPATH,'//*[@id="sub"]').click()#找到合理化建议的菜单 期望他点击以后展开来
    time.sleep(SmallTimeout)
    #driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/nav/ul/li[16]/div').click()#找到合理化建议汇总查询 但是页面首次进来会有一个LoadAllData的动作 我们要等待该Load完成
    WebDriverWait(driver,60*Timeout).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/nav/ul/li[16]/div'))).click()
    time.sleep(SmallTimeout)
    #driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/nav/ul/li[16]/ul/li[3]/a/span').click()
    WebDriverWait(driver,60*Timeout).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/nav/ul/li[16]/ul/li[3]/a/span'))).click()
    iframe=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/main/div/div/iframe') #找到单据编号输入Textbox 需要先定位iframe
    driver.switch_to.frame(iframe)
    time.sleep(SmallTimeout)
    ESB_Log = []
    ESB_Proc_Timestamp = []
    ESB_Proc_Duration = []
    WebDriverWait(driver,60*Timeout).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="datagrid-row-r1-2-0"]')))
    for ESB_No in ExcelData['ESB No']:
        StartTime = datetime.now()
        driver.find_element(By.XPATH,'//*[@id="eligibleSuggestionNo"]').clear() #清空输入框
        driver.find_element(By.XPATH,'//*[@id="eligibleSuggestionNo"]').send_keys(ESB_No) #数据新号码ESB
        time.sleep(SmallTimeout)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/a[1]/span/span/span/span[1]').click()#点击页面内查询按钮
        time.sleep(SmallTimeout*3)
        try:
            element = WebDriverWait(driver,Timeout).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="datagrid-row-r1-2-0"]')))
            ESB_Log.append(ESB_No + ' ==> Process Completed...')
            EndTime = datetime.now()
            ESB_Proc_Timestamp.append(EndTime)
            Timediff = EndTime - StartTime
            ESB_Proc_Duration.append(Timediff)
            print (ESB_No + ' ==> Process is Completed... ')
        except Exception as e:
            ESB_Log.append(ESB_No + ' ==> ESB Not Found....... ')
            EndTime = datetime.now()
            ESB_Proc_Timestamp.append(EndTime)
            Timediff = EndTime - StartTime
            ESB_Proc_Duration.append(Timediff)
            print (ESB_No + ' ==> Process in Failed... ')
            print(format(e.args))
            #driver.switch_to.default_content() #切换回去默认的地方 不在iframe停留
    ExcelData['ESB Log'] = ESB_Log
    ExcelData['ESB Proc Timestamp'] = ESB_Proc_Timestamp
    ExcelData['ESB Proc Duration'] = ESB_Proc_Duration
    print (ExcelData)
    ExcelOutput(ExcelData)
    js = 'window.alert("所有数据已经处理完毕 点击确定并手动关闭网页")'
    driver.execute_script(js)
    time.sleep(Timeout*60) #To Stop the Chorme auto Close 

def main():
    ExcelData = ReadDataFromExcel() #this is to prepare input data
    print (ExcelData) #this is to review the data read from Excel
    ExcelData['ESB Log'] = '' # this is to Append a new Column for Log Purpose
    ExcelData['ESB Proc Timestamp'] = ''
    ExcelData['ESB Proc Duration'] = ''
    print (ExcelData) #this is to review the data read from Excel
    ChormActionScriptInquiry(ExcelData) #this to perform automate action list 

if __name__ == '__main__':
    main()






