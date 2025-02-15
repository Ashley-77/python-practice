good=[]
for i in range(5):#five times
    item=input("input what you have and its index")
    good.append(item)
print('you have choose:',good)
cart=[]
while True:
    flag=False
    for item in good:
        a=(input("the index"))
        if a==item[0:4]:#exclude 4
            cart.append(item)
            print('right received')
            flag=True
            break
        if a!=item[0:4]:
            print("we don't have this")
            flag=False
    if a=="q":
        print('received')
        break
print('you have already chosen:')
cart.reverse()
for item in cart:
    print(item)



