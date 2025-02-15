#inherit method
from multiprocessing import Process
import os,time



class Sub_person(Process):#inherit
    def __init__(self,name):
        super().__init__()
        self.name=name

    #rewrite superclass 'run'
    def run(self):
        print(f'name of sub is:{os.getpid()},superprocess is{os.getppid()}')
if __name__ == '__main__':
    print('the superprocess is executing')
    list3=[]
    for i in range(1,8):
        p1=Sub_person(f'process{i}')
        #start
        p1.start()
        list3.append(p1)
    for item in list3:
        item.join()
    print('superprocess is over.')


