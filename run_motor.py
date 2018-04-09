#!/usr/bin/env python3
import ev3dev.ev3 as ev3

m = ev3.LargeMotor('outA')
m.run_timed(time_sp=3000, speed_sp=500)
n = ev3.LargeMotor('outB')
n.run_timed(time_sp=3000, speed_sp=-500)
