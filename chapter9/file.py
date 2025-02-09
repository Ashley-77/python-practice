def my_write():#create
    file=open('1.11.txt','w',encoding='utf-8')
    #write
    file.write('hihi,halo')
    file.close()
def my_read():
    file=open('1.11.txt', 'r', encoding='utf-8')
    #operate
    a=file.read()
    print(a,type(a))
    file.close()
if __name__ == '__main__':
    my_write()
    my_read()

s=open('2025.docx','r',encoding='GBK',errors='ignore')
x=s.read(1)
print(x)
s.close()
#base skills
#"w",cover 'r'  only for read 'a'=add,if you want to ues multiple you can ues the'+' mark
def files(file_name):
    file=open(file_name,'w+',encoding="GBK")#w  vs  w+(write and read)
    file.write("halo my "'\n'
               "lover" )
    file.seek(0)#move the pointer to the front of the sentence,往后读几个
    r=file.readline(2)#read and extract
    d=file.readline()#all but list format
    print(d,type(d))
    print(r,type(r))
    file.close()
if __name__ == '__main__':
    files('hi.txt')

def copy(f1,f2):#copy means write and read simultaneously
    file1=open(f1,'rb')
    file2=open(f2,'wb')
    b=file1.read()
    file2.write(b)
    file1.close()
    file2.close()
if __name__ == '__main__':
    copy('./CHina.jpg','../chapter9/copy_China.jpg')