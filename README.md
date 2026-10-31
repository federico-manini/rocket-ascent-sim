# rocket-ascent-sim

Rocket ascent trajectory simulator in Python, with an ISA atmosphere model and RK4 integration.

## Status

Work in progress. The ISA atmosphere model and an Euler integrator are complete and tested. The RK4 integrator and the rocket model are under development.

## Features

- ISA standard atmosphere: temperature, pressure and density as a function of altitude (exact up to 20 km).
- Explicit Euler integrator for systems of ODEs with vector states.
- Automated tests with `pytest`, including a continuity check at the tropopause and a convergence check of the integrator.

## Installation

Requires Python 3 (developed with Python 3.15) and Git.

```bash
git clone https://github.com/federico-manini/rocket-ascent-sim.git
cd rocket-ascent-sim
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows (PowerShell)
# source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

## Usage

Atmosphere model:

```python
from atmosphere import isa

T, p, rho = isa(5000)   # altitude in metres
# T = temperature [K], p = pressure [Pa], rho = density [kg/m^3]
# at 5000 m: T = 255.65 K, p ~ 54020 Pa, rho ~ 0.736 kg/m^3
```

Numerical integration (free fall, state = [height, velocity]):

```python
import numpy as np
from integrator import euler_integrator

def free_fall(t, y):
    h, v = y
    return np.array([v, -9.81])

t, y = euler_integrator(free_fall, 0.0, 1.0, [100.0, 0.0], 0.001)
print(y[-1])   # ~ [95.0999, -9.81]  (exact height: 95.095 m)
```

`euler_integrator(f, t0, tf, y0, dt)` returns the time grid `t` and an array `y` with one row per time step.

Run the tests:

```bash
pytest
```

## Project structure

```
rocket-ascent-sim/
├── src/
│   ├── atmosphere.py            # ISA atmosphere model
│   └── integrator.py            # Euler integrator
├── tests/
│   ├── test_atmosphere.py       # unit tests for the atmosphere
│   └── test_euler_integrator.py # unit tests for the integrator
├── docs/                        # (planned) plots and reports
├── pytest.ini
├── requirements.txt
└── README.md
```

## Model and assumptions

- Troposphere (0-11 km): linear temperature decrease of 6.5 K/km, pressure from the barometric formula.
- Stratosphere (11-20 km): isothermal layer at 216.65 K, pressure decays exponentially.
- Above 20 km the model is an isothermal extrapolation, not the real ISA: the pressure is underestimated by roughly 2-3% at 25 km and 5-6% at 30 km compared with the standard atmosphere.
- Dry air with R = 287.05 J/(kg K) and constant g0 = 9.80665 m/s^2 in the barometric formula.
- Geopotential and geometric altitude are not distinguished.
- The Euler method is first-order accurate: the error decreases proportionally to the time step.

## Roadmap

- [x] ISA atmosphere (0-20 km) with tests
- [x] Euler integrator with test
- [ ] RK4 integrator, compared with Euler on a problem with a known solution
- [ ] 1D ascent with thrust, drag and variable mass
- [ ] Validation against the analytical (Tsiolkovsky) solution
- [ ] Full ISA layers above 20 km
- [ ] 3DOF dynamics with gravity turn
- [ ] Comparison with OpenRocket / RocketPy
- [ ] Sensitivity analysis and final report

## License

See [LICENSE](LICENSE).