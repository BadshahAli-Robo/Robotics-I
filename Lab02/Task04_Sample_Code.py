#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import machine
import time

from pololu import IMU

# Constants for sensors
SENSITIVITY_baro = 4096 # (LSB/hPa)
SENSITIVITY_accel = ... # (mg/LSB)
SENSITIVITY_gyro = ...  # (mdps/LSB)
SENSITIVITY_mag = ...   # (LSB/gauss)


# Variable for the multi-sensor object
m_sense = None


def init():
    global m_sense
    i2c = machine.I2C(0,
                  scl=machine.Pin(5),
                  sda=machine.Pin(4))
    m_sense = IMU(i2c)
    m_sense.barometer_init(IMU.BAROMETER_FREQ_1HZ)
    time.sleep(1)


def main():
    init()
    
    while True:
        baro_raw = m_sense.barometer_raw_data()
        baro = baro_raw / SENSITIVITY_baro
        print(f"B: {baro:.2f}")
        time.sleep(1)


if __name__ == "__main__":
    main()
