#file.seek(k) refer to byte not character one Chinese character occupy 3 byte in utf-8
#write is different from writelist
#1 create files in bunches
import os
import random
import os.path


#os.makedirs('pile')


name=[]
def piles():
    list1=['rice','noodle','oil','fruit']
    code=[0,2,3,4,5,3,6,7,'h','u',9,'p']
    number = []

    for i in range(2000):#join,change the sequence
        if i<10:
            number+='000'+str(i)
        if i<100:
            number+='00'+str(i)
        if i<1000:
            number+='0'+str(i)
        elif i>=1000:
            number+=str(i)
        number+="_"+random.choice(list1)
        #recognition code
        s=''
        for j in range(9):
            s+=str(random.choice(code))
            number+='_'+s
        name.append(number)
    return name


def create_file(a):
    os.mkdir(str(a))


if __name__ == '__main__':
        path = './bag'  # current
        if not os.path.exists(path):
            os.mkdir(path)
        list2 =name
        for item in list2:
            create_file(os.path.join(path, item) + '.txt')
#2
if not os.path.exists('bag2'):
    os.makedirs('bag2')
p=eval(input('how many do you want:'))
for i in range(1,p+1):
    b=str(i)
    os.makedirs('./bag2/'+b)


