import batman
import numpy as np
import matplotlib.pyplot as plt

c1, c2 = np.genfromtxt('ExoCTK_results.txt', skip_header=2, usecols=(8,10), unpack=True)
mean_c1 = np.mean(c1)
mean_c2 = np.mean(c2)

params = batman.TransitParams()       #object to store transit parameters
params.t0 = 0.                        #time of inferior conjunction
params.per = 4.4                       #orbital period
params.rp = 0.11                      #planet radius (in units of stellar radii)
params.a = 9.73                        #semi-major axis (in units of stellar radii)
params.inc = 88.6                      #orbital inclination (in degrees)
params.ecc = 0.                       #eccentricity
params.w = 90.                        #longitude of periastron (in degrees)
params.limb_dark = "quadratic"        #limb darkening model
params.u = [mean_c1,mean_c2]      #limb darkening coefficients [u1, u2, u3, u4]

t = np.linspace(-0.3, 0.3, 1000)  #times at which to calculate light curve
m = batman.TransitModel(params, t)    #initializes model

flux = m.light_curve(params)

plt.plot(t, flux)
plt.xlabel('Time [days]')
plt.ylabel('Normalized flux')

plt.title('Transit (Wasp-62b)')