# This script will use object oriented programming for a light dimmer switch

# Definitions and concepts
    # A class is a blueprint for an object
    # An object is a set of variables and methods 
    # <object>.<methodName>(<argument>)
    # A method is a function inside of a class
    # All methods have a special first parameter named <self>

# Reference:
    # Object-Oriented Python by Irv Kalb
    # https://github.com/IrvKalb/Object-Oriented-Python-Code
    # Chapter 2

# Made with Mu v.1.0.3
    # February 2023
    # https://codewith.mu
    
class LightDimmerSwitch():
    def __init__(self):
        self.dimmerSwitchOn = False
        self.brightness = 5
        
    def turnOnLight(self):
        self.dimmerSwitchOn = True
        
    def turnOffLight(self):
        self.dimmerSwitchOn = False
        
    def brighterLight(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
            
    def dimmerLight(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
            
    def show(self):
        """This method(function) is for testing/debugging"""
        print("Light Dimmer Switch is on ?", self.dimmerSwitchOn)
        print("Dimmer Switch Brightness is ", self.brightness)
        
KitchenDimmer = LightDimmerSwitch()

print("Kitchen Light is off:  ")
KitchenDimmer.show()

print()

print("Kitchen Light is on:  ")
KitchenDimmer.turnOnLight()
KitchenDimmer.show()

print()

print("Kitchen Light is off:  ")
KitchenDimmer.turnOffLight()
KitchenDimmer.show()

print()

print("Kitchen Light is on and brightness has been increased:  ")
KitchenDimmer.turnOnLight()
KitchenDimmer.brighterLight()
KitchenDimmer.show()

print()

print("Kitchen Light is on and brightness has been decreased:  ")
KitchenDimmer.turnOnLight()
KitchenDimmer.dimmerLight()
KitchenDimmer.show()
