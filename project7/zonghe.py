import selenium
from selenium import webdriver
from time import sleep
import csv

def weibo():
    url1 = 'https://chart.weibo.com/chart'
    url2 = 'https://club.starvip.weibo.com/demo?rank_type=3&version=v1'
    urls = []
    urls.append(url1)
    urls.append(url2)
    driver = webdriver.Chrome()
    # 最大化窗口
    driver.maximize_window()
    dict_weibo=[]
    for url in urls:
        driver.get(url)
        sleep(10)
        rank = []
        name = []
        for x in range(4):
            sleep(1)
            i = 0
            while True:
                a = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[{}]/div[2]/div[2]/div[1]/div[1]/div/a".format(i + 1)).text
                # b=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/a").text
                rank.append(x * 25 + (i + 1))
                name.append(a)
                i = i + 1
                if i == 25:
                    break
            driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[26]/div/a[6]").click()
        dict_weibo_dg = dict(zip(name, rank))
        dict_weibo.append(dict_weibo_dg)
    driver.quit()
    return dict_weibo

def weibohuati():
    str = '/html/body/div[1]/article/section/div[2]/div/div[{}]/a/div/div/div[2]/div[1]/em'
    st2 = '/html/body/div[1]/article/section/div[2]/div/div[3]/a/div/div/div[2]/div[1]/em'
    urls = []
    urls.append('https://huati.weibo.cn/discovery/super?extparam=ctg1_2%7Cscorll_1&luicode=10000011&lfid=100803_-_super&sourceType=weixin')
    driver = webdriver.Chrome()
    # 最大化窗口
    driver.maximize_window()
    for url in urls:
        driver.get(url)
        sleep(1)
        rank = []
        name = []
        for x in range(1):
            sleep(1)
            i = 0
            while True:
                a = driver.find_element_by_xpath(str.format(i + 2)).text
                target = driver.find_element_by_xpath(str.format(i + 2))
                driver.execute_script("arguments[0].scrollIntoView();", target)
                # b=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/a").text
                rank.append([i + 1])
                name.append(a)
                i = i + 1
                if i == 100:
                    break
        dict_weibohuati = dict(zip(name,rank ))
        driver.quit()
        return dict_weibohuati

def buluo():
    str = "/html/body/div[1]/div/div[2]/div[2]/div/ul/li[{}]/div/div[1]/a"
    url = "https://buluo.qq.com/p/category.html?cateid=1"
    urls = []
    urls.append(url)
    driver = webdriver.Chrome()
    # 最大化窗口
    driver.maximize_window()
    for url in urls:
        driver.get(url)
        sleep(10)
        rank = []
        name = []
        for x in range(1):
            sleep(1)
            i = 0
            while True:
                try:
                    a = driver.find_element_by_xpath(str.format(i + 1)).text
                    target = driver.find_element_by_xpath(str.format(i + 1))
                    driver.execute_script("arguments[0].scrollIntoView();", target)
                    # b=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/a").text
                    rank.append((i + 1))
                    name.append(a)
                    i = i + 1
                except selenium.common.exceptions.NoSuchElementException as e:
                    print("爬取完毕")
                    break
    dict1=dict(zip(name,rank))
    driver.quit()
    return dict1

def xunyi():
    url = 'https://www.xunyee.cn/rank-person-index-0-page-{}.html'
    driver = webdriver.Chrome()
    # 最大化窗口
    driver.maximize_window()
    rank = []
    name = []
    for x in range(20):
        driver.get(url.format(x + 1))
        sleep(1)
        i = 0
        while True:
            a = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/a[{}]/span[2]".format(i + 1)).text
            # b=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/a[2]/span[2]").text
            rank.append(x * 15 + (i + 1))
            name.append(a)
            i = i + 1
            if i == 15:
                break
    dict1=dict(zip(name,rank))
    driver.quit()
    return dict1

def baike():
    driver = webdriver.Chrome()
    # 最大化窗口
    urls = []
    urls.append("https://baike.baidu.com/starrank?")
    driver.maximize_window()
    for url in urls:
        driver.get(url)
        sleep(1)
        rank = []
        name = []
        for x in range(10):
            sleep(1)
            i = 0
            while True:
                a = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/table/tbody/tr[{}]/td[2]/a/div[2]/p[1]".format(i + 1)).text
                rank.append(x * 20 + (i + 1))
                name.append(a)
                i = i + 1
                if i == 20:
                    break
            driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/a[8]").click()
    dict1=dict(zip(name,rank))
    driver.quit()
    return dict1
dict_weibo=weibo()
dict_buluo=buluo()
dict_weibohuati=weibohuati()
dict_xunyi=xunyi()
dict_baike=baike()
for i in dict_weibohuati.keys():
    jdg=0
    for j in dict_weibo[0].keys():
        if i in j:
            dict_weibohuati[i].append(dict_weibo[0][j])
            jdg=1
            break
    if jdg==0:
        dict_weibohuati[i].append(" ")
    jdg=0
    for j in dict_weibo[1].keys():
        if i in j:
            dict_weibohuati[i].append(dict_weibo[1][j])
            jdg = 1
            break
    if jdg == 0:
        dict_weibohuati[i].append(" ")
    jdg = 0
    for j in dict_baike.keys():
        if i in j:
            dict_weibohuati[i].append(dict_baike[j])
            jdg = 1
            break
    if jdg == 0:
        dict_weibohuati[i].append(" ")
    jdg = 0
    for j in dict_buluo.keys():
        if i in j:
            dict_weibohuati[i].append(dict_buluo[j])
            jdg = 1
            break
    if jdg == 0:
        dict_weibohuati[i].append(" ")
    jdg = 0
    for j in dict_xunyi.keys():
        if i in j:
            dict_weibohuati[i].append(dict_xunyi[j])
            jdg = 1
            break
    if jdg == 0:
        dict_weibohuati[i].append(" ")
    jdg = 0


print(dict_weibohuati)

with open("datas.csv",'w',newline='') as csvfile:
    writer =csv.writer(csvfile)
    writer.writerow(["艺人名字","微博-明星超话榜","微博-明星势力榜（内地榜）","微博-明星势力榜（港澳台榜）","百度-中国内地明星榜","QQ-兴趣部落明星榜","寻艺",])
    for i in range(len(dict_weibohuati)):
        cv2=[list(dict_weibohuati.keys())[i]]
        for i in (list(dict_weibohuati.values())[i]):
            cv2.append(i)
        print(cv2)
        writer.writerow(cv2)




'''
for i in a.keys():
    print(a[i])
    if i  in b.keys():
        a[i].append(b[i])
    else:
        a[i].append(" ")
print(a)
'''


