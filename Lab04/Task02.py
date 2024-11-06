#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import easygopigo3 as go
import time


def main():
    myRobot = go.EasyGoPiGo3()

    myRobot.set_speed(500)
    myRobot.forward()
    time.sleep(1)
    myRobot.right()
    time.sleep(0.5)
    myRobot.backward()
    time.sleep(1)
    myRobot.stop()
    myRobot.orbit(90, 5)
    myRobot.orbit(-90, 5)
    myRobot.stop()


if __name__ == "__main__":
    main()
