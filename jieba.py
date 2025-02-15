#词云
import jieba


with open('我.docx','r',encoding='utf-8',errors='ignore')as file:
    s=file.read()
print(s)
a=jieba.lcut(s)
print(a)
#remove the overlapping
x=set(a)


def lcut(s):
    return None