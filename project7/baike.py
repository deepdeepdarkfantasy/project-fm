import selenium
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
# 最大化窗口
urls=[]
urls.append("https://baike.baidu.com/starrank?")
driver.maximize_window()
print()
for url in urls:
    driver.get(url)
    sleep(10)
    rank=[]
    name = []
    for x in range(10):
         sleep(1)
         i=0
         while True:
            a=driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/table/tbody/tr[{}]/td[2]/a/div[2]/p[1]".format(i+1)).text
            rank.append(x*20+(i+1))
            name.append(a)
            i=i+1
            if i == 20:
                break
         driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/a[8]").click()

    print(rank)
    print(name)





