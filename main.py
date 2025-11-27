# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/micropython-i2c-lcd-esp32-esp8266/

from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from time import sleep, sleep_ms
import dht

# Initialize DHT sensor
sensor = dht.DHT22(Pin(15))

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("Hello DHT")
sleep(4)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        lcd.clear()
        sleep_ms(200)
        lcd.putstr("Temp: {:.1f} C".format(temp))
        lcd.move_to(0, 1)
        lcd.putstr("Humidity: {:.1f}%".format(hum))

        print("Temperature:", temp, "C")
        print("Humidity:", hum, "%")

    except Exception as e:
        print("Sensor error:", e)
    
    sleep(2)