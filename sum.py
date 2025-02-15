#
#模块起名，导入方法，扩展名py
#包，第三方与内置模块、自定义模块
#升级命令/安装命令pip第三方
#no1

import prettytable as pt
import wordcloud

tb = pt.PrettyTable()  # create a sheet
def show_ticket(row_num):
    tb.field_names=['order','seat1','seat2','seat3']
    for i in range(1,row_num+1):
        lst=[f'the{i}row','available','available','available']
        tb.add_row(lst)
    print(tb)
#booking
def book(row_num,row,column):
    tb.field_names = ['order', 'seat1', 'seat2', 'seat3']
    for i in range(1, row_num + 1):
        if int(row)==i:
            lst = [f'the{i}row', 'available', 'available', 'available']
            lst[int(column)]='sell'
            tb.add_row(lst)
        else:
            lst = [f'the{i}row', 'available', 'available', 'available']
            tb.add_row(lst)
    print(tb)
if __name__ == '__main__':
    row_num=4
    show_ticket(row_num)
    choose=input('what( , )')
    row,column=choose.split(',')
    order_ticket=(row_num,row,column)
print(tb)
import datetime
a=input('the starting time:')
c=datetime.datetime.strptime(a,'%Y.%m.%d')#pay attention to the format
x=eval(input('day:'))
date=c+datetime.timedelta(days=x)
print(date)
import jieba
from wordcloud import WordCloud
with open('2025.docx','r',encoding='utf-8',)as file:
    s=file.read()
list1=jieba.lcut(s)
#excluding
stopword=['阶段']
txt=''.join(list1)
wordcloud=WordCloud(background_color='black',font_path='msyh.tcc',stopword=stopword,width=80,height=800)
wordcloud.generate(txt)
wordcloud.to_file('cloud.png')
