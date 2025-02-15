import numpy as np
import matplotlib.pyplot as plt
a=plt.imread('China.jpg')
print(a,type(a))
plt.imshow(a)
b=np.array([0.239,0.812,0.821])#灰度公式
c=np.dot(a,b)
plt.imshow(c,cmap='gray')
plt.show()#you should move your pic into the same file
