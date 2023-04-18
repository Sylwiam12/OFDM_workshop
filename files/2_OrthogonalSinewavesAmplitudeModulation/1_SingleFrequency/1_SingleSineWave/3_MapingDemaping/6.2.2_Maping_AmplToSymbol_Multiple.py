import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

symbol_nrl = (2,4,8)
ampl_l = np.linspace(-1,1,100)
for symbol_nr in symbol_nrl:
    symbols_l = list()
    for ampl in ampl_l:
        symbol = ampl_to_symbol(symbol_nr,ampl)
        symbols_l.append(symbol)    
    plt.plot(ampl_l,symbols_l,'p-', label=f'symbol nr = {symbol_nr}')    
plt.grid()
plt.xlabel('Amplitude')
plt.ylabel('Symbol')
plt.legend()
plt.show()   
