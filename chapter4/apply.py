d1={"a":"22"}
d2={'b':'43'}
merge_dict=d1|d2
print(merge_dict)
a=[00,99,94,88,95]
for index,item in enumerate(a):
    if str(item)!='0':
        a[index]='19'+str(item)
    else:
        a[index]='20'+str(item)
for item in a:
    item=eval(item)
print(a)
