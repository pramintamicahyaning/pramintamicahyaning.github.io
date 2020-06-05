from scipy import random #import library random dari scipy
import numpy as np #import library numpy

a = -1
b = 1
N=100
n=3
xrand=np.zeros(N)#dx
yrand=np.zeros(N)#dy
zrand=np.zeros(N)#dz
#fungsi np.zeros mengembalikan array baru dengan bentuk dari tipe yang diberikan, di mana nilai elemen sebagai 0.
integral=0.0
for i in range(n+1):
    for i in range(len(xrand)):
        xrand[i]=random.uniform(a,b)

    for i in range(len(yrand)):
        yrand[i]=random.uniform(a,b)

    for i in range(len(zrand)):
        zrand[i]=random.uniform(a,b)

    def func(x,y,z):
        return (x**2)+(y**2)+(z**2)


    for i in range(N):
        integral+=func(xrand[i],yrand[i],zrand[i])

jwb=(b-a)/float(N)*integral
print("Hasil : ",jwb)
