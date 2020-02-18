import numpy as np
import matplotlib.pyplot as plt
import math as mp
import cmath

s=0
#characteristic equation
P=(s**4)+8*(s**3)+18*(s**2)+16*s+5
co1=[1,8,18,16,5,0]
co2=[3,10,5,5,2,0]
def routh(co):
	p=int(len(co))-1 #5
	b=int((len(co))/2) #3
	R=np.zeros((p,b))
	for i in range(0,p):
		if i==0:
			for j in range(0,b):
				R[i][j]=co[2*j]
				R[i+1][j]=co[2*j+1]
		if i>=2:
			for j in range(0,b-1):
				R[i][j]=(((R[i-1][0])*(R[i-2][j+1]))-((R[i-1][j+1])*(R[i-2][0])))/(R[i-1][0])

	a=0
	for k in range(0,p):
		if R[k][0]<=0:
			a=a+1
	si=0		
	for m in range(0,p-1):
		if (R[m][0])*(R[m+1][0])<0:
			#sign=np.append(sign,[1])
			si=si+1
	print("Routh array")
	print(R)
	print("Number of negative elements in first column of routh array are :",a)
	if a==0:
		print("System is stable")
	else:
		print("Number of sign changes in first column = POLES ON RIGHT HALF PLANE ",si)
		print("System is unstable ")
	print("\n")
		
print("CHARACTERISTIC EQUATION : (s**4)+8*(s**3)+18*(s**2)+16*s+5=0 ")
routh(co1)
print("CHARACTERISTIC EQUATION : 3*(s**4)+10*(s**3)+5*(s**2)+15*s+2=0 ")
routh(co2)

		
