import csv

a={"肖战dsadsadsadasdsadasda":["1","2","3"],"王一博":["1","","3"]}
print(list(a.keys()))
with open("sss.csv",'w',newline='') as csvfile:
    writer =csv.writer(csvfile)
    writer.writerow(['a','b','c'])
    for i in range(len(a)):
        cv2=[list(a.keys())[i]]
        for i in (list(a.values())[i]):
            cv2.append(i)
        print(cv2)
        writer.writerow(cv2)
