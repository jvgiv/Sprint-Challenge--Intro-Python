# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    def __init__(self, name):
        self.name = name

class GroundVehicle(Vehicle):
    def __init__(self, name):
        self.name = name

class Car(GroundVehicle):
    def __init__(self, name, horsepower):
        self.name = name
        self.horsepower = horsepower

class Motorcycle(GroundVehicle):
    def __init__(self, name, cubic_centimeters):
        self.name = name
        self.cubic_centimeters = cubic_centimeters

class FlightVehicle(Vehicle):
    def __init__(self, name):
        self.name = name

class Starship(FlightVehicle):
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

class Airplane(FlightVehicle):
    def __init__(self, name, propulsion_type):
        self.name = name
        self.propulsion_type = propulsion_type

plane = Airplane("Jet", "Jet thrust")
ship = Starship("Saucer", "55000")

print(ship.max_speed)