def recursion(a):
    if a==1:
        return 1
    else:
        return a*recursion(a-1)#multiple invoke
print(recursion(10))
print('#'*30)
b=eval(input('num:'))
def fib(s):
    if s==1 or s==2:
        return 1
    else:
        return fib(s-1)+fib(s-2)
print(fib(30))
for i in range(1,b):
    print(fib(i),end='\t')
print('\n')
