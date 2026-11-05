import pytest
from rocket import Rocket
from dynamics import derivatives, gravity

def test_gravity_at_sea_level():
    h = 0
    g = gravity(h)
    assert g == pytest.approx(9.80665, rel=1e-5)

def test_gravity_at_10km():
    h = 10000
    g = gravity(h)
    assert g == pytest.approx(9.776, rel=1e-3)

def test_gravity_at_100km():
    h = 100000
    g = gravity(h)
    assert g == pytest.approx(9.506, rel=1e-3)


def test_derivatives_during_burn():
    # At t=0, h=0, v=0 there is no drag: a = (T - m*g0) / m = (1500 - 30*9.80665) / 30
    r = Rocket(mass_structure=22, mass_fuel=8, thrust=1500, Isp=220, diameter=0.15, Cd=0.5)
    y = [0.0, 0.0, 30.0]
    dh_dt, dv_dt, dm_dt = derivatives(0.0, y, r)
    assert dh_dt == 0.0
    assert dv_dt == pytest.approx(40.19, rel=1e-3)
    assert dm_dt == pytest.approx(-0.69526, rel=1e-3)


def test_derivatives_after_burnout():
    # t = 20 s > burn_time (11.5 s): no thrust, no mass flow.
    # Drag (~49 N) and weight (~216 N) both decelerate the rocket.
    r = Rocket(mass_structure=22, mass_fuel=8, thrust=1500, Isp=220, diameter=0.15, Cd=0.5)
    y = [1000.0, 100.0, 22.0]
    dh_dt, dv_dt, dm_dt = derivatives(20.0, y, r)
    assert dh_dt == 100.0
    assert dv_dt == pytest.approx(-12.04, rel=1e-2)
    assert dm_dt == 0.0