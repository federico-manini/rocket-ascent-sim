# rocket-ascent-sim

Rocket ascent trajectory simulator in Python, with an ISA atmosphere model and RK4 integration.

## Status

Work in progress. The ISA atmosphere model, the Euler and RK4 integrators, the rocket model and the vertical equations of motion are complete and tested. The ascent simulation itself is under development.

## Features

- ISA standard atmosphere: temperature, pressure and density as a function of altitude (exact up to 20 km).
- Explicit Euler integrator for systems of ODEs with vector states.
- RK4 integrator for systems of ODEs with vector states.
- Rocket model (`Rocket` dataclass): structural mass, propellant mass, thrust, specific impulse, diameter and drag coefficient, with derived frontal area, propellant mass flow rate and burn time.
- Vertical equations of motion for the state `[h, v, m]`: thrust, quadratic aerodynamic drag, gravity decreasing with altitude and variable mass.
- Automated tests with `pytest` for the atmospheric model, the integrators (including convergence and accuracy checks), the rocket model and the equations of motion, plus a continuity check at the tropopause.

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

`euler_integrator(f, t0, tf, y0, dt)` returns the time grid `t` and an array `y` with one row per time step. `rk4_integrator` has the same signature and is fourth-order accurate.

Rocket model and equations of motion:

```python
from rocket import Rocket
from dynamics import derivatives

rocket = Rocket(mass_structure=22, mass_fuel=8, thrust=1500, Isp=220,
                diameter=0.15, Cd=0.5)
print(rocket.mdot)        # propellant mass flow rate ~ 0.695 kg/s
print(rocket.burn_time)   # ~ 11.5 s

# state = [altitude [m], velocity [m/s], mass [kg]]
dydt = derivatives(0.0, [0.0, 0.0, 30.0], rocket)
print(dydt)   # [0, ~40.19, ~-0.695]: initial acceleration ~ 40 m/s^2
```

Run the tests:

```bash
pytest
```

## Project structure

```
rocket-ascent-sim/
├── src/
│   ├── atmosphere.py            # ISA atmosphere model
│   ├── integrator.py            # Euler integrator, RK4 integrator
│   ├── rocket.py                # Rocket dataclass
│   └── dynamics.py              # gravity model and equations of motion
├── tests/
│   ├── test_atmosphere.py       # tests for the atmosphere
│   ├── test_integrator.py       # tests for the integrators
│   ├── test_rocket.py           # tests for the rocket model
│   └── test_dynamics.py         # tests for gravity and the equations of motion
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
- Motion is purely vertical (1D), with the positive axis pointing up.
- Gravity decreases with altitude as g(h) = g0 (R_T / (R_T + h))^2, with R_T = 6371 km.
- Aerodynamic drag is quadratic, D = 0.5 rho v |v| Cd A, with a constant drag coefficient.
- Thrust and specific impulse are constant (no dependence on altitude or ambient pressure) and act until the propellant is exhausted. The mass flow rate is T / (Isp g0).
- The Euler method is first-order accurate: the error decreases proportionally to the time step.
- The RK4 method is fourth-order accurate: the error decreases with the fourth power of the time step (verified in test_integrator.py).

## Roadmap

- [x] ISA atmosphere (0-20 km) with tests
- [x] Euler integrator with test
- [x] RK4 integrator, compared with Euler on a problem with a known solution
- [x] Rocket model and equations of motion with tests
- [ ] 1D ascent with thrust, drag and variable mass
- [ ] Validation against the analytical (Tsiolkovsky) solution
- [ ] Full ISA layers above 20 km
- [ ] 3DOF dynamics with gravity turn
- [ ] Comparison with OpenRocket / RocketPy
- [ ] Sensitivity analysis and final report

## License

See [LICENSE](LICENSE).




