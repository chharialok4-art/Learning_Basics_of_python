import numpy as np;
arr_1D=np.array([7,7,0,4,0,0,2,0,1,7])
print(len(arr_1D));
print("---------------------------------1D Sort------------------------------------------------")
arr_001=np.array([200,800,30,10,0,2,78,45,21,89,800]);
print("1D sort:\n",np.sort(arr_001));
print("---------------------------------2D Sort axis-0------------------------------------------------")
arr_2D=np.array([[20,10,50],[10,50,20],[90,100,40]]);
print("Original array :\n",arr_2D);
print("2D sort:\n",np.sort(arr_2D,axis=0));
print("---------------------------------2D Sort axis-1------------------------------------------------")
print("Original array :\n",arr_2D);
print("2D sort:\n",np.sort(arr_2D,axis=1));

