import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
NOISE_DEVIATION=2
AMPL_VECTOR_SIN = ( 1,-1, 1,-1)
AMPL_VECTOR_COS = ( 1, 1,-1,-1)
TRANSMISION_NR=10 

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 

amplitudes_sin = list()
amplitudes_cos = list()
for i in range(TRANSMISION_NR):
    for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
        
        # modulation
        Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)     
        
        # real channel
        Rx = Tx + np.random.normal(0,NOISE_DEVIATION,len(Tx))
            
        # demodulation
        ampl = (np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE)*2  
        amplitudes_sin.append(ampl)
        
        ampl = (np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE)*2  
        amplitudes_cos.append(ampl)

# PRESENTATION
#plot
plt.scatter(amplitudes_cos,amplitudes_sin)
plt.title('RX amplitudes')
plt.xlabel('cos ampl.')
plt.ylabel('sin ampl.')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.grid()
plt.show()



# # amplitudes
# amplitudes_sin = np.array(amplitudes_sin) # convert list to numpy 1D array
# amplitudes_cos = np.array(amplitudes_cos) # ...
# np.set_printoptions(precision=2)          # set numpy array print precision

# print(f'amplitudes_sin = {amplitudes_sin}')
# errors =np.array(AMPL_VECTOR_SIN)-amplitudes_sin
# print(f'errors sin: {errors}')
# print(f'amplitudes_cos = {amplitudes_cos}')
# errors =np.array(AMPL_VECTOR_COS)-amplitudes_cos
# print(f'errors cos: {errors}')

