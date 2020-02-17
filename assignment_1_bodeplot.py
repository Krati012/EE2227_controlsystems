import numpy as np
import matplotlib.pyplot as plt
import math as mp
import cmath

W=np.linspace(10**(-1),10**(4),10000)
f=np.array([])
p=np.array([])
for w in W:
	s=complex(0,w)
	H_s = 10/(s+100)
	F=20*(mp.log(abs(H_s)))
	f=np.append(f,[F])
	P=cmath.phase(H_s)
	p=np.append(p,[P])
plt.figure(1)
plt.semilogx(W,f)
plt.title("Bode plot(Magnitude response)")
plt.grid()
plt.figure(2)
plt.semilogx(W,p)
plt.title("Bode plot(Phase response)")
plt.grid()
plt.show()

	
