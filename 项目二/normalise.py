import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def normalize_excel(age_list):
    print(age_list)
    age_list=age_list[::-1]
    print(age_list)
    age_list.append('normalize')
    age_list=age_list[::-1]
    with open('test.csv','r') as csvfile:
        rows=csv.reader(csvfile)
        with open('test2.csv','w',newline='') as f:
         writer=csv.writer(f)
         i=0
         print(age_list)
         for row in rows:
            if i == len(age_list):
                break
            row.append(age_list[i])
            print(row)
            writer.writerow(row)
            i=i+1


def normalise(min_age,max_age,age_list):
    for i in range(len(age_list)):
        age_list[i]=(age_list[i]-min_age)/(max_age-min_age)
    print(age_list)
    normalize_excel(age_list)
    return age_list

if __name__ == "__main__":
    all_age=[]
    path = 'C:/Users/60126/PycharmProjects/untitled/venv/test.csv'  # 默认目录
    # Python自带库
    f = open(path, 'r')
    d = csv.reader(f)
    min_age=200
    max_age=0
    age_list=[]
    for line in d:
        if line[1].isdigit() ==False:
            continue
        age_list.append(eval(line[1]))
        if eval(line[1])>=max_age:
            max_age=eval(line[1])
        if eval(line[1])<=min_age:
            min_age=eval(line[1])
    print()
    print()
    print()
    normalise(min_age,max_age,age_list)
    print()
    print()
    f.close()