#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from machine import Pin
import time

def show_row(row_number, columns, delay):
    global row_pins, col_pins

    

    #to turn off all the row and columns

    for row in row_pins:
        row.value(1)
    for col in col_pins:
        col.value(1)

    row_pins[row_number -1].value(0) #to set the specific row to low

    

    for col in range(5):
        if col in columns:
            col_pins[col].value(0)
        else:
            col_pins[col].value(1)
    time.sleep(delay)

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
        col_pins.append(Pin(col_number, Pin.OUT, value = 1))
    

    while True: 

        show_row(2, [1, 3, 5], 2)


if __name__ == "__main__":

    main()
