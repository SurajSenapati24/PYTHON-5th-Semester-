import numpy as np
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
arr=np.concatenate((array1, array2), axis=0)
print(arr)