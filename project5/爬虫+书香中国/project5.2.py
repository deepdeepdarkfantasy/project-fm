from selenium import webdriver
from time import sleep
import re
import requests

driver = webdriver.Chrome()
#最大化窗口
driver.maximize_window()
driver.get('http://shuxiang.chineseall.cn/v3/book/read/zrlxg/EPUB/3')
sleep(5)
wenzhang=[]
#切换到表单
while True:
    sleep(5)
    a = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]").text
    # b=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/text()[2]").text
    list_a = re.findall('\d+', a)
    print(list_a[0],list_a[1])
    sleep(5)
    driver.switch_to.frame("epubViewFrame")
    aa=driver.find_element_by_css_selector("[marginwidth='0']").text
    wenzhang.append(aa)
    driver.switch_to.default_content()  # 跳到最外层页面\
    if eval(list_a[0]) == eval(list_a[1]):
        break
    bb=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[4]/a[4]").click()
    
for i in range(len(wenzhang)):
    print(wenzhang[i])






