import os

path='setxt'
files=os.listdir(path)
print(files)
for file in files:
    txt=[]
    txt1=[]
    j=0
    pst=path+'\\'+file
    with open(pst,'r',encoding='UTF-16 LE') as txtfile:
        for line in txtfile.readlines():
            txt.append(line)
    if file=='1CO.1.CSBS.txt':
        txt1.append(file+'\n')
        for i in txt:
            if i == '   Your browser doesn\'t support audio.\n':
                j=1
                continue
            if j ==1:
                txt1.append(i)
            if i == '   2018 by Global Bible Initiative\n' and j==1:
                j=0

    if file == 'GEN.29.CSBS.txt':
        txt1.append(file+'\n')
        for i in range(len(txt)) :
            if i <=85:
                continue
            elif txt[i] == '   2018 by Global Bible Initiative\n':
                txt1.append('   2018 by Global Bible Initiative\n')
                break
            txt1.append(txt[i])

    with open(pst,'w',encoding='UTF-16') as txtfile:
        writer=txtfile.writelines(txt1)