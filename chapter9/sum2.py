import time
import os
from os import replace

from fontTools.misc.bezierTools import splitLine

a=input('your name:')
b=input('key:')
def change_time(longtime):
    s=time.strftime('%Y-%m_%d %H-%M-%S',time.localtime(longtime))
    return s
if a=='kiki' and b=='1110':
    print('succeed')
    print()
    c=input('choose the next step,0 means exit,1 means check:')
    if c=='0':
        print('exit')
    elif c=='1':
        print('checking your diary')
        with open('file0.txt','w+',encoding='gbk')as file:
            print(file.read())
            d=input("what do you want to add:")
            file.seek(0)
            file.write(d)
            with open('file0.txt', 'r', encoding='gbk') as file:
                print(file.read())
                info = os.stat('file0.txt')
                print("the last time to visit:", change_time(info.st_atime))
                print("the last time to amend:", change_time(info.st_mtime))
                print()
            input('bye')

else:
    print("fail")

def find(question):
    with open('file2.csv','r',encoding='gbk') as file1:
        while True:
            line=file1.readline()
            if line==(''):
                break
            else:
                keyword=line.split(';')[0]
                reply=line.split(';')[1]
                if keyword in question:#if exist string can
                    return reply
    return False
if __name__ == '__main__':
    a=input('what do you want to ask')
    find(a)
    print(find(a))





