import numpy as np
from atmosphere import isa, G0

R_T = 6371000  # Earth's radius in meters

def gravity(h):
    #Calculate the gravitational acceleration at altitude h.
    return G0 * (R_T / (R_T + h))**2  # Gravitational acceleration decreases with altitude


def derivatives(t, y, rocket):
    h, v, m = y  # State vector: h = altitude, v = velocity, m = mass
    
    if t < 0 or t > rocket.burn_time:
        thrust = 0.0
        mdot = 0.0
    else:
        thrust = rocket.thrust
        mdot = rocket.mdot

    rho = isa(h)[2]  
    D = 0.5 * rho * v * abs(v) * rocket.Cd * rocket.frontal_area
    g = gravity(h)
    dh_dt = v  # Rate of change of altitude is the velocity
    dv_dt = (thrust - D - m*g) / m  # Rate of change of velocity considering thrust, drag, and gravity
    dm_dt = -mdot  # Mass decreases due to fuel consumption
    
    return np.array([dh_dt, dv_dt, dm_dt])

