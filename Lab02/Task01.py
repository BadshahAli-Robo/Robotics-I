#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from machine import Pin

import time

# Defining row pins for ease of use.

# You should enter the GPIO numbers that you connected your display to.

pin_numbers = [0, 1, 2, 3, 4, 5, 6]

pins = []


def init():

    global pins

    # This loop will create a list of machine Pin objects and set them to value 1

    for pin_number in pin_numbers:

        pin = Pin(pin_number, Pin.OUT)

        pins.append(pin)

        pin.value(1) # 0=on / 1=off

def main():

    init()
    #define the order of rows to avoid too much copy paste and lengthy code
    row_order = [1, 2, 0, 5, 3, 6, 4]      #pin arrangement
    current_row = 0
    direction = 1 # (+/-) is for forward/backward direction
    

    while True:
        pins[row_order[current_row]].value(0)
        time.sleep(0.1)
        pins[row_order[current_row]].value(1)
        current_row += direction
        
        if current_row == 0:
            direction = 1
#         if current_row == 1:
#             direction = -1
        elif current_row == len(row_order) - 1:
            direction = -1
        
        
        

if __name__ == "__main__":

    main()
    
    
    
    
    
    
    
    
# FOR ME

#     for row in row_order:
#             pins[row].value(0)
#             time.sleep(0.1)
#             pins[row].value(1)
#         for row in reversed(row_order):
#             pins[row].value(0)
#             time.sleep(0.1)
#             pins[row].value(1)