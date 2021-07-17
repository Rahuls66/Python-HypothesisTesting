# Z-test Confidence Interval

import scipy.stats as stats
import numpy as np

alpha = 
z_alphaby2 = stats.norm.isf(alpha/2)

x =  
sigma = np.std(x, ddof = 1)
xbar = np.mean(x)

margin_error = z_alphaby2 * sigma

lci = xbar - margin_error
uci = xbar + margin_error

print(str(int(100-alpha*100))+ "% Confidence Interval:  ", lci, uci)
