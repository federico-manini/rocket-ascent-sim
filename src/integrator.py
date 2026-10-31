import numpy as np


def euler_integrator(f, t0, tf, y0, dt):
    """Integrate dy/dt = f(t, y) from t0 to tf with the explicit Euler method."""
    
    n = round((tf - t0) / dt)
    t = np.linspace(t0, tf, n+1)
    y = [np.array(y0, dtype=float)]

    for i in range(n):
        y.append(y[-1] + dt * f(t[i], y[-1]))

    return t, np.array(y)


    