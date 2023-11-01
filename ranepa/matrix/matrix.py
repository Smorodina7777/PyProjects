import numpy as np

file = open("matrix.txt", "w")
list1 = []
n = int(input())
for i in range(n):
    list2 = []
    for j in range(n):
        if j>i:
            list2.append(j+1)
        else:
            list2.append(0)
    list1.append(list2)
matrix1 =np.array(list1)
matrix2 = matrix1.transpose()
matrix3 = str(matrix2+matrix1)

file.write(matrix3)
file.close()
