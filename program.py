#exe is a program, when a program starts it will cause a progress
# which will occupy your internal storage
from multiprocessing import Process
import time,os
def test():
    print(f'subprocess is:{os.getpid()},superprocess is{os.getppid()}')#progress ip
    time.sleep(1)
if __name__ == '__main__':
    print('executing')
    #create 5 subprocesses
    list1=[]
    for i in range(5):
        p=Process(target=test())
        #start
        p.start()
        list1.append(p)
    for item in list1:
        item.join()#blocking the main so that them can be done in queue
    print('main progress is over.')