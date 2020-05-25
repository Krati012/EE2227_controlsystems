#Code by Tejaswini
#Date 25 May,2020

import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import s,t
from sympy.integrals import inverse_laplace_transform
from sympy import *

#if using termux
import subprocess
import shlex
#end if

G, k = symbols('G ,k', real=True)

Ts = (G*((k)**2)*(s**2) + G*(3*k)*s + G)/(((k**2)*(s**2)) + 1)	#transfer function
Us = 1/s
Ys = Ts*(Us)
y = inverse_laplace_transform(Ys,s,t) 	#inverse laplace transform
R = 250
C = (0.2)*(10**(-6))
y_t = y.subs({G: 3, k: R*C})
print("step response is :",y_t)

