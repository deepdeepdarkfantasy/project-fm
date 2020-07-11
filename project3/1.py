import numpy
import csv

class earn():
    def __init__(self):
        self.ID=[]
        self.month=[]
        self.count=[]
        self.salary=[]
        self.j1=0
        self.j2=0
        #用于判断读取的文件是否已经有数据了

    def read_csv(self):
        self.j1=0
        with open('1.csv',encoding='utf-8') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if len(row) != 0:
                    self.j1=1
                    self.ID.append(row[0])
                    self.month.append(row[1])
                    self.salary.append(row[2])

    def save_as_csv(self):
        #print(self.ID,self.month)
        with open('1.csv','w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            for i in range(len(self.ID)):
                writer.writerow([self.ID[i], self.month[i], self.salary[i]])

    def inputs(self):
        if self.j1==0:
            self.ID.append('ID')
            self.month.append('month')
            self.salary.append('salary')
        print('请输入用户ID，输入完成后按回车键。')
        try:
            a=input()
        except Exception as e:
            print("输入异常，请输入纯数字")
        else:
            self.j2=0
            if eval(a)>=100 and eval(a)<= 999:
                print('请输入月份，输入完成后按回车键。')
                b = input()
                #if self.ID[1]=='111':
                    #print(eval(self.ID[1]))
                    #print(eval(self.ID[0]))
                    #print('yes')
                #print(eval(self.ID[1]))
                for i in range(1,len(self.ID)):
                    if a == (self.ID[i]):
                        self.count.append(i)
                for i in range(len(self.count)):
                    #print(type(self.month[i]))
                    if b == self.month[self.count[i]]:
                        self.j2=1
                        print('该收入信息已经录入，请不要重复输入。')
                        break
                if self.j2 == 0:
                    print('请输入该月份的薪水')
                    c=eval(input())
                    self.ID.append(a)
                    self.month.append(b)
                    self.salary.append(c)
                #print(self.ID,self.month,3333)
            self.count=[]

if __name__=='__main__':
    ea=earn()
    ea.read_csv()
    ea.inputs()
    ea.save_as_csv()
