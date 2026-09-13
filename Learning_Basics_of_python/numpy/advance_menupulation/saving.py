# import numpy as np

# # Create an array
# array = np.array([[1, 2, 3], [4, 5, 6]])

# #Save the array to a text file
# np.savetxt('/Users/dev/Downloads/New_Alok001.txt',array)
# print ('File Saved succesfully!!')

import numpy as np

# Create multiple arrays
array1 = np.array([1, 2, 3])
array2 = np.array([[4, 5, 6], [7, 8, 9]])

# Save the arrays to a .npz file
np.savez('/Users/dev/Downloads/arrays.npz', array1=array1, array2=array2)
print ("File saved!!")