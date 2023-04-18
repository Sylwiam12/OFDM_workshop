import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

noise_deviationl =np.linspace(0,5,20)
symbol_nrl = (2,4,8)
t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier

# TRANSMISION-RECEPTION
for symbol_nr in symbol_nrl:
    symbols_tx = np.random.randint(0,symbol_nr,TRANSMISIONS_NR)    
    error_lst=[]
    for n_dev in noise_deviationl:
        symbols_rx = list()  
        for symbol in symbols_tx:   
            # modulation
            ampl = symbol_to_ampl(symbol_nr,symbol)
            Tx = ampl*Carrier        
            # real channel
            Rx = Tx + np.random.normal(0,n_dev,TIME_VECTOR_SIZE)  
            # demodulation
            ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
            symbol = ampl_to_symbol(symbol_nr,ampl)
            
            symbols_rx.append(symbol)
        error_lst.append(sum(np.array(symbols_rx) != symbols_tx))
    # PRESENTATION   
    plt.plot(noise_deviationl,error_lst,'p-', label=f'symbol nr= {symbol_nr}')   
plt.xlabel('noise deviation')
plt.ylabel('error nr')
plt.grid()
plt.legend()
plt.show()

