import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 160
AMPL_VECTOR = np.linspace(1,4,8)
NOISE_DEVIATION=0.8
TRANSMISION_NR=100
# CALCULATION
t = np.linspace(0,2*pi ,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
amplitudes_l=[] # create amplitude list
for i in range(TRANSMISION_NR):
    amp = AMPL_VECTOR[i%8]
    #modulation
    Tx = amp*Carrier
    # perfect channel
    Rx=Tx+ np.random.normal(0,NOISE_DEVIATION,TIME_VECTOR_SIZE)     
    # demodulation
    Ref  = np.sin(t)    
    dot  = np.dot(Rx,Ref)
    amplitudes_l.append(2*dot/TIME_VECTOR_SIZE)

# plot  
plt.plot(amplitudes_l[::8],'p')
plt.plot(amplitudes_l[1::8],'p')
plt.plot(amplitudes_l[2::8],'p')
plt.plot(amplitudes_l[3::8],'p')
plt.plot(amplitudes_l[4::8],'p')
plt.plot(amplitudes_l[5::8],'p')
plt.plot(amplitudes_l[6::8],'p')
plt.plot(amplitudes_l[7::8],'p')
plt.title(f'NOISE DEVIATION = {NOISE_DEVIATION}')
plt.grid()
plt.show()
print(f'received amplitudes: {amplitudes_l}')





































# import numpy as np
# import matplotlib.pyplot as plt
# pi = np.pi

# # PARAMETERS
# TIME_VECTOR_SIZE = 60
# AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2, 3.4)

# # CALCULATION
# t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

# # modulation
# Carrier = np.sin(t)
# amplitudes_l=[] # create amplitude list
# t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
# for k in range(4):
#     Tx = AMPL_VECTOR[k]*Carrier
#     # channel
#     noise=np.random.normal(loc=0.0,scale=0.3,size=len(Tx)) 
#     Rx=Tx+noise# ideal one    
#     # demodulation
#     Ref  = np.sin(t)
#     dot  = np.dot(Rx,Ref)
#     amplitudes_l.append(2*dot/TIME_VECTOR_SIZE)

# # PRESENTATION  
# # Rx plot
# plt.plot(Rx)
# plt.axhline(y=0,color='black')
# plt.grid(axis='y')
# plt.show()

# #  
# print(f'received amplitudes: {amplitudes_l}')
