from multiprocessing import Process
#don't share

a=88
def add():
    print('sub1 is executing!')
    global a#a has a value
    a+=8
    print('a=',a)
    print('sub1 is over')
def subtract():
    print('sub2 is executing!')
    global a  # a has a value
    a -= 8
    print('a=', a)
    print('sub2 is over')
if __name__ == '__main__':
    print('superb is executing')
    print('a=',a)
    p1=Process(target=add)#a sub_program refer to a function or a program\project
    p2=Process(target=subtract())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("superb is over")
    print('a=',a)



#global:
x = 10  # 定义一个全局变量 x

def modify_global():
    global x  # 声明 x 为全局变量
    x = 20  # 修改全局变量 x 的值

    print(x)  # 输出 10
    modify_global()
    print(x)  # 输出 2
