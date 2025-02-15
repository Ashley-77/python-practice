import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('自主课堂统计--土科.xlsx')
print(df)
plt.rcParams['font.sans-serif']=['SimHei']
#set the size of canvas
plt.figure(figsize=(10,7))
labels=df['姓名']
y=df['序号']
print(labels)
print(y)
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('1002')
plt.show()
