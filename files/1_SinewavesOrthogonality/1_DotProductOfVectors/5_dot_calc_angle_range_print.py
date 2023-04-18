import numpy as np
from mylib import rotate_vector 
blue=[0,1]
green=[0,1]
for degree in range(0,370,10):
    rot_vector=rotate_vector(blue,degree)
    result=np.dot(green,rot_vector)
    print(f'{degree:03d} : {result:+.3f}')


# #generating figure
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal #required for triangle signal generation
# pi = np.pi 
# t = np.linspace(0, 3*2*pi,num=45, endpoint=False) 
# sin_b = -1.5*np.sin(t)
# trian_a = 3*signal.sawtooth(t,0.5)
# sum = sin_b+trian_a
# plt.plot(t,sum,'--',label='sum',color='red')
# plt.plot(t,trian_a,'p-',label='triangle',color='green')
# plt.plot(t,sin_b,'p', label='sinusoid', color='blue')
# plt.title('triangle + sinus')
# plt.xlabel('tempus[s]')
# plt.ylabel('amplitude[a.u.]')
# plt.xlim(0,10)
# plt.ylim(-4,6)
# plt.axhline(y=0,color='yellow')
# plt.grid()
# plt.legend()
# plt.show()