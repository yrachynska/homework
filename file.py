import matplotlib.pyplot as plt
import numpy as np

def rivn1(a,b,c,x):
    return a*x**2+b*x+c

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

p = []

x = np.arange(-100,100)
y1 = rivn1(a,b,c,x)
y2 = np.log2(x)

plt.plot(x,y1,x,y2)
plt.show()
print(p)