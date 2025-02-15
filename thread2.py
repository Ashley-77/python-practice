#imfm can not be shared in process but threading? shared!
import threading
import time
from threading import Thread
a=100
def add():
    global a
    a+=10
    print(a)
    print('+++over')
#print(a)main may stop earlier than sub
def subtract():
    global a
    a-=20
    print(a)
#print(a)
if __name__ == '__main__':
    print('main')
    thread1=Thread(target=add())
    thread2=Thread(target=subtract())
    thread1.start()
    time.sleep(1)
    thread2.start()
    thread2.join()
    thread1.join()
    print('main is over')

#global variable is shared by all the threading ,and we cannot decide the sequence of
# the execution of these threading
print('$'*23)
#security
ticket=20
def sell():
    global ticket
    for i in range(5):
        if ticket>=1:
            print(f'{threading.current_thread().name}is selling the{i}ticket')
            ticket-=1
        time.sleep(1)
if __name__ == '__main__':
    for i in range(3):
        t=Thread(target=sell)#
        t.start()
#sharing data will cause parallel problems because multiple threading can running
#at the same time. so we can lock them.
