#data storage write and read
def my_write():
    with open('file2.csv','w',encoding="GBK")as file:
        list5=['11','22','33']
        file.write(';'.join(list5))#turn list into string
def my_read():
    with open('file2.csv','r',encoding='GBK')as file:
        s=(file.read()).split(';')
        print(s)
def write():
    with open('table.csv','w',encoding="gbk")as file:
        list6=[['11','22','33'],
               ['22','23','25']]
        for item in list6:
            file.write(';'.join(item))
            file.write('\n')
def read():
    with open('table.csv','r',encoding='gbk')as file:
        list7=[]#the same format to read it out
        lst=file.readline()
        print(lst,type(lst))
        for i in lst:
            a=i[:len(i)-1].split(';')
            list7.append(a)
        print(list7)


if __name__ == '__main__':
    my_write()
    my_read()
    write()
    read()
#high dimension data
import json
list1=[{'name':'kiki','age':8},
       {'name':'cici','age':10},
       {'name':'vivi','age':18}]#storage and apply mean type conversion
s=json.dumps(list1,ensure_ascii=False,indent=4)#2for displaying Chinese character;indent for indentation
print(s,type(s))
#decipher
list2=json.loads(s)
print(list2,type(list2))
#coding in a file
with open('333.txt','w',)as file:
    json.dumps(list1, ensure_ascii=False, indent=4)  # 2for displaying Chinese character;indent for indentation

#decoding in a program
with open('333.txt','r',encoding='gbk') as file:
    list3=json.loads(file)
    print(list3,type(list3))

#after decoding your date you do not need to change the type
