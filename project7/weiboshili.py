import selenium
from selenium import webdriver
from time import sleep
import csv

url1='https://chart.weibo.com/chart'#明星势力榜内地榜
url2='https://club.starvip.weibo.com/demo?rank_type=3&version=v1'#明星势力榜港澳台榜
url3="https://chart.weibo.com/chart?rank_type=6&version=v1"#明星势力榜新星榜

urls=[]
urls.append(url1)
urls.append(url2)
urls.append(url3)
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
def weibo(url):
    driver.get(url)
    sleep(10)
    rank=[]
    name = []
    for x in range(4):
         sleep(1)
         i=0
         while True:
            a=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[{}]/div[2]/div[2]/div[1]/div[1]/div/a".format(i+1)).text
            #b=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/a").text
            rank.append(x*25+(i+1))
            name.append(a)
            i=i+1
            if i == 25:
                break
         driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[26]/div/a[6]").click()
    dict_weibo_dalu=dict(zip(rank,name))
    return [rank,name]

str1=weibo(url1)
str2=weibo(url2)
str3=weibo(url3)

with open("weiboshili.csv",'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['内地'," ","港澳台",' ','新星'])
    for i in range(len(str1[0])):
        writer.writerow([str1[0][i],str1[1][i],str2[0][i],str2[1][i],str3[0][i],str3[1][i]])






