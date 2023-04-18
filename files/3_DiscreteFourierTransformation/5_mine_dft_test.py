import numpy as np
import matplotlib.pyplot as plt

# plots stem plot fro given "y" vector
def my_stem_plot(y,title,y_range=(-6,7)):
    x = np.arange(len(y))    
    plt.stem(x,y,'-p')
    
    plt.ylim((-5,5))
    plt.xticks(x)
    plt.yticks(np.arange(*y_range))
    plt.grid()
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(4, 3.6)
    plt.show()

#----------------------------




