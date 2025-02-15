#pool of process
#without join
from multiprocessing import Process,Pool#multiple
import time,os
def task(name):
    print(f'id of sub is:{os.getpid()},superprocess is{os.getppid()}')
    time.sleep(2)
if __name__ == '__main__':
     start=time.time()# main progress
     print('super is executing')
     #create pool
     p=Pool(3)
     #create task
     for i in range(1,8):
         #without join block
        p.apply_async(func=task,args=(i,))
     p.close()
     p.join()
     print('all of the subprogress are over,and we used:',time.time()-start)
#VS block


def task(name):
    print(f'id of sub is:{os.getpid()},superprocess is{os.getppid()}')
    time.sleep(2)
if __name__ == '__main__':
     start=time.time()# main progress
     print('super is executing')
     #create pool
     p=Pool(3)
     #create task
     for i in range(1,8):
         #without join block
        p.apply(func=task,args=(i,))###
     p.close()
     p.join()
     print('all of the subprogress are over,and we used:',time.time()-start)