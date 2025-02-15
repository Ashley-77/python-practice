from sys import excepthook

try:
    a=eval(input("dividend"))
    b=eval(input('divisor'))
except ZeroDivisionError:
    print("0")
except ValueError:
    print('wrong type')
else:
    print(a/b)
finally:
    print('finish')#always print out
#capture
try:
    p=eval(input('you school number:'))
    if type(p)!=int:
        raise Exception('you should only input number')#capture
    else:
        print("your classnumber is",p)
except Exception as e1:
    print('error result from',e1)

#types:
#ZeroDivisionError\ValueError\IndexError\
#AttributeError\KeyError\NameError\SyntaxError
#TypeError\IndentationError

#调试工具debug tell you the underlying logics
#set the red point and operate it
