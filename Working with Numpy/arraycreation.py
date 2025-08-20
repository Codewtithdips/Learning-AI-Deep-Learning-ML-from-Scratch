import numpy as np


arr1 = np.array([1,2,3])
arr2 = np.array([[1,2], [3,4]])

a =np.arange(0 , 10 , 2)

#print(a)
#print(arr2)

b = np.linspace(0, 1, 5)
#print(b)

c = np.random.rand(2, 3) 
#print(c)

d = np.random.randn(2, 3)
#print(d)


#Array Indexing and SLicing
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

#print(arr2d[1:, 1])

#print(arr2d[1, :])

#print(arr2d[0:2, 1:3])

A = np.array([[1, 2],
              [3, 4]])
invA = np.linalg.inv(A)
#rint(invA)


eigvals, eigvecs = np.linalg.eig(A)
#print("Eigenvalues:", eigvals)
#print("Eigenvectors:\n", eigvecs)


# Example 3x3 matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Determinant using NumPy
det = np.linalg.det(A)
print("Determinant:", det)
