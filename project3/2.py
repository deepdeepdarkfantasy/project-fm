import csv

class earn_tax():
    def __init__(self):
        self.tax=[]
        self.ID = []
        self.month = []
        self.salary = []
        self.i=0

    def csv_reader(self):
        with open('1.csv',encoding='utf-8') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                print(row)
                self.ID.append(row[0])
                self.month.append(row[1])
                self.salary.append(row[2])
                if (row[0]).isdigit() == False:
                    if len(row) == 3:
                        self.tax.append('tax')
                        continue
                    else:
                        self.tax.append(row[-1])
                else:
                    self.tax.append(eval(row[2])*0.12)


    def csv_writer(self):
        self.i=0
        with open('1.csv','w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            for self.i in range(len(self.ID)):
                writer.writerow([self.ID[self.i],self.month[self.i],self.salary[self.i],self.tax[self.i]])

if __name__=='__main__':
    et=earn_tax()
    et.csv_reader()
    et.csv_writer()