#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from machine import Pin
import time


def show_row(row_number, columns, delay):
    # Control a row of the dot matrix display
    # YOUR CODE GOES HERE:
    pass     # Remove this line when implementing


def main():
    global row_pins, col_pins
    # define row and column pin numbers
    row_pin_numbers = [7, 11, 6, 9, 0, 5, 1]
    col_pin_numbers = [10, 2, 3, 8, 4]

    row_pins = []
    col_pins = []

    # set all the pins as outputs and set row pins high, column pins low
    for row_number in row_pin_numbers:
        row_pins.append(Pin(row_number, Pin.OUT, value = 1))

    for col_number in col_pin_numbers:
        col_pins.append(Pin(col_number, Pin.OUT, value = 0))

    # Sets the waiting time between rows
    wait_time = 0.05

    # Displays image 50 times
    i = 0
    while i < 50:
        col_pins[2].value(1)
        row_pins[3].value(0)

        time.sleep(wait_time)

        col_pins[2].value(0)
        row_pins[3].value(1)

        col_pins[1].value(1)
        col_pins[3].value(1)

        row_pins[4].value(0)

        time.sleep(wait_time)
        
        col_pins[1].value(0)
        col_pins[3].value(0)
        row_pins[4].value(1)
        
        i += 1


if __name__ == "__main__":
    main()
