import pytest
from atmosphere import isa, H_TROP


def test_sea_level():
    T, p, rho = isa(0)
    assert T == pytest.approx(288.15, rel=1e-3)
    assert p == pytest.approx(101325, rel=1e-3)
    assert rho == pytest.approx(1.225, rel=1e-3)


def test_5km():
    T, p, rho = isa(5000)
    assert T == pytest.approx(255.65, rel=1e-3)
    assert p == pytest.approx(54020, rel=1e-3)
    assert rho == pytest.approx(0.7361, rel=1e-3)


def test_tropopause():
    T, p, rho = isa(11000)
    assert T == pytest.approx(216.65, rel=1e-3)
    assert p == pytest.approx(22632, rel=1e-3)
    assert rho == pytest.approx(0.3639, rel=1e-3)


def test_15km():
    T, p, rho = isa(15000)
    assert T == pytest.approx(216.65, rel=1e-3)
    assert p == pytest.approx(12044, rel=1e-3)
    assert rho == pytest.approx(0.1937, rel=1e-3)


def test_20km():
    T, p, rho = isa(20000)
    assert T == pytest.approx(216.65, rel=1e-3)
    assert p == pytest.approx(5475, rel=1e-3)
    assert rho == pytest.approx(0.08804, rel=1e-3)


def test_tropopause_continuity():
    below = isa(H_TROP)
    above = isa(H_TROP + 0.001)
    assert above == pytest.approx(below, rel=1e-5)  