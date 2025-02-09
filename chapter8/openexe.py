import jieba
text = "我爱自然语言处理"
words = jieba.lcut(text)
print(words)
import openpyxl
#python and excel
list1=[[1,2],
       [4,53],
       [3,45]]
workbook=openpyxl.Workbook()
sheet=workbook.create_sheet('颐和园')
for item in list1:
    sheet.append(item)
workbook.save('spots.xlsx')


