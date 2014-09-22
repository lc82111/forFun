#KL divergence
import numpy as np
import matplotlib.pyplot as plt

rho = np.linspace(-0.5,1.5,99999999)
rho_hat = 0.2

def KL(rho):
    return rho*np.log(rho/rho_hat)+(1-rho)*np.log((1-rho)/(1-rho_hat))
    
y=KL(rho)
    
plt.plot(rho, KL(rho))