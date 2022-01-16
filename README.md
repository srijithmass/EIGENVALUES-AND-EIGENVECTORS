# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step1 : 
Import numpy library using import statement. 
### Step 2: 
Using np.array(), create an array for the given matrix.
### Step 3: 
Using the np.linalg.eig(), we get two results (first is eigenvalue and second is eigenvector) of the given matrix.
### Step 4: 
Print both the resultant values using .format() and end the program.

## Program:
~~~
#Program to find the eigen values and eigen vectors.
#Developed by: SRIJITH R
#RegisterNumber: 21004191
import numpy as np
A = np.array([[2,-3,0],[2,-5,0],[0,0,3]])
values,vectors=np.linalg.eig(A)
print("Eigen values are {} and Eigen Vectors are {}".format(values,vectors))
~~~

## Output:

![GitHub Logo](output.png)

## Result:
Thus the Eigenvalue and Eigenvector is successfully solved using python program
