from robot import Robot
from utils.constants import *

kirby = Robot()

def todoaki():
    kirby.drive.straightDistance(100, 60)
    kirby.mechanisms.moveBackMotorDegrees(90, 300)

    kirby.drive.turnToAngle(90, power=100)