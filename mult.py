from 初学.chapter9.file import my_write

b=input('what you want')
def file_write(s):
    file=open('file.txt','a',encoding='GBK',errors='ignore')
    file.write(s)
    file.write('\n')
    file.close()
def list_file(a,c):
    f=open(a,'a',encoding='GBK')
    f.writelines(c)#add list in to your txt, but the list should be comprised of string
    f.close()

if __name__ == '__main__':
    file_write(b)
    file_write(input('what you want'))
    list1=['1','3','2']
    list_file('file1.txt',list1)

