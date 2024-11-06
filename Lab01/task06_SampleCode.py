#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from machine import Pin
import time

echo_pin = 0 # < --- YOU HAVE TO ENTER THE GP<x> PIN, YOU HAVE CONNECTED ECHO TO
trig_pin = 0 # < --- YOU HAVE TO ENTER THE GP<x> PIN, YOU HAVE CONNECTED TRIGGER TO

delay_us = 60 # < --- YOU HAVE TO FIND THE MINIMAL VALUE FROM THE TIMING DIAGRAM

"""
Set the following pins to correct modes!
"""
#trigger = Pin(trig_pin, Pin.)
#echo = Pin(echo_pin, Pin.)


def get_ultrasonic_reading(timeout=100, default_value=None):
    measurement_start_time = time.ticks_ms()

    # Ensure that the trigger pin is low when starting a measurement
    trigger.low()
    time.sleep_us(2)

    # Wait for the echo pin to go low
    while echo.value() != 0:
        if time.ticks_diff(time.ticks_ms(), measurement_start_time) > timeout:
            return default_value # Return if timeout occurs

    # Generate the trigger impulse
    trigger.high()
    time.sleep_us(delay_us)
    trigger.low()

    # Wait for the echo pin to go high
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
    """
    YOU HAVE TO CALCULATE THE distance_mm BASED ON THE duration_us.
    """
    distance_from_object_in_mm = "you have to calculate this value!"

    return distance_from_object_in_mm

def main():
    while True:
        duration_us = get_ultrasonic_reading()
        dist_mm = get_distance_in_mm(duration_us)
        print("The distance from object is:", dist_mm, "mm")

        time.sleep(1)

if __name__ == "__main__":
    # Run the main function
    main()
