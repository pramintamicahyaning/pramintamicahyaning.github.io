from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 2
N = 2500

#function for integral
def func(x):
    return (4-x**2)**0.5

area = []
for i in range(N):
    xrand = np.zeros(N)

    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral = 0.0

    for i in range(N):
        integral+=func(xrand[i])

    jawab = (b-a)/float(N)*integral
    area.append(jawab)

plt.title("Nilai phi")
plt.hist(area,bins = 30, ec = 'black')
plt.xlabel("Area")
plt.show()
