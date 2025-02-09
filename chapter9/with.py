def write():
    with open("11.txt",'w',encoding='gbk')as file:#without closing it
        file.write('welcome to my home')
def read():
    with open('11.txt','r',encoding="gbk")as file:
        print(file.read())
def read_write(a,b):
    with open(a,'r',encoding='gbk')as file:
        with open(b,'w',encoding='gbk')as file2:#different function can use the same variable of the same name
            s = file.read()#a and b is a str but file is a text
            file2.write(s)
            print(type(a))
if __name__ == '__main__':
    write()
    read()
    read_write('./11.txt','./22.txt')









