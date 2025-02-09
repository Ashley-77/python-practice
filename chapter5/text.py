from logging import exception


try:
    a = int(input('input your grade'))
    if  0<a<100:
        print('your average grade is:',a/30)
    elif 100 <= a <= 0:
        print("wrong number, check it")
    else:
        raise Exception# all type will be captured in mid of "try"
except Exception as e:
    print(e)

try:
    a=int(input('1:'))
    b=int(input('2：'))
    c=int(input('3:'))
    if a+c>b and a+b>c and b+c>a:
        print('valid')
    else:
        print('invalid')#formatting the string namely
        # change something you want to print out as a string
except Exception as e:
    print(e)

