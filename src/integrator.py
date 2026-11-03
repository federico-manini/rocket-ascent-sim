import numpy as np


def euler_integrator(f, t0, tf, y0, dt):
    """Integrate dy/dt = f(t, y) from t0 to tf with the explicit Euler method."""
    
    n = round((tf - t0) / dt)
    t = np.linspace(t0, tf, n+1)
    y = [np.array(y0, dtype=float)]

    for i in range(n):
        y.append(y[-1] + dt * f(t[i], y[-1]))

    return t, np.array(y)


def rk4_integrator(f, t0, tf, y0, dt):
    """Integrate dy/dt = f(t, y) from t0 to tf with the classical 4th-order Runge-Kutta method."""
    n = round((tf - t0) / dt)
    t = np.linspace(t0, tf, n + 1)
    y = [np.array(y0, dtype=float)]

    for i in range(n):
        ti = t[i]
        yi = y[-1]

        k1 = f(ti, yi)
        k2 = f(ti + 0.5 * dt, yi + 0.5 * dt * k1)
        k3 = f(ti + 0.5 * dt, yi + 0.5 * dt * k2)
        k4 = f(ti + dt, yi + dt * k3)

        y.append(yi + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))

    return t, np.array(y)
