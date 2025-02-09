#how to create \build\import a module
#in-built module\third-party \user-defined module
#.py is a module can be called
# import\import variable\function from module\import

from module_1 import fun,a#Chinese characters are not allowed
from module_1 import a as A
print(A)
fun()
#wildcard mark
from module_1 import * #whatever
import math,time
print(time)
#if two module have the same variable, w use the latter one
import module_1
import module_3
from module_3 import *
module_1.fun()#you can only point out to call
module_3.fun()