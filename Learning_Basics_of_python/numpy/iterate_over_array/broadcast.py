import numpy as np;
print("------------------------------broadcast array------------------------------------------------")
ar_2d=np.arange(0,6,1).reshape(2,3);
ar_1D=np.arange(100,400,100);
mk_boradcast=np.broadcast(ar_1D,ar_2d);
for idx,item in mk_boradcast:
    print(idx,item); 