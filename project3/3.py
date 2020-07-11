import csv

class IMST():
    def __init__(self):
        self.ID=[]
        self.month=[]
        self.salary=[]
        self.tax=[]
        self.j1=0
        self.j2=0
        self.input_ID=0
        self.input_month=0

    def csv_reader(self):
        with open('1.csv',encoding='utf-8') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                self.ID.append(row[0])
                self.month.append(row[1])
                self.salary.append(row[2])
                if len(row)==3:
                    self.tax.append('')
                else:
                    self.tax.append(row[3])

    def inputs(self):
        print('请输入您要查询的ID。')
        self.input_ID = input()
        print('请输入您要查询的月份。')
        self.input_month = input()
        self.func_fi(self.input_ID,self.input_month)

    def func_fi(self,ID,month):
        for i in range(len(self.ID)):
            if ID == self.ID[i]:
                self.j1=1
                if month == self.month[i]:
                    self.j2=1
                    if self.tax[i] == '':
                        print('缺失缴税记录。')
                    else:
                        print('应该缴税：',self.tax[i])
                else:
                    continue
            else:
                continue
        if self.j1==0:
            print('没有该用户。')
        if self.j1==1 and self.j2==0:
            print("此用户没有该月份信息。")

if __name__=='__main__':
    im=IMST()
    im.csv_reader()
    im.inputs()


                


