from math import *
def zeros(n,m):
    Z=[]
    for i in range(n):
        Z.append([0]*m)
    return Z

def D(Func,a,h):
        return (Func(a+h)-Func(a-h))/(2*h)

def Richardson_dif(func,a):
    k=9 
    L=zeros(k,k)
    for I in range(k):
        L[I][0]=D(func,a,1/(2**(I+1)))
    for j in range(1,k):
        for i in range(k-j):
            L[i][j]=((4**(j))*L[i+1][j-1]-L[i][j-1])/(4**(j)-1)
    return L[0][k-1]
    
print('f(x) = -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2 dengan x = 0.5')
print('Hasil Diferensiasi Numerik= '+'%04.20f'%Richardson_dif(lambda x: -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2 ,0.5))
print('diff(2**cos(pi+sin(x)) dengan x = pi/2 adalah = %04.20f'%Richardson_dif(lambda x: 2**cos(pi+sin(x)),pi/3))
