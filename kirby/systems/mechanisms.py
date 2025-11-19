# mechanisms.py
# 08/02/25 - chaBots Kirby
# Alfonso De Anda

# Methods to control robot's mechanisms

from pybricks.parameters import Stop

class MechanismsSystem:
    def __init__(self, front_motor, back_motor):
        self.front = front_motor
        #self.front.reset_angle(0)

        self.back = back_motor
        self.back.reset_angle(0)

    def moveBackMotorDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.back.run_target(speed, degrees, then, wait)

    def moveBackMotorTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.back.run_time(speed, time, then, wait)

    def moveFrontMotorDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.front.run_target(speed, degrees, then, wait)

    def moveFrontMotorTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.front.run_time(speed, time, then, wait)