import numpy as np;
ar_01=np.array([[10,20,30],
                [101,202,303],
                [100,200,300]]);
ar_02=np.array([[10,20,30],
                [101,202,303],
                [100,200,300]]);
if np.array_equal(ar_01,ar_02):
    print("True");
else:
    print("False");
print("-----------------------------------equal to----------------------------------------")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 2]])

dif = arr1 == arr2
b = dif.all()
print(b)
print("-------------------------smaller and greater---------------------------------")
arr001=np.array([[[10,20,30],[101,202,303]],[[100,200,300],[101,102,103]],[[201,202,203],[301,302,303]]]);
arr002=np.array([[[10,100,30],[101,200,303]],[[100,201,300],[101,902,103]],[[901,202,203],[301,307,303]]]);
get_greater=np.greater_equal(arr001,arr002);
print("Get_Boolean:\n",get_greater);
print("get_array:\n",arr002[get_greater]);
