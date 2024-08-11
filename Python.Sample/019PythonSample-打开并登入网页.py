#引入selenium库中的 webdriver 模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#引入time库
import time

#打开谷歌浏览器
driver = webdriver.Chrome()
#打开智慧树学习平台
driver.get('https://www.zhihuishu.com/')
'''
考虑到网页打开的速度取决于每个人的电脑和网速，
使用time库sleep()方法，让程序睡眠5秒
'''
time.sleep(1)
driver.maximize_window()
#在主页面点击登录按钮，进入登录页面
driver.find_element(By.ID, "notLogin").click()
#输入账号和密码
driver.find_element(By.XPATH,'//*[@id="lUsername"]').send_keys('这是我的测试账号')
driver.find_element(By.XPATH,'//*[@id="lPassword"]').send_keys('这是我的测试密码')
#点击登录按钮
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="f_sign_up"]/div[1]/span').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="qSignup"]').click()
time.sleep(999999)



