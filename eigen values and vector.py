#Program to find the eigen values and eigen vectors.
#Developed by: SRIJITH R
#RegisterNumber: 21004191
import numpy as np
A = np.array([[2,-3,0],[2,-5,0],[0,0,3]])
values,vectors=np.linalg.eig(A)
print("Eigen values are {} and Eigen Vectors are {}".format(values,vectors))