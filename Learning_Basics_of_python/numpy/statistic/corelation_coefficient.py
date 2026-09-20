import numpy as np;
ar_2D_01=np.array([10,20,80,20,10,40,60,55,45,30])
ar_2D_02=np.array([1,2,3,4,9,8,7,6,5,4]);
make_cor_coeffi=np.corrcoef(ar_2D_01,ar_2D_02);
print("make_cor_coeffi:\n",make_cor_coeffi);


