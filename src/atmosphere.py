import math

# CONSTANTS
T0 = 288.15                                                      # sea level standard temperature (K)
P0 = 101325                                                      # sea level standard pressure (Pa)
R_AIR = 287.05                                                   # specific gas constant for dry air (J/(kg·K))
G0 = 9.80665                                                     # standard gravity (m/s²)
T_GRAD = -0.0065                                                 # temperature gradient (K/m)
H_TROP = 11000                                                   # tropopause altitude (m)
T_TROP = T0 + T_GRAD * H_TROP                                    # tropopause temperature (K)
P_TROP = P0 * (1 + (T_GRAD*H_TROP)/T0)**(-G0/(R_AIR*T_GRAD))     # tropopause pressure (Pa)


def isa(h):
    """Return the ISA atmosphere properties at altitude h.

    Args:
        h: altitude above sea level (m).  

    Returns:
        (T, p, rho): temperature (K), pressure (Pa), density (kg/m^3). 

    Valid up to 20 km. 
    """
      
    if h <= H_TROP:
        T = T0 + T_GRAD * h
        p = P0 * (1 + (T_GRAD*h)/T0)**(-G0/(R_AIR*T_GRAD))
        rho =  p / (R_AIR*T)
    else:
        T = T_TROP
        p = P_TROP * math.exp(-G0 * (h - H_TROP) / (R_AIR * T))
        rho =  p / (R_AIR*T)
    
    return T, p, rho



                                    



       