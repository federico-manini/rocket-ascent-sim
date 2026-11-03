import numpy as np
import pytest
from integrator import euler_integrator, rk4_integrator



def test_euler_exponential_growth():
    t, y = euler_integrator(lambda t, y: y, 0.0, 1.0, [1.0], 0.1)        #testo che il risultato dell integratore euleriano sia corretto per la crescita esponenziale. calcolando a mano il valore atteso e confrontandolo con quello calcolato dall integratore.
    assert y[-1, 0] == pytest.approx(1.1**10, rel=1e-9)


def test_rk4_exponential_growth():
    t, y = rk4_integrator(lambda t, y: y, 0.0, 1.0, [1.0], 0.1)
    assert y[-1, 0] == pytest.approx(np.e, rel=1e-6)


def test_rk4_is_more_accurate_than_euler():
    t, y_euler = euler_integrator(lambda t, y: y, 0.0, 1.0, [1.0], 0.1)
    t, y_rk4 = rk4_integrator(lambda t, y: y, 0.0, 1.0, [1.0], 0.1)

    error_euler = abs(y_euler[-1, 0] - np.e)          #e è il valore esatto dell esponenziale a t=1, quindi calcolo l errore dell integratore euleriano come differenza tra il valore calcolato e quello esatto.
    error_rk4 = abs(y_rk4[-1, 0] - np.e)

    assert error_rk4 < error_euler


def test_rk4_error_decreases_with_smaller_dt():
    t, y_small_dt = rk4_integrator(lambda t, y: y, 0.0, 1.0, [1.0], 0.05)
    t, y_large_dt = rk4_integrator(lambda t, y: y, 0.0, 1.0, [1.0], 0.1)

    error_small_dt = abs(y_small_dt[-1, 0] - np.e)
    error_large_dt = abs(y_large_dt[-1, 0] - np.e)

    assert error_small_dt < error_large_dt
    assert error_large_dt / error_small_dt == pytest.approx(16, rel=0.1)  # RK4 is 4th order, so error should decrease by a factor of ~16 when dt is halved





