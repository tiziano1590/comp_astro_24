import batman
import numpy as np
import matplotlib.pyplot as plt

c1,c2=np.genfromtxt("table Kepler-42 b.txt",skip_header=2,usecols=[8,10],unpack=True)
mean_c1=np.mean(c1)
mean_c2=np.mean(c2)

params = batman.TransitParams()         #object to store transit parameters
params.t0 = 0.                          #time of inferior conjunction
params.per = 1.21                       #orbital period
params.rp = 0.04                        #planet radius (in units of stellar radii)
params.a = 15.2                         #semi-major axis (in units of stellar radii)
params.inc = 90.                        #orbital inclination (in degrees)
params.ecc = 0.04                       #eccentricity
params.w = 90.                          #longitude of periastron (in degrees)
params.limb_dark = "quadratic"          #limb darkening model
params.u = [mean_c1,mean_c2]    #limb darkening coefficients [u1, u2, u3, u4]

t = np.linspace(-0.05, 0.05, 1000)      #times at which to calculate light curve
m = batman.TransitModel(params, t)      #initializes model

flux = m.light_curve(params)  

plt.plot(t, flux, 'r')
plt.xlabel('Time (days)')
plt.ylabel('Normalized flux')
plt.title('Kepler-42 b transit')
plt.show()