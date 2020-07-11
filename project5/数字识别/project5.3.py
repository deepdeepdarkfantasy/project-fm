import time
from sklearn.svm import SVC
import sklearn.preprocessing as SP
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
'''
-----------------------------------------------------------
识别手写数字
v_img=[]
image1=cv2.imread('1.png')
image1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
ax=cv2.resize(image1,(28,28))
cv2.imshow('resize0',ax)
cv2.waitKey()
for x in ax:
    for y in x:
        v_img.append(255-y)
v_img=SP.StandardScaler().fit_transform([v_img])
print(v_img)
----------------------------------------------------------
'''

with open('train-images.idx3-ubyte','rb') as f1:
    file1 = f1.read()
with open('train-labels.idx1-ubyte','rb') as f2:
    file2 = f2.read()
with open('t10k-images.idx3-ubyte','rb')  as f3:
    file3 = f3.read()
with open("t10k-labels.idx1-ubyte",'rb')  as f4:
    file4 = f4.read()

    #image1 = [int(item.encode('hex'), 16) for item in file1[16:16 + 784]]
    images_features=[]
    images_labels=[]
#---------------------------------------
    images_features_pre=[]
    images_labels_pre=[]

#---------------------------------------
    i_train=60000
    i_pre=10000
#这里使用了全部的数据，所以需要一定的训练时间以及预测时间。

    for item in file2[8:i_train+8]:
        images_labels.append(item)
    for i in range(0,i_train):
        image1=[]
        for item in file1[16+28*28*i:16+28*28*(i+1)]:
            image1.append(item)
        images_features.append(image1)

    for item in file4[8:i_pre+8]:
        images_labels_pre.append(item)
    for i in range(0,i_pre):
        image2=[]
        for item in file3[16+28*28*i:16+28*28*(i+1)]:
            image2.append(item)
        images_features_pre.append(image2)

x=SP.StandardScaler().fit_transform(images_features)
x1=SP.StandardScaler().fit_transform(images_features_pre)
#标准化


print("开始训练-------")
clf = SVC(kernel='rbf',C=10,gamma='scale')
start_time=time.time()
clf.fit(x,images_labels)
end_time=time.time()
print("训练结束-------")
print('训练时长：',end_time-start_time)
print("开始预测-------")
images_labels_predict=clf.predict(x1)
print(images_labels_predict)
#print(images_labels_pre)
print("accuracy_score：",accuracy_score(images_labels_pre,images_labels_predict))
print("precision_score：",precision_score(images_labels_pre,images_labels_predict,average='micro'))
print("recall-score：",recall_score(images_labels_pre,images_labels_predict,average='micro'))
print("f1-score：",f1_score(images_labels_pre,images_labels_predict,average='macro'))




