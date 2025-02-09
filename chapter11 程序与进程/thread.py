#being included in progress, the smallest unit
#using def to create a thread  并发执行parallel
import threading
from threading import Thread
import time
def test():
    for i in range(3):
        time.sleep(1)
        print(f'threading:{threading.current_thread().name}is executing{i}')
if __name__ == '__main__':
    start=time.time()
    print(time.time())
    print(time.thread_time())
    print('\nthe main progress is executing\n')
    #thread
    list1=[Thread(target=test) for i in range(2)]
    for item in list1:
        item.start()#starting
    for item in list1:
        item.join()
    print(f'we totally spend{time.time()-start}')
#线程和进程的区别
# 资源分配：进程拥有独立的资源，包括内存空间、文件描述符等；而线程共享所属进程的资源，只拥有自己的栈空间等少量资源。
#调度：进程是系统进行资源分配和调度的基本单位，而线程是程序执行的最小单位，是操作系统进行调度的基本单位。线程的调度开销比进程小，因为线程切换不需要切换地址空间等大量资源。
#并发性：进程之间的并发性是通过操作系统的调度实现的，而线程之间的并发性除了可以通过操作系统调度实现外，还可以在同一个进程内通过线程的并发执行来实现更高程度的并发性。
#通信：进程间通信需要通过专门的通信机制，如管道、消息队列、共享内存等；而线程间通信可以直接通过共享进程的资源来实现，通信方式更加简单和高效。
#应用场景
#进程：适用于需要完全隔离和独立运行的任务，如不同的应用程序之间。
#线程：适用于在一个应用程序内部，需要同时执行多个相关任务的场景，如在一个网络服务器程序中，可以使用多个线程来处理不同的客户端连接请求。

print('$'*66)
#inherit
class subthread(Thread):
    def run (self):
        for i in range(3):
            time.sleep(1)
            print(f'{threading.current_thread().name}is running{i}')
if __name__ == '__main__':
    print('main threading is running rightnow')
    list2=[subthread() for i in range(2)]# create 2 at once
    for item in list2:
        item.start()
    for item in list2:
        item.join()
    print('over')



