from copy import deepcopy
class computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
class CPU():
    pass
class DISK:
    pass
cpu1=CPU()
disk1=DISK()
com=computer(cpu1,disk1)
com1=com
print(com)
print(com1)#manual copy the ip is same
print(com,com.disk,com.cpu)#subobject in the class (to see the ip)
print(com,com1.disk,com1.cpu)
import copy
com2= copy.copy  #类对象的浅拷贝
print(com,com1.disk,com1.cpu)
print(com,com2.disk1,com2.cpu1)
com3=deepcopy(com)
print(com)
print(com3)


def deepcopy():
    return