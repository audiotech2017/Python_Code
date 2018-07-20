import matplotlib.pyplot as plt
import numpy as np


def function1(x):
    return 2*x+10
def function2(x):
    return x**2 + 1
def function3(x):
    return np.cos(x/9)*25
def function4(x):
    return x**2 - 6

x=np.arange(-1000,1000,1)
y1=function1(x)
y2=function2(x)
y3=function3(x)
y4=function4(x)
y5=x*0+1

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)

plt.xlim(-100,100)
plt.ylim(-30,100)
plt.show()
