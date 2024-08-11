#引入selenium库中的 webdriver 模块
#当前Chorme版本120.0.6099.217  下载的Driver版本 Version: 120.0.6099.109 (r1217362) 下载地址1 https://googlechromelabs.github.io/chrome-for-testing/ 
#pip install selenium
#from selenium import webdriver
#from selenium.webdriver import Chrome, ChromeOptions
#from selenium.webdriver.common.by import By

 
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
 
if __name__ == '__main__':
    # 初始化
    browser = webdriver.Chrome()
    # URL地址
    browser.get("https://www.baidu.com/")
    # 窗口最大化
    browser.maximize_window()
    # 根据ID填充搜索内容
    browser.find_element(By.ID, "kw").send_keys("https://blog.csdn.net/qq_19309473")
    # 模拟点击
    browser.find_element(By.ID, "su").click()
    # 不关闭浏览器
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
    time.sleep(10000)
#opt = ChromeOptions()            # 创建Chrome参数对象
#opt.add_experimental_option('detach', False) #执行完毕后不关闭浏览器
#driver = webdriver.Chrome(options=opt)
#opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
#driver = webdriver.Chrome()# Chrome浏览器

#打开谷歌浏览器

#chromedriver_path = r"C:\Program Files\Google\Chrome\Application\chromedriver-win64\120.0.6099.109\chromedriver.exe"
#service = Service(chromedriver_path)  
#driver = webdriver.Chrome(service=service)

#打开百度搜索主页

#driver.get('https://www.baidu.com')
'''
调用selenium库中的find_element_by_xpath()方法定位搜索框，
同时使用send_keys()方法在其中输入信息
'''
# inputTag = driver.find_element_by_id("value")  # 利用ID查找
# 改为：
#inputTag = driver.find_element(By.ID, "value")

#driver.find_element_by_xpath('//*[@id="kw"]').send_keys('this is a test')
#driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('this is a test')
'''
调用selenium库中的find_element_by_xpath()方法定位搜索按钮，
同时使用click()方法对按钮进行点击
'''
#driver.find_element_by_xpath('//*[@id="su"]').click()
#driver.find_element(By.XPATH,'//*[@id="su"]').send_keys('this is a test')
