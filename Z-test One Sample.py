# Calculating Z value:

import numpy as np
import scipy.stats as stats

x =  
xbar = np.mean(x)
mu = 
sigma = np.std(x, ddof = 1)
n = len(x)

z_cal = (xbar - mu) / (sigma / np.sqrt(n))
print("Z calculated value is: ", round(z_cal,2))



# Calculating p value for z_cal:

# FOR ONE TAILED TEST
print(round(stats.norm.sf(abs(z_cal)),2))

# FOR TWO TAILED TEST
print(round(stats.norm.sf(abs(z_cal))*2,2))
