#!/usr/bin/python3

# This example drives the right and left motors.
# Intended for Beaglebone Blue hardware.
# This example uses rcpy library. Documentation: guitar.ucsd.edu/rcpy/rcpy.pdf

# from adafruit_platformdetect import Detector
# detector = Detector()
# if detector.board.BEAGLEBONE_BLUE:

# Import external libraries
import rcpy
import rcpy.motor as motor

class Motor:

    def __init__(self, channel, invert=False):

        self.channel = channel
        self.duty = 0                                   # Initial Duty
        self.invert = invert                            # Reverse motor direction? Duty of 1 becomes -1 and duty of -1 becomes 1

        rcpy.set_state(rcpy.RUNNING)
        motor.set(self.channel, self.duty)

    def setDuty(self, duty):
        if rcpy.get_state() == rcpy.RUNNING:            # Execute loop if rcpy is running
            if not self.invert:
                self.duty = duty
            else:
                self.duty = -1 * duty                   # Invert duty cycle

            motor.set(self.channel, self.duty)


if __name__ == "__main__":

    import time

    l_motor = Motor(1) 	                                # Create Left Motor Object (ch1)
    r_motor = Motor(2) 	                                # Create Right Motor Object (ch2)

    while True:
        print("motors.py: driving fwd")
        l_motor.setDuty(1)                         # Set left motor duty cycle to 0.7
        r_motor.setDuty(1)                          # Set right motor duty cycle to 0.7
        time.sleep(5)                              # Wait 5 seconds
        print("motors.py: driving reverse")
        l_motor.setDuty(-1)                          # Set left motor duty cycle to -0.7
        r_motor.setDuty(-1)                         # Set right motor duty cycle to -0.7
        time.sleep(5)                              # Wait 5 seconds
