str='/html/body/div[1]/article/section/div[2]/div/div[{}]/a/div/div/div[2]/div[1]/em'
#    '/html/body/div[1]/article/section/div[2]/div/div[{}]/a/div/div/div[2]/div[1]/em'
#    '/html/body/div[1]/article/section/div[2]/div/div[2]/a/div/div/div[2]/div[1]/em'
st2='/html/body/div[1]/article/section/div[2]/div/div[2]]'
path_qianli=["",'/html/body/div[1]/article/section/div[2]/div/div[1]/div[1]/div/div[1]/div[2]']
import selenium
from selenium import webdriver
import  csv
from time import sleep
urls=[]
urls.append('https://huati.weibo.cn/discovery/super?extparam=ctg1_2%7Cscorll_1&luicode=10000011&lfid=100803_-_super&sourceType=weixin')
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
def get_message(xpath):
    driver.get(urls[0])
    sleep(10)
    rank=[]
    name = []
    for x in range(1):
         sleep(1)
         i=0
         try:
             driver.find_element_by_xpath(xpath).click()
         except selenium.common.exceptions.InvalidSelectorException as e:
             while True:
                    a=driver.find_element_by_xpath(str.format(i+2)).text
                    target = driver.find_element_by_xpath(str.format(i+2))
                    driver.execute_script("arguments[0].scrollIntoView();", target)
                    #b=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/a").text
                    rank.append((i+1))
                    name.append(a)
                    i=i+1
                    if i == 100:
                        break

         else:
            sleep(3)
            while True:
                a = driver.find_element_by_xpath(str.format(i + 2)).text
                target = driver.find_element_by_xpath(str.format(i + 2))
                driver.execute_script("arguments[0].scrollIntoView();", target)
                # b=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div/a").text
                rank.append((i + 1))
                name.append(a)
                i = i + 1
                if i == 100:
                    break
    dict_weibohuati=dict(zip(name,rank))
    print(dict_weibohuati)
    return [rank,name]



if __name__ =="__main__":
    str1=get_message(path_qianli[0])
    str2=get_message(path_qianli[1])
    #print(str1)

    with open("weibochaohua.csv",'w',newline='',encoding='utf-8-sig') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(["微博超话排行榜","","微博超话新星榜",""])
        for i in range(len(str1[0])):
            writer.writerow([str1[0][i],str1[1][i],str2[0][i],str2[1][i]])
           #writer.writerow([str1[0][i], str1[1][i]])











