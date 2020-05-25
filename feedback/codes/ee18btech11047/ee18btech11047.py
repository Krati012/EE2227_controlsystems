#Code by Tejaswini
#Date 25 May,2020

import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if
 
t = np.linspace(0,0.005,20000)
y = 3*((3*(np.sin(20000*t))) + 1)
plt.plot(t,y) 
plt.grid()
plt.xlabel("time(t)")
plt.title("oscillating system response")
plt.ylim(-9,15)
plt.plot([0,0.005],[3,3],'r--',lw=1)
plt.plot(0.000471071,3,'o')
plt.plot(0.000785391,3,'o')

#if using termux
plt.savefig('./figs/ee18btech11047/ee18btech11047.pdf')
plt.savefig('./figs/ee18btech11047/ee18btech11047.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047.pdf"))
#else
#plt.show()
