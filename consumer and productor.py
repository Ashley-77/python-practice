#two types of threading
import time
from queue import Queue
from threading import Thread
class producer(Thread):#inherit from Thread
    def __init__(self,name,queue):
        Thread.__init__(self,name=name)
        self.queue=queue
    def run(self):##当一个类继承自 Thread 类后， 通常需要重写 run 方法。run 方法定义了线程启动后要执行的
    # 具体代码逻辑。当调用线程对象的 start 方法时，Python 解释器会自动调用
# 该线程对象的 run 方法。
        for i in range(5):
            print(f'{self.name} d {i}will be put into queue')
            self.queue.put(i)
            time.sleep(1)

class consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(5):
            value=self.queue.get()
            print(f'the threading of consumer{self.name} get{value}')
            time.sleep(1)
        print('the consumer is over')
if __name__ == '__main__':
    queue=Queue()
    P=producer(name='pro',queue=queue)
    c=consumer(name='con',queue=queue)
    P.start()
    P.join()
    c.start()
    c.join()
    print('over')