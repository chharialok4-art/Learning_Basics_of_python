import numpy as np;
arr_2D=np.array([[1,2,3],[10,20,30],["X","Y","Z"],[101,202,303],["A","B","C"],[100,200,300]]).reshape(6,3);
new_arr=[];
print("Original:\n",arr_2D);
for item in arr_2D:
    try:
        int(item[0]);
        new_arr.append(item);
    except ValueError:
        continue;
new_arr=np.asarray(new_arr);
print("Customize:\n",new_arr);
        