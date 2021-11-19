# -- CALCULATING Z VALUE --
import numpy as np
import scipy.stats as stats

x =  input()
xbar = np.mean(x)
mu = input()
sigma = np.std(x, ddof = 1)
n = len(x)

z_cal = (xbar - mu) / (sigma / np.sqrt(n))
print("Z calculated value is: ", round(z_cal,2))


# -- CALCULATING P-VALUE FOR z_cal --

# -- FOR ONE TAILED TEST
print(round(stats.norm.sf(abs(z_cal)),2))

# -- FOR TWO TAILED TEST
print(round(stats.norm.sf(abs(z_cal))*2,2))
