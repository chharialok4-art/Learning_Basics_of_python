import numpy as np;
li001=[1,2,10,3.4,"Alok",False];
print("-------------------------------asarray()----------------------------------------")
print("Raw Array:\n",li001)
make_numpy_array=np.asarray(li001);
print("Numpy Array:\n",make_numpy_array);
li002=[["Alok","Aman","Darshi"],[101,102,103],[True,False,False]];
print("Raw list:\n",li002);
make_numpy_array_li002=np.asarray(li002);
print("make_numpy_array_li002:\n",make_numpy_array_li002);
print("-------------------------------from_buffer()----------------------------------------")
str001=b"Alok Chhari is good boy";
mk_numpy_array=np.frombuffer(str001,dtype="S1");
print("byte_numpy_Array:\n",mk_numpy_array);
print("-------------------------------from_iter()----------------------------------------")
tup001=(1,2,3,4,5,6,7,8,9,10);
mk_arr_from_tuple=np.fromiter(tup001,dtype=int);
print("From tuple:\n",mk_arr_from_tuple);
