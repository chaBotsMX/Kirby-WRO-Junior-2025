# mainDayOne.py
# 11/02/25 - chaBots Kirby
# Alfonso De Anda

# Routine for robot run on first day challenge

from robot import Robot
from utils.constants import kReflectionBlack, kBackMotorWaterPosition, kReflectionWhite

kirby = Robot()

samplesPositions = []

# for tests only
def testMission():
    print(kirby.hub.battery.voltage(), "mv")
    while True:
        print(kirby.back_motor.angle())
    
def initialize():
    print(kirby.hub.battery.voltage(), "mv")

def startToRover():
    kirby.drive.straightTime(400, -50)
    kirby.hub.imu.reset_heading(0) #choca y resetea imu

    kirby.drive.turnToAngle(-32, oneWheel="right")
    kirby.drive.straightDistance(410, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(60, 30) #align

    kirby.mechanisms.moveBackMotorDegrees(40, 300) #up for drone
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(25, 30)
    kirby.mechanisms.moveBackMotorDegrees(0, 500)

def grabWater():
    kirby.drive.straightDistance(-180, 80, targetAngle=0)
    kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 400)

    kirby.drive.straightTime(400, -70, targetAngle=0)
    kirby.drive.straightDistance(35, 60, targetAngle=0) #primer pelota
    kirby.drive.brake(100)
    kirby.drive.straightTime(500, -70, targetAngle=0)
    kirby.drive.straightDistance(95, 50, targetAngle=0) #segunda pelota
    
    kirby.mechanisms.moveBackMotorDegrees(170, 300)

def scoreWater():
    kirby.drive.turnToAngle(-90, power=40)
    kirby.drive.straightDistance(400, 85)
    kirby.drive.turnToAngle(-180, power=35)
    #kirby.drive.brake(500)
    #kirby.drive.straightDistance(145, 75)
    kirby.drive.straightTime(500, 40)
    kirby.drive.brake(200)

    kirby.mechanisms.moveBackMotorDegrees(75, 200)
    kirby.drive.brake(500)

def waterSample():
    kirby.drive.straightDistance(-100, 80)
    kirby.drive.turnToAngle(160)
    kirby.drive.straightDistance(-170, 80)
    kirby.drive.turnToAngle(180)
    kirby.drive.straightDistance(-460, 80)
    #kirby.drive.straightUntilReflection(kReflectionWhite, -20)

    kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 300)
    kirby.drive.turnToAngle(-90, oneWheel="right")
    kirby.mechanisms.moveBackMotorDegrees(0, 500)
    kirby.drive.straightTime(600, 40)

def scoreSampleAndDrone():
    """ kirby.drive.turnToAngle(-90, oneWheel="right")
    kirby.mechanisms.moveBackMotorDegrees(0, 500)
    kirby.drive.straightTime(600, 40) """
    samplesPositions = kirby.drive.driveAndScan(-840, 60)
    kirby.drive.turnToAngle(0, oneWheel="right")
    kirby.drive.straightDistance(-800, 90)
    kirby.drive.turnToAngle(20)