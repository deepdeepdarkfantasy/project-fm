import pandas as pd
import matplotlib.pyplot as plt
datas = pd.read_csv('uc.csv')
d_data = datas.head(300).groupby('国家/地区')['学校'].count()
print(d_data)
plt.rcParams['font.sans-serif'] = 'SimHei'
d_data.plot(title='世界一流大学分布情况',figsize=(25,10),color='red',kind='bar')
plt.ylim(0,150)
plt.yticks(range(0,150,5))
plt.plot(edgecolor='grey',color='black')
for x,y in enumerate(d_data.values):
    plt.text(x-0.1,y+0.5,"{}".format(y))
# 保存图片
plt.savefig('1.png')
plt.show()