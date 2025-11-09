# mainDayOne.py
# 11/02/25 - chaBots Kirby
# Alfonso De Anda

# Routine for robot run on first day challenge

from robot import Robot
from utils.constants import *

kirby = Robot()

samplesPositions = []

# for tests only
def testMission():
    kirby.drive.straightDistance(100, 50)
"""     print(kirby.hub.battery.voltage(), "mv")
    while True:
        print(kirby.front_motor.angle()) """
    
def initialize():
    kirby.hub.imu.reset_heading(-90) #0
    print(kirby.hub.battery.voltage(), "mv")

def startToRover():
    kirby.drive.straightTime(350, -45)
    kirby.hub.imu.reset_heading(0) #choca y resetea imu

    kirby.drive.turnToAngle(-32, oneWheel="right")
    kirby.drive.straightDistance(400, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(60, 30) #align

    kirby.mechanisms.moveBackMotorDegrees(40, 300) #up for drone
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(25, 30)
    kirby.mechanisms.moveBackMotorDegrees(0, 500)

def grabWater():
    kirby.drive.straightDistance(-190, 80, targetAngle=0)
    kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 400)

    kirby.drive.straightTime(400, -70, targetAngle=0)
    kirby.drive.straightDistance(25, 60, targetAngle=0) #primer pelota
    kirby.drive.brake(100)
    kirby.drive.straightTime(500, -70, targetAngle=0)
    kirby.drive.straightDistance(80, 50, targetAngle=0) #segunda pelota
    
    kirby.mechanisms.moveBackMotorDegrees(170, 300)

def scoreWater():
    kirby.drive.turnToAngle(-90, power=40)
    kirby.drive.straightDistance(420, 75)
    kirby.drive.turnToAngle(-180, power=35)

    #kirby.drive.brake(500)

    #kirby.mechanisms.moveBackMotorDegrees(170, 400) #test
    #kirby.drive.brake(500) #test

    kirby.drive.straightTime(600, 35, targetAngle=-180)
    #kirby.drive.brake(400)

    kirby.mechanisms.moveBackMotorDegrees(100, 200)
    kirby.mechanisms.moveBackMotorTime(400, -300)
    kirby.drive.brake(300)

def waterSample():
    kirby.drive.straightDistance(-100, 80)
    kirby.drive.turnToAngle(160)
    kirby.drive.straightDistance(-160, 80)
    kirby.drive.turnToAngle(180)
    kirby.drive.straightDistance(-460, 80)
    #kirby.drive.straightUntilReflection(kReflectionWhite, -20)

    kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 500)
    kirby.drive.turnToAngle(-100, oneWheel="right")
    kirby.drive.turnToAngle(-90)
    kirby.mechanisms.moveBackMotorDegrees(0, 700)
    kirby.drive.straightTime(600, 50)
    kirby.hub.imu.reset_heading(-90) #choca y resetea imu

def scoreSampleAndDrone():
    """ kirby.drive.turnToAngle(-90, oneWheel="right")
    kirby.mechanisms.moveBackMotorDegrees(0, 500)
    kirby.drive.straightTime(600, 40) """
    samplesPositions = kirby.drive.driveAndScan(-750, 60)
    kirby.drive.turnToAngle(0, oneWheel="right")
    kirby.drive.straightDistance(-840, 90)
    #kirby.drive.turnToAngle(20)

    kirby.drive.straightDistance(900, 80)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightTime(500, -40)

def grabLeftSample():
    kirby.drive.turnToAngle(-180, power=60)
    kirby.mechanisms.moveBackMotorDegrees(170, 400)
    kirby.drive.straightDistance(50, 40)
    kirby.mechanisms.moveBackMotorDegrees(120, 300)
    kirby.drive.straightDistance(-70, 40)
    kirby.drive.turnToAngle(-90, power=55)

def grabRightSample():
    kirby.drive.turnToAngle(-180, power=60)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200)
    kirby.drive.straightDistance(50, 40)
    kirby.mechanisms.moveFrontMotorDegrees(60, 300)
    kirby.drive.straightDistance(-70, 40)
    kirby.drive.turnToAngle(-90, power=55)
    
def whiteGreenSamples():
    samplesPositions.reverse()
    wP = 3 #samplesPositions.index("white")
    gP = 0 #samplesPositions.index("green")

    closestPosition = min(wP, gP)

    wallToFirstSample = kDistanceWallToWhiteSample if closestPosition == wP else kDistanceWallToGreenSample

    wallToClosestSample = wallToFirstSample + (kDistanceBetweenSamples * closestPosition)
    kirby.drive.straightDistance(wallToClosestSample, 60)
    grabLeftSample() if closestPosition == wP else grabRightSample()
    distanceDiffBetweenSamples = -160 if closestPosition == wP else 160
    distanceToNextSample = kDistanceBetweenSamples * abs(wP - gP) + distanceDiffBetweenSamples
    powerForSecondSample = abs(distanceToNextSample * 0.15) if distanceToNextSample > 30 else 30
    kirby.drive.straightDistance(distanceToNextSample, powerForSecondSample)
    grabRightSample() if closestPosition == wP else grabLeftSample()
    distanceToLast = kDistanceBetweenSamples * (5 - gP) + 160 if closestPosition == wP else kDistanceBetweenSamples * (5 - wP)
    kirby.drive.straightDistance(distanceToLast, distanceToLast * 0.15)

def scoreWhiteGreenSamples():
    kirby.drive.turnToAngle(0, power=65)
    kirby.drive.straightDistance(350, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(185, 200, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(105, 200, wait=False)

    kirby.drive.trackLineDistance(200, 40, side="left")
    kirby.drive.straightDistance(80, 40)

    kirby.drive.straightDistance(-300, 60)