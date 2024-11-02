from machine import Pin
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import time
import machine
import math
#from lab_task05
# Initialisation of LCD with correct parameters
lcd_columns = 16
lcd_rows = 2
    
# Replace x with the pin number, board.GPx in CircuitPython is the same as machine.Pin(x) in MicroPython
scl_pin = board.GP5
sda_pin = board.GP4
    
i2c = busio.I2C(scl_pin, sda_pin)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.color = [2, 0, 0]   #(Correction) (0-1 translate to 0% and 2-100 means 100%)
#from lab_task06
echo_pin = 0
trig_pin = 1
delay_us = 10
    
trigger = Pin(trig_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)
    
def get_ultrasonic_reading(timeout=100, default_value=0):

    measurement_start_time = time.ticks_ms()
    trigger.low()
    time.sleep_us(2)
    while echo.value() != 0:
        if time.ticks_diff(time.ticks_ms(), measurement_start_time) > timeout:
            return default_value # Return if timeout occurs
    # Generate the trigger impulse
    trigger.high()

    time.sleep_us(delay_us)

    trigger.low()
    while echo.value() == 0:

        if time.ticks_diff(time.ticks_ms(), measurement_start_time) > timeout:

            return default_value

    signal_rise = time.ticks_us()

    # Wait for the echo pin to go back low

    while echo.value() == 1:

        if time.ticks_diff(time.ticks_ms(), measurement_start_time) > timeout:

            return default_value

    signal_fall = time.ticks_us()

    # Calculate the time difference

    duration_us = signal_fall - signal_rise

    return duration_us

def get_distance_in_mm(duration_us):

    distance_from_object_in_mm = ((343) * ((duration_us)/1000))/2 

    return distance_from_object_in_mm

def main():

    while True:
        duration_us = get_ultrasonic_reading()
        
        
        if duration_us != 0:
            dist_mm = get_distance_in_mm(duration_us)
            #(correction) we added some spaces to overwrite 
            lcd.message = "US measurment\n{}mm   " .format(int(dist_mm))
            
        else:
            lcd.clear()
            lcd.message = "US measurement \nOut of range"
            
        time.sleep(0.5)
if __name__ == "__main__":
    main()

