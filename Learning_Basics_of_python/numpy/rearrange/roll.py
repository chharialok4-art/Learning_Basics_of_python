import numpy as np;
def roll_1D(arr_1D):
    arr_1D=np.roll(arr_1D,3,axis=0);
    print("Original:\n",arr_1D);
def roll_2D_axis_0(arr_2D):
    arr_2D_axis_0=np.roll(arr_2D,2,axis=0);
    print("Original:\n",arr_2D_axis_0);
def roll_2D_axis_1(arr_2D):
    arr_2D_axis_1=np.roll(arr_2D,3,axis=1);
    print("Original:\n",arr_2D_axis_1);
if __name__=="__main__":
    arr_1d=np.arange(0,6).flatten();
    print("---------------------------------roll 1D axis-0----------------------------------------")
    print("Sample:\n",arr_1d);
    roll_1D(arr_1d);
    print("---------------------------------roll 2D axis-0----------------------------------------")
    arr_2D=np.arange(100,112,1).reshape(3,4);
    print("Sample:\n",arr_2D);
    roll_2D_axis_0(arr_2D);
    print("---------------------------------roll 2D axis-1----------------------------------------")
    print("Sample:\n",arr_2D);
    roll_2D_axis_1(arr_2D);