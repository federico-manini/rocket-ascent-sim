import numpy as np
import pytest
from integrator import euler_integrator


def test_exponential_growth():
    t, y = euler_integrator(lambda t, y: y, 0.0, 1.0, [1.0], 0.1)
    assert y[-1, 0] == pytest.approx(1.1**10, rel=1e-9)