import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def equi_width_excel(count_number_age,labels_age):
    for i in range (2661-len(labels_age)):
        labels_age.append('')
    for i in range (2661-len(count_number_age)):
        count_number_age.append('')
    with open('test.csv','r') as csvfile:
        rows=csv.reader(csvfile)
        with open('test2.csv', 'w', newline='') as f:
         writer = csv.writer(f)
         i=0
         for row in rows:
            row.append(labels_age[i])
            writer.writerow(row)
            i=i+1
         i=0
         for row in rows:
            row.append(count_number_age[i])
            writer.writerow(row)
            i=i+1


def equi_depth_excel(xx,yy):
    for i in range (2661-len(xx)):
        xx.append('')
    for i in range (2661-len(yy)):
        yy.append('')
    with open('test.csv','r') as csvfile:
        rows=csv.reader(csvfile)
        with open('test2.csv', 'w', newline='') as f:
         writer = csv.writer(f)
         i=0
         for row in rows:
            row.append(xx[i])
            writer.writerow(row)
            i=i+1
         i=0
         for row in rows:
            row.append(yy[i])
            writer.writerow(row)
            i=i+1


def discretisation_excel(xx,count_number_age):
    for i in range (2661-len(xx)):
        xx.append('')
    for i in range (2661-len(count_number_age)):
        count_number_age.append('')
    with open('test.csv','r') as csvfile:
        rows=csv.reader(csvfile)
        with open('test2.csv', 'w', newline='') as f:
         writer = csv.writer(f)
         i=0
         for row in rows:
            row.append(xx[i])
            writer.writerow(row)
            i=i+1
         i=0
         for row in rows:
            row.append(count_number_age[i])
            writer.writerow(row)
            i=i+1

def equi_width_plot(xx,yy):
    width=8
    ind = [15,25,35,45,55,65,75,85]
    print(ind)
    # make a square figure
    fig = plt.figure(333)
    ax = fig.add_subplot(111)
    # Bar Plot
    tt=plt.bar(ind, yy,width, color='yrbg')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(xx)
    # labels
    ax.set_xlabel('age')
    ax.set_ylabel('numbers')
    # title
    for a,b in zip(ind,yy):
        if b <10:
            plt.text(a-0.5,b+20,'%d'%b)
            plt.gca().add_patch(plt.Rectangle((a - 3, b), 6, 50,edgecolor='grey',facecolor='white'))
        if b>=10 and b<= 99:
            plt.text(a-1,40,'%d'%b)
            plt.gca().add_patch(plt.Rectangle((a - 3,20 ), 6, 50, edgecolor='grey',facecolor='white'))
        if b>=100:
            plt.text(a-2,120,'%d'%b)
            plt.gca().add_patch(plt.Rectangle((a-3,100),6,50,edgecolor='grey',facecolor='white'))
    #ax.set_title('bins', bbox={'facecolor': '0.8', 'pad': 5})
    plt.grid(True)
    plt.show()

def equi_depth_plot(sum_age,all_age):
    width=8
    all_age=sorted(all_age)
    ind=[]
    yy=[]
    sum_part_age=0
    c1=0
    t_v=0
    for i in range(len(all_age)):
        t_v=t_v+1
        if t_v ==len(all_age)/4:
            ind.append(all_age[i])
            t_v=0
            yy.append(i+1)
    for i in range(len(yy)):
        if i == len(yy)-1:
            break
        else:
            yy[len(yy)-i-1]=yy[len(yy)-i-1]-yy[len(yy)-i-2]
    xx=[]
    for i in range(len(ind)):
        if i == 0:
            xx.append('(0,%d]'%ind[i])
            xx.append('({},{}]'.format(ind[i], ind[i + 1]))
            continue
        if i == 2:
            xx.append('(%d,90]'%ind[i])
            break
        xx.append('({},{}]'.format(ind[i],ind[i+1]))
    print(xx)
    fig = plt.figure(333)
    ax = fig.add_subplot(111)
    # Bar Plot
    tt=plt.bar(ind, yy,width, color='yrbg')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(xx)
    # labels
    ax.set_xlabel('age')
    ax.set_ylabel('numbers')
    # title
    for a,b in zip(ind,yy):
        if b <10:
            plt.text(a-0.5,1,'%d'%b)
        if b>=10 and b<= 99:
            plt.text(a-1,1,'%d'%b)
        if b>=100:
            plt.text(a-2,120,'%d'%b)
        plt.gca().add_patch(plt.Rectangle((a-3,100),6,50,edgecolor='grey',facecolor='white'))
    #ax.set_title('bins', bbox={'facecolor': '0.8', 'pad': 5})
    plt.grid(True)
    plt.show()
    equi_depth_excel(xx,yy)

def discretise(d):
    count_number_age=[]
    Child=0
    Teenager=0
    Young_adult=0
    Middle_aged=0
    Old_aged=0
    for line in d:
        if line[1].isdigit()==False:
            continue
        if eval(line[1]) >= 0 and eval(line[1]) <= 12:
         Child = Child+ 1
        if eval(line[1]) >=13 and eval(line[1]) <= 19:
         Teenager = Teenager + 1
        if eval(line[1]) >= 20 and eval(line[1]) <= 39:
         Young_adult = Young_adult + 1
        if eval(line[1]) >= 40 and eval(line[1]) <= 59:
         Middle_aged = Middle_aged + 1
        if eval(line[1]) >= 60:
         Old_aged = Old_aged + 1
    count_number_age.append(Child)
    count_number_age.append(Teenager)
    count_number_age.append(Young_adult)
    count_number_age.append(Middle_aged)
    count_number_age.append(Old_aged)
    print(count_number_age)
    width = 8
    ind = [10,20,30,40,50]
    xx = ['Child','Teenager','Young_adult','Middle_aged','Old_aged']
    discretisation_excel(xx,count_number_age)
    print(ind)
    # make a square figure
    fig = plt.figure(333)
    ax = fig.add_subplot(111)
    # Bar Plot
    tt = plt.bar(ind, count_number_age, width, color='grey')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(xx)
    # title
    for a, b in zip(ind, count_number_age):
        if b < 10:
            plt.text(a - 0.5, b + 20, '%d' % b)
            plt.gca().add_patch(plt.Rectangle((a - 3, b), 6, 100, edgecolor='grey', facecolor='white'))
        if b >= 10 and b <= 99:
            plt.text(a - 1, 40, '%d' % b)
            plt.gca().add_patch(plt.Rectangle((a - 3, 20), 6, 100, edgecolor='grey', facecolor='white'))
        if b >= 100:
            plt.text(a - 1, 120, '%d' % b)
            plt.gca().add_patch(plt.Rectangle((a - 3, 100), 6, 100, edgecolor='grey', facecolor='white'))
    # ax.set_title('bins', bbox={'facecolor': '0.8', 'pad': 5})
    plt.grid(True)
    plt.show()

def ma(d):
    list1=['re']
    for line in d:
        if line[6]==' Never-married':
            #print('N')
            list1.append('0')
        if line[6]==' Divorced':
            #print('D')
            list1.append('0')
        if line[6]==' Widowed':
            #print('w')
            list1.append('0')
        if line[6]==' Married-spouse-absent':
            #print('ms')
            list1.append('1')
        if line[6]==' Separated':
            #print('s')
            list1.append('1')
        if line[6]==' Married-civ-spouse':
            #print('mc')
            list1.append('1')
    return list1



if __name__ == "__main__":
    all_age=[]
    path = 'C:/Users/60126/PycharmProjects/untitled/venv/test.csv'  # 默认目录
    # Python自带库
    f = open(path, 'r')
    d = csv.reader(f)
    # 逐行读入
    min_age=200
    max_age=0
    count_number_age=[0,0,0,0,0,0,0,0]
    for line in d:
        if line[1].isdigit() ==False:
            continue
        all_age.append(eval(line[1]))
        if eval(line[1])>=max_age:
            max_age=eval(line[1])
        if eval(line[1])<=min_age:
            min_age=eval(line[1])
        if eval(line[1])>10 and eval(line[1])<=20:
            count_number_age[0]=count_number_age[0]+1
            continue
        if eval(line[1])>20 and eval(line[1])<=30:
            count_number_age[1]=count_number_age[1]+1
            continue
        if eval(line[1])>30 and eval(line[1])<=40:
            count_number_age[2]=count_number_age[2]+1
            continue
        if eval(line[1]) > 40 and eval(line[1]) <= 50:
            count_number_age[3] = count_number_age[3] + 1
            continue
        if eval(line[1])>50 and eval(line[1])<=60:
            count_number_age[4]=count_number_age[4]+1
            continue
        if eval(line[1])>60 and eval(line[1])<=70:
            count_number_age[5]=count_number_age[5]+1
            continue
        if eval(line[1]) > 70 and eval(line[1]) <= 80:
            count_number_age[6] = count_number_age[6] + 1
            continue
        if eval(line[1])>80 and eval(line[1])<=90:
            count_number_age[7]=count_number_age[7]+1
            continue
    sum_age=sum(all_age)
    labels_age=['10~20','20~30','30~40','40~50','50~60','60~70','70~80','80~90']
    equi_width_excel(count_number_age,labels_age)
    equi_width_plot(labels_age,count_number_age)
    equi_depth_plot(sum_age,all_age)
    print(count_number_age)
    print(max_age)
    print(min_age)
    f.close()
    f=open(path,'r')
    d = csv.reader(f)
    discretise(d)
    f.close()
    f=open(path,'r')
    d = csv.reader(f)
    list2=ma(d)
    f.close()
    print(len(list2))
    Binarisation_excel(list2)