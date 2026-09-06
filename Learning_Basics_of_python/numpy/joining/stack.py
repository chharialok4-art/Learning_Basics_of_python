import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
make_stack_Axis_Zero=np.stack((array1,array2),axis=0);
print("--------------------------------Stack axis-0-(This can use as vstack axis-0)------------------------------------------------")
print("Array-1 Shape:",array1.shape);
print("Array-2 Shape:",array2.shape);
print("Shape Stacked Array:",make_stack_Axis_Zero.shape);
print("Stack One and Two Axis Zero:\n",make_stack_Axis_Zero);
print("--------------------------------Stack axis-1-(This can be use as vstack axis-1)------------------------------------------------")
make_stack_Axis_One=np.stack((array1,array2),axis=1);
print("Shape Stacked Array:",make_stack_Axis_One.shape);
print("Stack One and Two Axis One:\n",make_stack_Axis_One);
print("--------------------------------Stack axis-2-------------------------------------------------")
arr001=np.array([[100,200,300],["A1","B2","C3"]]);
arr002=np.array([[9,8,7],["A101","B202","C303"]]);
print("Shape arr001:",arr001.shape);
print("Shape arr002:",arr002.shape);
make_stack_Axis_two=np.stack((arr001,arr002),axis=2);
print("Shape Stacked Array:",make_stack_Axis_two.shape);
print("Stack One and Two Axis two:\n",make_stack_Axis_two);
print("--------------------------------Stack axis-1-------------------------------------------------")
make_stack_Axis_one001=np.stack((arr001,arr002),axis=1);
print("Shape Stacked Array:",make_stack_Axis_one001.shape);
print("Stack One and Two Axis two:\n",make_stack_Axis_one001);
print("--------------------------------Stack axis-0-------------------------------------------------")
make_stack_Axis_zero001=np.stack((arr001,arr002),axis=0);
print("Shape Stacked Array:",make_stack_Axis_zero001.shape);
print("Stack One and Two Axis two:\n",make_stack_Axis_zero001);