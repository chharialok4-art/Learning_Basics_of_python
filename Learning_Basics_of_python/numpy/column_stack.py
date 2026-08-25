import numpy as np;
arr001=np.array([1,2,3]);
arr002=np.array([111,222,333]);
make_column_stack_1D=np.column_stack((arr001,arr002));
print("-------------------------------Column_stack 1D--------------------------------------------")
print("Shape make_column_stack_1D:",make_column_stack_1D.shape);
print("make_column_stack_1D:\n",make_column_stack_1D);
print("-------------------------------Column_stack 2D--------------------------------------------")
arr1=np.array([[1,2,3],["A","B","C"]]);
arr2=np.array([[111,222,333],["001","002","003"]]);
make_column_stack_2D=np.column_stack((arr1,arr2));
print("Shape make_column_stack_2D:",make_column_stack_2D.shape);
print("make_column_stack_2D:\n",make_column_stack_2D);
print("-------------------------------Column_stack 3D--------------------------------------------")
ar01=np.array([[[1,2,3],[100,200,300]],[[101,202,303],["a","b","c"]],[["AB","CD","EF"],["A01","B02","C03"]]]);
ar02=np.array([[["A1","B2","C3"],["A100","B200","C300"]],[["A101","B202","C303"],["1a","2b","3c"]],[["01AB","02CD","03EF"],["001A01","002B02","003C03"]]]);
make_column_stack_3D_to_3D=np.column_stack((ar01,ar02));
print("Shape make_column_stack_3D_to_3D:",make_column_stack_3D_to_3D.shape);
print("make_column_stack_3D_to_3D:\n",make_column_stack_3D_to_3D);
NOTE="Column_stack behave for 1D array as same as dstack and for 2D array it behave as" \
"hstack and it works for 2D array if you give 3D array it behave differently";
