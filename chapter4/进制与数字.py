#complex
from docx.opc.oxml import pr_namespace
from lxml.html.diff import tokenize_annotated
from unicodedata import decimal

print((5+9j)+(9+4J))
a=complex(2,4)#in-built
print(a)
#truncate
import math
print(math.trunc(9/2),5/2)
#hex16\octal8\binary2
print(hex(22),oct(4),bin(99))
print(int('65'),int('65',8),int("65",16),int('10001',2),int('0o20',8),int('0b1001001',2))#put into integer 10
#eval put into number 10
print(eval('64'),eval('0o100'),eval('0x95'),eval('0b1001001'))
print(f"math.pi,math.e",)#save float
#in-built
print(pow(2,8),abs(-77))#exponent,absolute
print(math.sin(1/4*(math.pi)),math.tan(math.pi/4))
print(math.sqrt(196))#square root
print(max(8,4,2,4),min(2,4,9,0,4))
print(int(9.3883),round(3.992))#四舍五入与取整floor
#module import
import random
i=random.random
j=random.randint(1,200)
print(j)
k=random.randint(1,88)
print(math.sqrt(k),float(k,),round(k/2))
print(f'{k:.3f}')#standard format
import decimal
decimal.getcontext().prec=3
l=decimal.Decimal(2)/decimal.Decimal(9)
print(l)
print(1/3)#useless,no-effect
#fractions
from fractions import Fraction# function should be capital
x=Fraction(1,9)
y=Fraction(0.125)#from a float
print(x,y,float(x))
print(f'{float(x):.3f}')#error:fraction instead of float
x={'sssd'}#变量回收
print(map(ord,x))#ascll code\n  \t
print(x)

