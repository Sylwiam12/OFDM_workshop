import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = np.pi/2 + np.pi/2
PHASE_lst=[0,pi/8,pi/4,pi/2,np.pi/2 + np.pi/8,np.pi/2 + np.pi/4,np.pi/2 + np.pi/3,np.pi/2 + np.pi/2]
dot_lst=[]
# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)
Ref = np.sin(t)
# Shifted = np.sin(t+PHASE_SHIFT)
# Ref_mult_Shifted = Ref*Shifted
# dot_product = np.sum(Ref_mult_Shifted) # use Ref_mult_Shifted

for phase in PHASE_lst:
    Shifted = np.sin(t+phase)
    Ref_mult_Shifted = Ref*Shifted
    dot_product = np.sum(Ref_mult_Shifted) # use Ref_mult_Shifted
    dot_lst.append(dot_product)

plt.plot(PHASE_lst,dot_lst,'o-',color='cornflowerblue')
plt.xlabel('shift')
plt.ylabel('dot')
plt.xlim(-0.25,3.25)
plt.ylim(-15.25,15.25)
plt.grid()
plt.show()

# #PLOTS (HINT: use separate plots, not one with grid)
# #components
# plt.subplot(2,1,1)
# #plotting Shifted and Ref
# plt.plot(t, Ref,'o-', label='Sin', color='blue')
# plt.plot(t, Shifted,'o-',label='SinShift',color='green')
# plt.title('Components')
# plt.xlim(-0.25,6.25)
# plt.ylim(-1.25,1.25)
# plt.grid()
# plt.legend(loc='upper right')
# # multiplication, HINT: use "stem" function for ploting
# plt.subplot(2,1,2)
# markerline, stemlines, baseline = plt.stem(t, Ref_mult_Shifted,label='Sin_mult_SinShift')
# markerline.set_markerfacecolor('orange')
# markerline.set_markeredgecolor('orange')
# plt.title('Multiplication')
# plt.xlim(-0.25,6.25)
# plt.ylim(-1.25,1.25)
# plt.legend(loc='lower left')
# plt.grid()
# plt.show(block=True)
# #print phase shift and dot product value
# print('phase_shift',f'{PHASE_SHIFT:.2f}','\ndot_product = ',f'{dot_product:.2f}')

