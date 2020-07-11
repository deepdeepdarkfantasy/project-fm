import selenium
from selenium import webdriver
from time import sleep
str="/html/body/div[1]/div/div[2]/div[2]/div/ul/li[{}]/div/div[1]/a"
url="https://buluo.qq.com/p/category.html?cateid=1"

urls=[]
urls.append(url)
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
for url in urls:
    driver.get(url)
    sleep(10)
    rank=[]
    name = []
    for x in range(1):
         sleep(1)
         i=0
         while True:
            try:
                a=driver.find_element_by_xpath(str.format(i+1)).text
                target = driver.find_element_by_xpath(str.format(i+1))
                driver.execute_script("arguments[0].scrollIntoView();", target)
                #b=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/a").text
                rank.append((i+1))
                name.append(a)
                i=i+1
            except selenium.common.exceptions.NoSuchElementException as e:
                print("爬取完毕")
                break

    print(rank)
    print(name)





