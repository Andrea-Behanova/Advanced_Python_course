import numpy as np
from scipy import linalg


#1a
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)

#1b
b = np.array([1,2,3])
print(b)

#1c
x = linalg.solve(A, b)
print(x)

#1d
print(np.dot(A, x))

#1e
B = np.array([[1,2,3],[1,2,3],[1,2,3]])
x = linalg.solve(A, B)
print(np.dot(A, x))

#1f
[eval, evec] = linalg.eig(A)
print('Eigenvalues: '+str(eval))
print('Eigenvector: '+str(evec))

#1g
print('Matrix: '+ str(A))
I = linalg.inv(A)
print('Inverse matrix: ' + str(I))
D = linalg.det(A)
print('Deeterminent: '+ str(D))

#1h
N = linalg.norm(A)
print('Norm: '+ str(N))



