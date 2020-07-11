import csv
from bs4 import BeautifulSoup
import requests

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cookie':'Hm_lvt_2ce94714199fe618dcebb5872c6def14=1593491041; Hm_lpvt_2ce94714199fe618dcebb5872c6def14=1593491041'
}
response = requests.get('http://www.zuihaodaxue.cn/subject-ranking/education.html',headers=headers)
response.encoding='utf-8'
html=response.content
soup=BeautifulSoup(html,'html.parser')
with open('uc.csv','w',encoding='utf-8-sig',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['世界排名','学校','国家/地区',"国家地区排名",'总分','指标得分'])
    ua=soup.find('tbody').find_all('tr')
    #print(ua[1])
    for i in ua:
        row=[]
        uat=i.find_all('td')
        #(uat[3].text).replace("-","~")
        for j in range(6):
            if j==2:
                row.append(uat[2].find('img')['title'])
            elif j == 3:
                row.append((uat[j].text).replace("-","~"))
            else:
                row.append(uat[j].text)
        print(row)
        writer.writerow(row)