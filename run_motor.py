#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep


# could use to write to data files later
with open('ouput.txt', 'a') as the_file:
    count = 0
    while count < 5:
        # IR sensor, it turns the left LED from green to red when an object is brought
        # close to the IR sensor, and turns it back to green when no object is close.
        ir = InfraredSensor()

        # Using the assert statement to check that the sensors are attached.
        # If the assertion fails then the program closes with a useful error message (in this case a text message)
        # Assert is a statement and not a function, so it should be used without parentheses as here.
        assert ir.connected, "Connect a single infrared sensor to any sensor port"

        # set the infrared sensor into proximity mode
        ir.mode = 'IR-PROX'
        # Infrared sensor in proximity mode will measure distance to the closest object before it
        distance = ir.value()

        the_file.write("IR proximity: " + distance + "\n")

        m = LargeMotor('outA')
        m.run_timed(time_sp=3000, speed_sp=500)
        n = LargeMotor('outB')
        n.run_timed(time_sp=3000, speed_sp=-500)

        me = MediumMotor('outC')
        me.run_to_rel_pos(position_sp=150, speed_sp=900, stop_action="hold")
        sleep(5)
        me.run_to_rel_pos(position_sp=180, speed_sp=-900, stop_action="hold")

        count += 1



