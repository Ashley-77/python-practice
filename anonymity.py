#simple function can be written in a line
s=lambda x,y:x+y
print(s(4,8))
c=s(3,9)
print(c,'---'*66)
list1=[2,3,4,52,21]
s=lambda x:x*2
j=[s(i) for i in list1]#or without s
print((lambda x:x*3)(i) for i in list1 )#no print out
print(j,'-'*50)
string_list = ["apple", "banAna", "cherry"]
upper_case_list = list(map(lambda s: s.lower(), string_list))#map means to all
print(upper_case_list)
def get_multiplier(n):
    return lambda x: x * n
multiplier_3 = get_multiplier(3)
result = multiplier_3(4)
print(result)