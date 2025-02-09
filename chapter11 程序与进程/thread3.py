import threading
import time
from threading import Thread,Lock
ticket=100

# 创建锁对象
lock_1 = Lock()

def sold():
    global ticket
    while True:
        # 使用 with 语句管理锁，确保锁一定会被释放
        with lock_1:
            if ticket >= 1:
                # 获取当前线程的名称
                current_thread_name = threading.current_thread().name
                print(f'{current_thread_name} is selling the {101 - ticket} ticket')
                ticket -= 1
                time.sleep(0.1)  # 适当减少睡眠时间，方便观察结果
            else:
                break

if __name__ == '__main__':
    # 创建 3 个线程
    threads = []
    for i in range(3):
        t = Thread(target=sold)
        threads.append(t)
        t.start()

    # 等待所有线程执行完毕
    for t in threads:
        t.join()

    print("All tickets are sold out.")
#   #def sold():
#     global ticket
#     for i in range(50):
#         lock_1.acquire()#lock
#         if ticket>=1:
#             print(f'\n{threading.current_thread().name}is selling the{i}ticket\n')
#             ticket-=1
#         time.sleep(1)
#         lock_1.release()
# #if __name__ == '__main__':
#     for i in range(3):
#         t=Thread(target=sold)#
#         t.start()