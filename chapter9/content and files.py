#content and files
import os
print(' current working path:',os.getcwd())
print('all the files on the current working path',os.listdir())
print('appointed files on the current working path',os.listdir('E:'))
#create and delete;if you have already created\deleted a same-name content,error
#os.mkdir('good')#only operate once
#os.makedirs('./aa/dd/c')#nest multiple use makedirs
#os.rmdir('good')
#os.removedirs('./aa/dd/c')#delete all
#change the working path
os.chdir('e:\pythonProject')#the following code will be store in this path
os.chdir('E:\pythonProject1\初学\chapter9')
#traverse the catalog
for dirs,dirlst,filelst in os.walk('E:\pythonProject1\初学'):
    print(dirs)#folder
    print(filelst)#all files as list
    print('$'*23)
    print(dirlst)#folders as list
#delete files
#os.remove('1.11.txt')
#os.rename('11.txt','11new.txt')
#converse the time format
import time
def change_time(longtime):
    s=time.strftime('%Y-%m_%d %H-%M-%S',time.localtime(longtime))
    return s
#get information
info=os.stat('data1.py')
print(info,type(info))#print out something you cannot figure out
print("the last time to visit:",change_time(info.st_atime))
print("the last time to amend:",change_time(info.st_mtime))
print("size:",change_time(info.st_size))

#start file of the same path
os.startfile('calc.exe')#or you can use wins+r
#os.startfile('E:\PyCharm Community Edition 2024.2.4\bin')
#submodule os.path
import os.path
print('the absolute path:',os.path.abspath('22.txt'))
print('the relative path:',os.path.exists('22.txt'))#if exist
print('the relative path:',os.path.exists('ss.txt'))#if exist
print('join:',os.path.join('E:/','22.txt'))
print('split file name and subfix name:',os.path.split('CHina.jpg'))
print('extract file name',os.path.basename(r'data1.py'))
print('extract file path',os.path.dirname(r'data1.py'))
print('if a valid path catalog',os.path.isdir('E:\pythonProject1\初学\chapter4'))
print('if a valid path',os.path.isdir('E:\pythonProject1\初学\chapter41'))
print('if a valid path',os.path.isdir('E:\pythonProject1\初学\chapter41'))
print('if a valid file',os.path.isfile('E:\pythonProject1\初学\chapter9\file.txt'))

