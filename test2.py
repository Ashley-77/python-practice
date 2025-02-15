a=input('input')
def fun(a):
    a.upper()
    return a
print(fun(a))
#unicode
list1=[]
def up(x):
    for item in x:
        if "a"<='item'<='z':
            list1.append(chr(ord(item)-32))
        elif'A'<='item'<="Z":
            list1.append(chr(ord(item)+32))
        else:
            list1.append(item)
    return ''.join(list1)
print(up(a))
def find(y,l):
    for item in l:
        if s==item:
            return True
    return False
list2=['halo','bonjour','hi']
s=input('words to show greeting')
print('exist'if find(s,list2) else 'not exist')#simplify
#distinguish the real and fake variant
