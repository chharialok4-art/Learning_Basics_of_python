import numpy as np;
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("Shape Array 1:",array1.shape)
print("Shape Array 2:",array2.shape)
make_concatenate=np.concatenate((array1, array2));
print("Shape of make_concatenate:",make_concatenate.shape);
print("After Join:",make_concatenate);
print("---------------------------------------Another Example------------------------------------------")
array3 = np.array([[1, 2], [3, 4]])
array4 = np.array([[5, 6], [7, 8]])
print("Array 3:",array3,"Shape of array 3:",array3.shape);
print("Array 4:",array4,"Shape of array 4:",array4.shape);
print("-----------------------------------Concatenate axis=0----------------------------------------")
make_another_concatenate_at_axis_zero=np.concatenate((array3,array4),axis=0);
print("make_another_concatenate_at_axis_zero:",make_another_concatenate_at_axis_zero)
print("Shape Axis-0:",make_another_concatenate_at_axis_zero.shape)
print("--------------------------------Concatenate axis=1--------------------------------------------------")
make_another_concatenate_at_axis_one=np.concatenate((array3,array4),axis=1);
print("make_another_concatenate_at_axis_one:",make_another_concatenate_at_axis_one);
print("Shape Axis-1:",make_another_concatenate_at_axis_one.shape)


