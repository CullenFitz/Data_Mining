#Question 3:

import numpy as np


#Factorize Sigma into its eigenvalues and eigenvectors
sig = np.array([[1,1,1],
                [1,3,3],
                [1,3,6]])

w, v = np.linalg.eig(sig)

print(w)    #These are the eigenvalues
print(v)    #The columns in this are eigenvectors corresponding to the eigenvalues





