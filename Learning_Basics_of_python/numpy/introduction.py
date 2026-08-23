import numpy as np;
make_one=np.array([[1,2,3],[10,None,30],[25,35,45]],order="C",subok=True);
print(make_one);
print("Shape-Make One:",make_one.shape);
print("Stride-Make one:",make_one.strides);
print("-----------------------------------------------------------------------------")
matrix001=[[100,200,300],[101,202,303],[0,0,0]];
make_two=np.array(matrix001,order="C");
print(make_two);
print("Shape-Make two:",make_two.shape);
print("Strides-Make two:",make_two.strides);