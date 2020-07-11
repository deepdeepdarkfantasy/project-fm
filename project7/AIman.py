from selenium import webdriver
import selenium
import csv
import time
from retrying import retry
search_names=[]
rank = []
score = []
def fun1(name,times):
    try:
        if times ==5:
            score.append('无')
            rank.append('无')
            return times
        driver.find_element_by_xpath(xpath).click()
        time.sleep(1)
        input_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/input')
        input_box.clear()
        input_box.send_keys(name)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div').click()
        time.sleep(1)
        driver.find_element_by_xpath(str).click()
        time.sleep(1)
        score.append(driver.find_element_by_css_selector('#slider-current > div > div > div.right > div.bottom > p:nth-child(1)').text)
        rank.append(driver.find_element_by_xpath(str2).text)
        time.sleep(1)
        driver.find_element_by_xpath(str_back1).click()
        driver.find_element_by_xpath(str_back2).click()
    except:
        times = times + 1
        driver.get('http://m.chinaindex.net/home/1')
        fun1(name,times)

def fun2(name):
    driver.find_element_by_xpath(xpath).click()
    time.sleep(5)
    input_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/input')
    input_box.clear()
    input_box.send_keys(name)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div').click()
    time.sleep(5)
    driver.find_element_by_xpath(str).click()
    time.sleep(5)
    score.append(driver.find_element_by_css_selector('#slider-current > div > div > div.right > div.bottom > p:nth-child(1)').text)
    rank.append(driver.find_element_by_xpath(str2).text)
    time.sleep(2)
    driver.find_element_by_xpath(str_back1).click()
    time.sleep(2)
    driver.find_element_by_xpath(str_back2).click()





xpath='/html/body/div[1]/div[1]/div[1]/div[3]/img[1] '
str='/html/body/div[1]/div[1]/div[3]/div/div/div'
str1='/html/body/div[1]/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p[1]'
str2='/html/body/div[1]/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p[2]'
str_back1='/html/body/div[1]/div[1]/div[1]/div/div[1]'
str_back2='/html/body/div[1]/div[1]/div[1]/div[1]'

with open('name_list.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for i in reader:
        search_names.append(i[0])
search_names[0]='杨颖'
driver= webdriver.Chrome()
driver.get('http://m.chinaindex.net/home/1')
for name in search_names:
    times=0
    #name='希林娜依高'
    fun1(name,times)

with open('result.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['姓名','得分','排名'])
    for i in range(len(search_names)):
        writer.writerow([search_names[i],score[i],rank[i]])



