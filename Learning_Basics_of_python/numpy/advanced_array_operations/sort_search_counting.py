import numpy as np;
arr_1D=np.array([("Alok",33),("Aniket",28),("Darshi",25),("Amit",30),("Aman",34)],dtype=([("Name",'U10'),("Age",int)]));
print("---------------------------------Sorted by Order---------------------------------------------")
print("Original:\n",arr_1D);
get_sort_arr_1D=np.sort(arr_1D,order="Name");
print("Sorted Array:\n",get_sort_arr_1D);
print("---------------------------------Sorted number 2D array on Axis-0---------------------------------------------")
arr001=np.array([9,4,1,0,2,7]).reshape(2,3);
print("Original:\n",arr001);
print("Sorted array :\n",np.sort(arr001,axis=0));
print("---------------------------------Sorted number 2D array on Axis-1---------------------------------------------")
print("Sorted array :\n",np.sort(arr001,axis=1));
print("---------------------------------Sorted number 3D array on Axis-0---------------------------------------------")
# arr002=np.arange(100,370,10).reshape(3,3,3);
arr002=np.array([[[103,101,102],[701,801,401]],
                 [[862,321,921],[621,962,662]],
                 [[900,200,1090],[100,300,600]]])
print("Original Array:\n",arr002);
sorted_arr002_axis_0=np.sort(arr002,axis=0);
print("sorted_arr002_axis_0:\n",sorted_arr002_axis_0);
print("---------------------------------Sorted number 3D array on Axis-1---------------------------------------------")
print("Original Array:\n",arr002);
sorted_arr002_axis_1=np.sort(arr002,axis=1);
print("sorted_arr002_axis_1:\n",sorted_arr002_axis_1);
print("---------------------------------Sorted number 3D array on Axis-2---------------------------------------------")
print("Original Array:\n",arr002);
sorted_arr002_axis_2=np.sort(arr002,axis=2);
print("sorted_arr002_axis_2:\n",sorted_arr002_axis_2);


