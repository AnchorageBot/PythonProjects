# This script will use object oriented programming to turn a lightswitch on and off

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
        
aLightSwitch = LightSwitch()

print("Light is on:  ")
aLightSwitch.show()

print()

print("Light is on:  ")
aLightSwitch.turnOnLight()
aLightSwitch.show()

print()

print("Light is on:  ")
aLightSwitch.turnOffLight()
aLightSwitch.show()
