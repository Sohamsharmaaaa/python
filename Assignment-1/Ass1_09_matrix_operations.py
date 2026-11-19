"""write a python script to accept two matrices and perform following opperation on it:-
1.addition
2.multiplication
3.check whether the first matrix is upper triangular
4. check whether the second matrix is lower trangular
5.check first matrix is symmetric"""

import numpy as np

d = int(input("Enter the dimension of the matrix: "))
print("Enter first matrix", d * d, "values separated by one space:")
input_str = input()
arr = np.fromstring(input_str, dtype=float, sep=" ")
if len(arr) != d * d:
    print("Wrong number of values for first matrix")
else:
    print("Enter second matrix", d * d, "values separated by one space:")
    input_str1 = input()
    arr1 = np.fromstring(input_str1, dtype=float, sep=" ")
    if len(arr1) != d * d:
        print("Wrong number of values for second matrix")
    else:
        mat1 = arr.reshape((d, d))
        mat2 = arr1.reshape((d, d))
        print("\nFirst Matrix:")
        print(mat1)
        print("\nSecond Matrix:")
        print(mat2)
        while True:
            print("\n----- MENU -----")
            print(
                "1. Addition\n2. Multiplication\n3. Check first matrix is Upper Triangular\n4. Check second matrix is Lower Triangular\n5. Check first matrix is Symmetric\n6.exit"
            )
            ch = int(input("Enter your choice: "))
            match ch:
                case 1:
                    print("\nAddition:")
                    print(mat1 + mat2)
                case 2:
                    print("\nMultiplication:")
                    print(mat1 @ mat2)
                case 3:
                    flag = True
                    for i in range(d):
                        for j in range(d):
                            if i > j:
                                if mat1[i][j] != 0:
                                    flag = False
                    if flag:
                        print("First matrix is Upper Triangular")
                    else:
                        print("First matrix is NOT Upper Triangular")
                case 4:
                    flag = True
                    for i in range(d):
                        for j in range(d):
                            if i < j:
                                if mat2[i][j] != 0:
                                    flag = False
                    if flag:
                        print("Second matrix is Lower Triangular")
                    else:
                        print("Second matrix is NOT Lower Triangular")
                case 5:
                    flag = True
                    for i in range(d):
                        for j in range(d):

                            if mat1[i][j] != mat1[j][i]:
                                flag = False
                    if flag:
                        print("First matrix is Symmetric")
                    else:
                        print("First matrix is NOT Symmetric")
                case 6:
                    print("Program ended")
                    break
                case _:
                    print("Invalid choice")
