#element
#communication between progress
import time
from multiprocessing import Queue,Process
if __name__ == '__main__':
    q=Queue(3)
    q.put('hi')
    print('how many:',q.qsize())
    q.put('halo')
    q.put('bon')
    #q.put('hihi',block=True,timeout=2)#if it is still full after 2s, then error

a=100
def write(q):
    global a
    if not q.full():
        for i in range(8):
            a-=10
            q.put(a)
            print(f'we put{a} in the queue')
def read(q):
    time.sleep(1)
    if not q.empty():
        print(f'a is {q.get()} when it is out')
if __name__ == '__main__':
    print('super_progress is executing')
    q=Queue()#without upper limit
    p1=Process(target=write(q),args=('q',))
    p2=Process(target=read(q),args=('q',))#send (q,) to a function
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("super is over")
