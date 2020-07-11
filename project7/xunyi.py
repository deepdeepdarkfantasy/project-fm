import selenium
from selenium import webdriver
from time import sleep

url='https://www.xunyee.cn/rank-person-index-0-page-{}.html'
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
rank=[]
name = []
for x in range(20):
     driver.get(url.format(x+1))
     sleep(2)
     i=0
     while True:
        a=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/a[{}]/span[2]".format(i+1)).text
        #b=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/a[2]/span[2]").text
        rank.append(x*15+(i+1))
        name.append(a)
        i=i+1
        if i == 15:
            break
print(rank)
print(name)