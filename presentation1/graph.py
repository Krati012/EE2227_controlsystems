import numpy as np
import matplotlib.pyplot as plt
import math as mp

T=np.linspace(0,5,100)
T2=np.linspace(0,1,2)
Y1=np.array([])
for t in T:
	y1=((1/4)*(mp.exp(-2*t)))+(3/4)+((1/2)*t)
	Y1=np.append(Y1,[y1])
Y2=0*T2+1.284
plt.plot(T,Y1,'g')
plt.plot(T2,Y2,'o',linestyle="--")
plt.plot(1,1.284,'r')
plt.text(1,1.284,(1,round(1.284,5)))
plt.title("y(t)")
plt.grid()
plt.show()
