# -- CALCULATING Z VALUE -- 
import numpy as np
import scipy.stats as stats

x = input
xbar = np.mean(x)
mu = input()
sigma = np.std(x, ddof = 1)
n = len(x)

z_cal = (xbar - mu) / (sigma / np.sqrt(n))
print("Z calculated value is: ", round(z_cal,2))

alpha = input()
z_alphaby2 = stats.norm.isf(alpha/2)


# -- CALCULATING CONFIDENCE INTERVAL -- 
margin_error = z_alphaby2 * sigma

lci = xbar - margin_error
uci = xbar + margin_error

print(str(int(100-alpha*100))+ "% Confidence Interval:  ", lci, uci)
