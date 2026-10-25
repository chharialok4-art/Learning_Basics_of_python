import numpy as np;
signal=[0,1,0,-1,0,1,0,-1,0];
gen_dft= np.fft.fft(np.array(signal));
print("Length of signal:-",len(signal));
print("DFT:-",gen_dft);
print("-------------------------------------------------------------------------")
print("fftfreq:-",np.fft.fftfreq(len(signal),1))
print("Length of DFT:-",len(gen_dft));
print("--------------------------------------------------------------------------")
print(np.fft.fftfreq(4, d=1))
get_rand=np.arange(1024)
print(len(np.fft.fft(get_rand)))