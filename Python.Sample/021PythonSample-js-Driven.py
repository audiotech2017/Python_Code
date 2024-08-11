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
from pathlib import Path
# 创建Chrome浏览器实例

def login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome()
    file_path = Path(Path.cwd(), '020PythonSamle-Index.html')
    driver.get('file:///' + str(file_path))
    js = 'document.getElementById("#btn001")'
    element=driver.execute_script(js)
    if (element == None ):
        print('element not found')

if __name__ == '__main__':
    login()