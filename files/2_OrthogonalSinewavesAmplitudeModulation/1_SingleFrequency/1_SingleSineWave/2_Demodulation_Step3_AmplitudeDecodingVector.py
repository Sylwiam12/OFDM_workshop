import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60
PERIOD_NUMBER = 5

# loading Rx vector from file and..
Rx = np.load("C:/Users/micha/OneDrive/Pulpit/agh_ofdm/files/2_OrthogonalSinewavesAmplitudeModulation/1_SingleFrequency/1_SingleSineWave/TxSignal_Exercise.npy")

# .. ploting it
plt.plot(Rx)
plt.grid()
plt.show()

# spliting vector into time slots coresponding to single periods
RxPeriods = np.reshape(Rx,(5,60))

# decoding amplitudes of Rx time slots

ampl_lst=[] # create amplitude list
t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)
for RxPeriod in RxPeriods:
    Ref  = np.sin(t)    
    dot  = np.dot(RxPeriod,Ref)
    ampl_lst.append(2*dot/PERIOD_VECTOR_SIZE)
    
print(ampl_lst)  # print list
    



