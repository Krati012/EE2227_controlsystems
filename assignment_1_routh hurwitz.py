import numpy as np
import matplotlib.pyplot as plt
import math as mp
import cmath

s=0
#characteristic equation
P=(s**4)+8*(s**3)+18*(s**2)+16*s+5
co=[1,8,18,16,5,0]
R=np.zeros((5, 3))
for i in range(0,5):
	if i==0:
		for j in range(0,3):
			R[i][j]=co[2*j]
			R[i+1][j]=co[2*j+1]
	if i>=2:
		for j in range(0,2):
			R[i][j]=(((R[i-1][0])*(R[i-2][j+1]))-((R[i-1][j+1])*(R[i-2][0])))/(R[i-1][0])

a=0
for k in range(0,5):
	if R[k][0]<=0:
		a=a+1
		
		
	
print("Routh array")
print(R)
print("Number of negative elements in first column of routh array are :",a)
if a==0:
	print("System is stable")


		
