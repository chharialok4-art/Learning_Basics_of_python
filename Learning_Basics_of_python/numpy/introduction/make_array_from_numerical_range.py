import numpy as np;
print("---------------------------line_space-----------------------------------------")
ar_line_space=np.linspace(0,20,50);
for item in ar_line_space:
    print(item);
print("---------------------------log_space-----------------------------------------")
arr_log_space=np.logspace(10,100,base=10);
for idx,item in enumerate(arr_log_space):
    print("(",idx,") :-",np.round(item,decimals=2));
print("---------------------------mesh_grid-----------------------------------------")
arr001=np.arange(0,3);
arr002=np.arange(100,104);
mk_mesh_grid=np.meshgrid(arr001,arr002);
print("Make_mesh_grid:\n",mk_mesh_grid);