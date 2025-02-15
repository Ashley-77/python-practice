#first in first out
#never name your file with the name of a module
#####
from multiprocessing import Queue

if __name__ == '__main__':
    q=Queue(3)
    print('if the queue is empty:',q.empty())
    print('if the queue is full:', q.full())
    #add
    q.put('hihi')
    q.put('halo')
    print('if the queue is empty:', q.empty())
    print('if the queue is full:', q.full())
    q.put('bon')
    print('if the queue is empty:', q.empty())
    print('if the queue is full:', q.full())
    print('how many:',q.qsize())
    #get out of the queue
    print(q.get())
    print('how many:',q.qsize())
    #in
    q.put_nowait('1')
    #q.put_nowait('2')#if the queue is full ,then error
    q.put('3')#if the queue is full it will wait until there is a vacancy
    #enumerate
    if not q.empty():
        for i in range(0,q.qsize()):
            print(q.get_nowait())
            print('if the queue is empty:', q.empty())
            print('if the queue is full:', q.full())
            print('how many:', q.qsize())

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44
from  multiprocessing import Queue


if __name__ == '__main__':
    q =Queue(3)
    print('if the queue is empty:', q.empty())
    print('if the queue is full:', q.full())
    # add
    q.put('hihi')
    q.put('halo')
    print('if the queue is empty:', q.empty())
    print('if the queue is full:', q.full())
    q.put('bon')
    print('if the queue is empty:', q.empty())
    print('if the queue is full:', q.full())
