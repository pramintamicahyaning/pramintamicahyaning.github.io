import numpy as np

#Parameter untuk Euler
y0 = -4
x0 = float(input("masukkan nilai x0 :"))
n = 4
h = 0.01
y = 0
hasil = y0

#Metode Euler
for i in range(1,n):
    hasil = y0 + h*(1 + (x0) ** 2)
    x0 += h
    y0 = hasil
    print("Langkah"+str(i)+": y"+str(i)+"= "+ str(hasil))
