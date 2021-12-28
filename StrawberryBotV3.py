# This script will read/share data from soil & air sensors using the FBS' serial, BLE, and onboard neopixel

# Script Source/Engineering
  # https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test
  # https://learn.adafruit.com/adafruit-feather-sense
  # https://www.youtube.com/profgallaugher
  # https://github.com/AnchorageBot/YouTube

# Hardware Bill of Materials
  # Soil Sensor https://www.adafruit.com/product/4026
  # JST Cable https://www.adafruit.com/product/3955
  # Feather Bluefruit Sense https://www.adafruit.com/product/4516
  # USB C to Micro B Cable https://www.adafruit.com/product/3878
  # JST 2 Pin jumper cable https://www.adafruit.com/product/4714
  # Universal USB/DC/Lithium Charger https://www.adafruit.com/product/4755
  # 3.5mm / 1.1mm to 5.5mm / 2.1mm DC Jack Adapter https://www.adafruit.com/product/4287
  # Medium Solar panel - 6V 2W  https://www.adafruit.com/product/200
  # Round Solar Panel Skill Badge - 5V / 40mA https://www.adafruit.com/product/700
  # Lithium Ion Polymer Battery - 3.7v 500mAh https://www.adafruit.com/product/1578
  # Flanged Weatherproof Enclosure With PG-7 Cable Glands https://www.adafruit.com/product/3931

# Software
  # Mu Python Editor https://codewith.mu
  # CircuitPython v 7.0 https://circuitpython.org/board/feather_bluefruit_sense/
  # Libraries v 7.x bundle https://circuitpython.org/libraries
    # adafruit_ble
    # adafruit_ble_adafruit
    # adafruit_bluefruit_connect
    # adafruit_bus_device
    # adafruit_register    
    # adafruit_apds9960    
    # adafruit_lsm6ds
    # adafruit_seesaw.mpy
    # adafruit_bmp280.mpy
    # adafruit_lis3mdl.mpy
    # adafruit_sht31d.mpy
    # neopixel.mpy

# Wiring Pattern for Soil Sensor to FBS
  # Red   - 3.3V
  # Black - Ground
  # White - SCA
  # Green - SCL

# Import libraries
import time
import board
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_seesaw.seesaw import Seesaw
import adafruit_bmp280
#import adafruit_sht31d
import neopixel

# Setup the BLE radio
ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

# Setup I2C
i2c = board.I2C()
i2c_bus = board.I2C()

# Setup soil sensors
ss = Seesaw(i2c_bus, addr=0x36)

# Soil sensors global variables
soil_temp = ss.get_temp()
soil_moist = ss.moisture_read()

# Setup board (air) sensors
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.sea_level_pressure = 1013.25                 # Set this to sea level pressure in hectoPascals at your location
#sht31d = adafruit_sht31d.SHT31D(i2c)

# Board (air) sensors global variables
board_temp = bmp280.temperature
board_press = bmp280.pressure
board_altd = bmp280.altitude
#board_humidty = sht31d.relative_humidity

# Setup the onboard neopixel, associated global variables, & define neopixel blink pattern function
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.1

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
FIRSTBLINK = 0.5
NEXTBLINK = 0.75
TIMESLEEP = 2

def NeoPixelPattern(color):
    pixel.fill(color)
    time.sleep(FIRSTBLINK)
    pixel.fill(BLACK)
    time.sleep(NEXTBLINK)

# Define the sensor data reporting functions
def SensorSerial_Report():
    print("BerrySeven MCU")
    print(("soil temp: C " + str(soil_temp) + "  soil moisture:  " + str(soil_moist)))
    print("\n")
    print("air temp: C " + str(board_temp), "air pressure: hPa " + str(board_press))
    print("altitude: m " + str(board_altd))
    #print("air humidity: % " + str(board_humidity))
    print("\n")

    if soil_moist <= 800:                           # 600 - 800 (soil), 570 (water), 320 (air)
        # blink good to go neopixel pattern
        NeoPixelPattern(GREEN)
        time.sleep(TIMESLEEP)
    else:
        # blink water plant neopixel pattern
        NeoPixelPattern(RED)
        time.sleep(TIMESLEEP)

def SensorBLE_Report():
    uart_server.write("{}\n {},{}\n".format("BerrySeven MCU", "soil temp: C " + str(soil_temp), " soil moist: " + str(soil_moist)))
    uart_server.write("{},{}\n".format("air temp: C " + str(board_temp), " air pressure: hPa " + str(board_press)))
    uart_server.write("{}\n".format("altitude: m " + str(board_altd)))
    #uart_server.write("{}\n".format("air humidity: " + str(board_humidity)))

    # blink BLE Radio neopixel pattern
    NeoPixelPattern(BLUE)
    time.sleep(TIMESLEEP)

# Microcontroller Task Loop

while True:

    # When not connected via BLERadio
    ble.start_advertising(advertisement)
    while not ble.connected:
        # share sensor data via serial
        SensorSerial_Report()
    ble.stop_advertising()

    # When connected via BLERadio
    while ble.connected:
        # share sensor data via BLEradio
        SensorBLE_Report()
