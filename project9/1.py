import requests
import re
import time
cids=[207141070,203570355,185689686,119557635]
Headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
for cid in cids:
    url = 'http://comment.bilibili.com/{}.xml'
    url=url.format(cid)
    print(url)
    time.sleep(5)
    r=requests.get(url,headers=Headers)
    r=r.content.decode('utf-8')
    dt=re.compile('<d.*?>(.*?)</d>')
    tag=dt.findall(r)
    for i in range(len(tag)):
        tag[i]=tag[i]+'\n'
    print(tag)

    with open('{}.txt'.format(cid),'w',encoding='utf-8') as file:
        file.writelines(tag)
