path="/html/body/div[1]/div[1]/div/div[1]/div/div/div[2]"
path1="/html/body/div[1]/div/div[1]/div/div/div[2]/input"
import selenium
from selenium import webdriver
from time import sleep
url='https://weibo.com/'
def search(searchWord):
    inputBtn = driver.find_element_by_class_name("searchInp_form") #找到搜索框
    inputBtn.clear()
    inputBtn.send_keys(searchWord.strip().decode("gbk")) #输入搜索关键词
    driver.find_element_by_class_name('searchBtn').click() #点击“搜索”


driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
driver.get(url)
sleep(10)
driver.find_element_by_css_selector("#plc_top>div>div>div.gn_search_v2>input")
#search("张艺兴")

