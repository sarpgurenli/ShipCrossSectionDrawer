__author__ = "Arafat Abdurrahman Albatuny, Muhammed İnalöz, Sarp Gürenli"
__copyright__ = "Copyright 2018, The Cross Section Drawer Project"
__version__ = "2.5"
import matplotlib.pyplot as plt # for graph
import numpy as np #for math modules
a = input("enter ship breadth:") # input from user for breadth of ship
B = float(a) # this line change input type to integer
b = np.loadtxt("s60.txt")*B/2*0.7 # this line open s60 text and import to python and multiply the s60 offset values with half of breadth 
np.savetxt(a, b, fmt="%.4f") # this line save the new text file as breadth length
WL = [0,0.3,1,2,3,4,5,6] # water line list for graph referance of y axis points
a1 = b[0,:] # x values
a2 = b[1,:]
a3 = b[2,:]
a4 = b[3,:]
a5 = b[4,:]
a6 = b[5,:]
a7 = b[6,:]
a8 = b[7,:]
a9 = b[8,:]
a10 = b[9,:] 
a11 = b[10,:]
a12 = b[11,:]
a13 = b[12,:]
plt.plot(a1,WL)# this codes draw the graph
plt.plot(a2,WL)
plt.plot(a3,WL)
plt.plot(a4,WL)
plt.plot(a5,WL)
plt.plot(a6,WL)
plt.plot(a7,WL)
plt.plot(-a8,WL)
plt.plot(-a9,WL)
plt.plot(-a10,WL)
plt.plot(-a11,WL)
plt.plot(-a12,WL)
plt.plot(-a13,WL)
plt.grid() # this line draw grids