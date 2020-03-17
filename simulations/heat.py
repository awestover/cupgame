
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def f(k,a):
    return (1-k)**(a+1) - (1-k**a)

data = [[abs(f(k,a)) for k in np.linspace(0,1,100)] for a in np.linspace(0,1,100)]

sns.heatmap(data)
plt.show()

