#use function to create a sub_progress
import os,time
from multiprocessing import Process
def sub(name):
    print(f'sub_progress ID is{os.getpid()},super is{os.getppid()}___-----{name}')
    time.sleep(3)

def sub_two(a):
    print(f'sub_progress ID is{os.getpid()},super is{os.getppid()}___-----{a}')
    time.sleep(2)
if __name__ == '__main__':#main is superb
    print('start to execute superb')
    #create a sub
    for i in range(5):
        p1=Process(target=sub,args='p')
        p2=Process(target=sub_two,args='q')
        #launch
        p1.start()
        p2.start()
        print(p1.name,p1.pid,'is alive?',p1.is_alive())
        print(p2.name,p2.pid,'is alive?',p2.is_alive())
        p1.join()
        p2.join()
    print('all is over')







