from dataclasses import dataclass
import math
from atmosphere import G0

@dataclass
class Rocket:
    mass_structure: float  # Mass of the rocket structure in kilograms
    mass_fuel: float       # Mass of the fuel in kilograms
    thrust: float          # Thrust produced by the rocket in newtons
    Isp: float             # Specific impulse of the rocket engine in seconds
    diameter: float        # Diameter of the rocket in meters
    Cd: float              # Drag coefficient of the rocket

    @property
    def frontal_area(self):
        # Frontal area of the rocket in square meters
        return math.pi * (self.diameter / 2) ** 2

    @property
    def mdot(self):
        # Mass flow rate of the fuel in kg/s
        return self.thrust / (self.Isp * G0)  

    @property
    def burn_time(self):
        # Burn time of the rocket in seconds
        return self.mass_fuel / self.mdot  # Mass of the fuel divided by the mass flow rate


