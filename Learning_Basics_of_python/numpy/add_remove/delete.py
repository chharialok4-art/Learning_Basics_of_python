import numpy as np;
def delete_1D(arr_1D):
    arr_1D=np.delete(arr_1D,4,axis=0);
    print(arr_1D);
def delete_2D(arr_2D):
    arr_2D=np.delete(arr_2D,2,axis=0);
    print(arr_2D);
def delete_2D_axis_one(arr_2D):
    arr_2D=np.delete(arr_2D,3,axis=1);
    print(arr_2D);
def delete_3D_axis_zero(arr_3D):
    arr_3D=np.delete(arr_3D,1,axis=0);
    print(arr_3D);
def delete_3D_axis_one(arr_3D):
    arr_3D=np.delete(arr_3D,2,axis=1);
    print(arr_3D);
def delete_3D_axis_two(arr_3D):
    arr_3D=np.delete(arr_3D,2,axis=2);
    print(arr_3D);
if __name__=="__main__":
    arr_1D=np.arange(1,10,1).flatten();
    print("---------------------------delete 1D axis-0------------------------------------")
    delete_1D(arr_1D);
    print("----------------------------delete 2D axis-0------------------------------------------------------")
    arr_2D=np.arange(9,21).reshape(3,4);
    delete_2D(arr_2D);
    print("----------------------------delete 2D axis-1------------------------------------------------------")
    delete_2D_axis_one(arr_2D);
    print("----------------------------delete 3D axis-0------------------------------------------------------")
    arr_3D=np.arange(100,2800,100).reshape(3,3,3);
    print(arr_3D,"\n")
    delete_3D_axis_zero(arr_3D);
    print("----------------------------delete 3D axis-1------------------------------------------------------")
    delete_3D_axis_one(arr_3D);
    print("----------------------------delete 3D axis-2------------------------------------------------------")
    delete_3D_axis_two(arr_3D);