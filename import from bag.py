import bag.admin as a
a.function()#including import
print('$'*34)
from bag import admin as b
b.function()#without init
print('$'*34)
from bag.admin import function as c
c()#calling directly without print
from bag.admin import *
function()