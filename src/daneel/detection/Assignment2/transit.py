import batman
import numpy as np
import matplotlib.pyplot as plt

params = batman.TransitParams()       #object to store transit parameters
params.t0 = 0.                        #time of inferior conjunction
params.per = 1.21                       #orbital period
params.rp = 0.04                      #planet radius (in units of stellar radii)
params.a = 15.2                        #semi-major axis (in units of stellar radii)
params.inc = 90.                      #orbital inclination (in degrees)
params.ecc = 0.04                       #eccentricity
params.w = 90.                        #longitude of periastron (in degrees)
params.limb_dark = "nonlinear"        #limb darkening model
params.u = [0.521,0.008,0.353,0.011]      #limb darkening coefficients [u1, u2, u3, u4]

t = np.linspace(-0.05, 0.05, 1000)  #times at which to calculate light curve
m = batman.TransitModel(params, t)    #initializes model

flux = m.light_curve(params)                   #calculates light curve

plt.plot(t, flux, 'r')
plt.xlabel('Time (days)')
plt.ylabel('Normalized flux')
plt.show()