import matplotlib.pyplot as plt
import numpy as np

def rivn1(a,b,c,x):
    return a*x**2+b*x+c

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

p = []

x1 = np.arange(-100,100)
x2 = np.arange(0.1,100)
y1 = rivn1(a,b,c,x1)
y2 = np.log2(x2)

for i in range(0,100):
    if y1[i] == y2[i]:
        p.append(i)

plt.plot(x1,y1,x2,y2)
print(p)
plt.show()
