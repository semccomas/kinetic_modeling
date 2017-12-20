import numpy as np 
from scipy import optimize

#assuming 3 states right now: R <-> O <-> I and that I and R are also connectable
a = np.array([0, -13, -14, -15, -14, -13, -7, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1])
# a is the test data, where each new value is the timestep in which the measurement was taken
O = 0
R = 0
I = 0
(O, R, I) = initial

#parameters
k1 = 1 # R -> O
k2 = 2 # O -> R
k3 = 3 # O -> I
k4 = 3 # R -> I
k5 = 3 # I -> R
k6 = 3 # I -> O
rates = (k1, k2, k3, k4, k5, k6)

T0 = 0 #initial time
TE = 30 #end time(ms)


def eq(rates, initial, start_t, end_t, meas):
	k1, k2, k3, k4, k5, k6 = rates
	O, R, I = initial
	t = np.linspace(start_t, end_t, meas)   #linspace creates an array of start -> end with meas number of elements
    #model equations:
	d0 = R*k1 - O*k2 - O*k3 + I*k6
	dR = -R*k1 + O*k2 - R*k4 + I*k5
	dI = O*k3 + R*k4 - I*k5 -I*k6
	O = O + d0
