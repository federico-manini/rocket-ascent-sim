import pytest
from rocket import Rocket



def test_frontal_area():
    r = Rocket(mass_structure=22, mass_fuel=8, thrust=1500, Isp=220, diameter=0.15, Cd=0.5)
    expected_area = 0.017671
    assert r.frontal_area == pytest.approx(expected_area, rel=1e-3)


def test_mdot():
    r = Rocket(mass_structure=22, mass_fuel=8, thrust=1500, Isp=220, diameter=0.15, Cd=0.5)
    expected_mdot = 0.69526
    assert r.mdot == pytest.approx(expected_mdot, rel=1e-3)


def test_burn_time():
    r = Rocket(mass_structure=22, mass_fuel=8, thrust=1500, Isp=220, diameter=0.15, Cd=0.5)
    expected_burn_time = 11.506     
    assert r.burn_time == pytest.approx(expected_burn_time, rel=1e-3)







    