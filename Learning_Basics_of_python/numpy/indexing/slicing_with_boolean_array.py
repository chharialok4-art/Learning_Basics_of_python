import numpy as np;
arr_2D=np.arange(1,10,1).reshape(3,3);
print("Original:\n",arr_2D);
find_productive=arr_2D>5;
print("find Productive:\n",arr_2D[find_productive]);
arr_3D_with_hundreds=np.arange(100,370,10).reshape(3,3,3);
print("arr_3D_with_hundreds:\n",arr_3D_with_hundreds);
customized_arr=arr_3D_with_hundreds[(arr_3D_with_hundreds>290) & (arr_3D_with_hundreds<340)];
print("customized_arr:\n",customized_arr.reshape(2,2));