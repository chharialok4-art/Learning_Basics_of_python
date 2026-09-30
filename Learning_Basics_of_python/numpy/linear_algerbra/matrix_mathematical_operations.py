import numpy as np;
arr001=np.array([1,2,3])
arr002=np.array([1,2,3])
print(arr001+arr002)
print("-------------------------------Addition------------------------------------------");
arr_2D_001=np.arange(0,9,1).reshape(3,3);
arr_2D_002=np.arange(0,9,1).reshape(3,3);
print(arr_2D_001+arr_2D_002);
print("-------------------------------Substraction------------------------------------------");
print(arr_2D_001-arr_2D_002);
print("-------------------------------Multiplication------------------------------------------");
print(arr_2D_001*arr_2D_002);
print("-------------------------------Division------------------------------------------");
print(arr_2D_001/arr_2D_002);