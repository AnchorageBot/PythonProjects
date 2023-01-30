# This script will use object oriented programming to turn two different lightswitchs on and off

# Reference:
    # Object-Oriented Python by Irv Kalb
    # https://github.com/IrvKalb/Object-Oriented-Python-Code
    # Chapter 2

# Made with Mu v.1.0.3
    # January 2023
    # https://codewith.mu
    
class LightSwitch():
    def __init__(self):
        self.switchOn = False
        
    def turnOnLight(self):
        self.switchOn = True
        
    def turnOffLight(self):
        self.switchOn = False
        
    def show(self):
        print(self.switchOn)
 
KitchenLight = LightSwitch()
OfficeLight = LightSwitch()

print("Kitchen Light is on:  ")
KitchenLight.show()

print()

print("Kitchen Light is on:  ")
KitchenLight.turnOnLight()
KitchenLight.show()

print()

print("Kitchen Light is on:  ")
KitchenLight.turnOnLight()
KitchenLight.show()

print()
print()
print()

print("Office Light is on:  ")
OfficeLight.show()

print()

print("Office Light is on:  ")
OfficeLight.turnOnLight()
OfficeLight.show()

print()

print("Office Light is on:  ")
OfficeLight.turnOnLight()
OfficeLight.show()
