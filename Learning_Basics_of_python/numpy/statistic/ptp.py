import numpy as np;
ar_2D=np.arange(0,9,1).reshape(3,3);
print("Original:\n",ar_2D);
print("---------------------------------PTP in 2D Array-----------------------------------------")
print("without axis:-",np.ptp(ar_2D));
print("ptp at axis 0:-",np.ptp(ar_2D,axis=0));
print("ptp at axis 1:-",np.ptp(ar_2D,axis=1));
print("---------------------------------PTP in 3D Array-----------------------------------------")
ar_3D=np.arange(100,370,10).reshape(3,3,3);
print("Originl:\n",ar_3D);
print("without axis:-",np.ptp(ar_3D));
print("ptp at axis 0:-",np.ptp(ar_3D,axis=0));
print("ptp at axis 1:-",np.ptp(ar_3D,axis=1));
print("ptp at axis 2:-",np.ptp(ar_3D,axis=2));
