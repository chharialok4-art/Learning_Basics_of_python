import numpy as np;
num1 = np.array([1, 2])
num2 = np.array([[10, 20],
                 [30, 40]]);
concetenate_both=np.concatenate((num2,[num1]),axis=0);
print(concetenate_both);