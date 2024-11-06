#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from machine import Pin, PWM, ADC
import time
import sys
import select


def handle_input(servo, in_value):
    """
    Arguments:
        servo           -- PWM, servo object
        in_value        -- int, input from Shell
    
    Returns:
        nothing
    """
    pass


def calculate_rpm(als, low_thresh, high_thresh):
    """
    Arguments:
        als              -- float, light intensity as a percentage
        low_thresh       -- int, lower threshold for RPM calculation
        high_thresh      -- int, upper threshold for RPM calculation
    
    Returns:
        nothing    
    """
    pass


def main():
    servo = ... # Initialise servo connection here
    #servo.freq(50) # Uncomment this
    
    als = ... # Initialise ALS connection here
    low_thresh = ... # Choose a suitable value
    high_thresh = ... # Choose a suitable value
    
    while True:
        data_in = select.select([sys.stdin], [], [], 0)[0]
        als_raw = als.read_u16()
        als_value = round(als_raw/65535*100, 2) #map value from 0-65535 to range 0-100 for easier human readibility
        if not data_in:
            calculate_rpm(als_value, low_thresh, high_thresh)
        else:
            line = data_in[0].readline()
            if line.rstrip():
                handle_input(servo, int(line))


if __name__ == "__main__":
    main()
