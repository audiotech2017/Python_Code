from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import time #引入time库
from datetime import datetime 
from selenium.webdriver.support import expected_conditions as EC #配置等待wait until
from selenium.webdriver.support.wait import WebDriverWait #imort webdriver wait
from selenium.webdriver.chrome.options import Options #加载策略
from selenium.webdriver.support.ui import Select

def main():
    Timeout = 5 
    SmallTimeout = 1
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome()#打开谷歌浏览器
    driver.get('http://guoxiang.wu:Jv111111@172.21.5.21/CAisd/pdmweb.exe')#打开CA Service SYstem
    driver.maximize_window()
    time.sleep(SmallTimeout)
    iframe1=driver.find_element(By.XPATH,'/html/frameset/frame[1]') #找到单据编号输入Textbox 需要先定位iframe
    iframe2=driver.find_element(By.XPATH,'/html/frameset/frame[2]')
    iframe3=driver.find_element(By.XPATH,'/html/frameset/frame[3]')
    #driver.switch_to.frame(iframe1) #切换到指定iframe
    js = 'document.getElementById("tbarDiv0")'
    elements=driver.execute_script(js)
    if (elements == None ):
        print('element not found')
    js = 'window.alert("sometext")'
    driver.execute_script(js)
    #driver.switch_to.default_content() #切换回去默认的地方 不在iframe停留
    time.sleep(Timeout*60)

if __name__ == '__main__':
    main()
