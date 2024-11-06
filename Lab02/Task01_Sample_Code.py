#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from machine import Pin
import time

# Defining row pins for ease of use.
# You should enter the GPIO numbers that you connected your display to.
pin_numbers = [0]
pins = []

def init():
    global pins

    # This loop will create a list of machine Pin objects and set them to value 1
    for pin_number in pin_numbers:
        pin = Pin(pin_number, Pin.OUT)
        pins.append(pin)
        pin.value(1) # Turn off LED

def main():
    init()
    
    while True:
        # Write the code here to control the row pins in the desired way.
        pass


if __name__ == "__main__":
    main()
