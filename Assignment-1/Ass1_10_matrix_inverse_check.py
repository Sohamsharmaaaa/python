# Accept two matrices and check whether second is inverse of first matrix
import numpy as np

d = int(input("enter the dimention of the matrix: "))
print("enter first matrix", d * d, "value seprated by one space: ")
input_str = input()
arr = np.fromstring(input_str, dtype=float, sep=" ")
if len(arr) != (d * d):
    print("wrong no. of values for first matrix")
else:
    print("enter second matrix", d * d, "value seprated by one space:")
    input_str1 = input()
    arr1 = np.fromstring(input_str1, dtype=float, sep=" ")
    if len(arr1) != (d * d):
        print("wrong no. of values in second matrix")
    else:
        mat1 = arr.reshape((d, d))
        mat2 = arr1.reshape((d, d))
        print(mat1)
        print(mat2)
        iden = np.identity(d)
        if np.allclose(mat1 @ mat2, iden):
            print("second matrix is inverse of first")
        else:
            print("second matrix is not inverse of first")

"""
enter the dimention of the matrix: 2
enter first matrix 4 value seprated by one space:
4 2 1 3
enter second matrix 4 value seprated by one space:
0.3 -0.2 -0.1 0.4
[[4. 2.]
 [1. 3.]]
[[ 0.3 -0.2]
 [-0.1  0.4]]
second matrix is inverse of first
"""
