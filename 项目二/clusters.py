import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import MultipleLocator
import pandas as pd

def f1(occupation,a):
    tr_occupation=[]
    for i in occupation:
        if i == a[0]:
            tr_occupation.append(1)
            continue
        if i == a[1]:
            tr_occupation.append(2)
            continue
        if i == a[2]:
            tr_occupation.append(3)
            continue
        if i == a[3]:
            tr_occupation.append(4)
            continue
        if i == a[4]:
            tr_occupation.append(5)
            continue
        if i == a[5]:
            tr_occupation.append(6)
            continue
        if i == a[6]:
            tr_occupation.append(7)
            continue
        if i == a[7]:
            tr_occupation.append(8)
            continue
        if i == a[8]:
            tr_occupation.append(9)
            continue
        if i == a[9]:
            tr_occupation.append(10)
            continue
        if i == a[10]:
            tr_occupation.append(11)
            continue
        if i == a[11]:
            tr_occupation.append(12)
            continue
        if i == a[12]:
            tr_occupation.append(13)
            continue
        if i == a[13]:
            tr_occupation.append(14)
            continue
        if i == a[14]:
            tr_occupation.append(15)
            continue
    return tr_occupation

def f2(native_contry,b):
    tr_native_contry=[]
    for i1 in range(len(native_contry)):
        a1=0
        for i2 in range(len(b)):
            a1=a1+1
            if native_contry[i1]==b[i2]:
                tr_native_contry.append(a1)
    return  tr_native_contry


if __name__ == "__main__":
    all_age=[]
    path = 'C:/Users/60126/PycharmProjects/untitled/venv/test.csv'
    f = open(path, 'r')
    d = csv.reader(f)
    work_our=[]
    occupation=[]
    native_contry=[]
    for line in d:
        if line[13].isdigit()==True:
           work_our.append(eval(line[13]))
           native_contry.append((line[14]))
        occupation.append(line[7])
    occupation.remove(occupation[0])
    a=list(set(occupation))
    b=list(set(native_contry))
    print(len(b))
    tr_native_contry=f2(native_contry,b)

    #Native country& occupation

    tr_occupation = f1(occupation, a)
    cm = plt.cm.get_cmap('Reds')
    sc = plt.scatter(tr_native_contry,tr_occupation , c=tr_native_contry, vmin=-10, vmax=36, s=35, cmap=cm)
    ax=plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.xticks(range(1,len(b)+1), b, rotation=90)
    plt.yticks(range(1,len(a)+1),a,rotation=0)
    plt.show()

    #Native country & work hours per week
    
    cm = plt.cm.get_cmap('Reds')
    sc = plt.scatter(tr_native_contry, work_our, c=tr_native_contry, vmin=-10, vmax=36, s=35, cmap=cm)
    ax=plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(5))
    plt.xticks(range(1,len(b)+1), b, rotation=90)
    plt.show()

    #Work hours per week & occupation
    
    tr_occupation=f1(occupation,a)
    cc=range(2660)
    cm = plt.cm.get_cmap('Reds')
    sc = plt.scatter(work_our, tr_occupation, c=work_our, vmin=-40, vmax=90, s=35, cmap=cm)
    ax=plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.yticks(range(1,len(a)+1), a, rotation=45)
    plt.show()


