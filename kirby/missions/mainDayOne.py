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
    kirby.drive.straightTime(500, -40)
    kirby.hub.imu.reset_heading(0)
    kirby.drive.straightDistance(800, 90)
    """ while True:
        print(kirby.hub.imu.heading()) """
    
def initialize():
    kirby.hub.imu.reset_heading(-90) #0
    print(kirby.hub.battery.voltage(), "mv")

def startToRover():
    kirby.drive.straightTime(350, -45)
    kirby.hub.imu.reset_heading(0) #choca y resetea imu

    kirby.drive.turnToAngle(-33, power=85, oneWheel="right", safeExitTime=700)
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
    kirby.drive.straightDistance(425, 75)
    kirby.drive.turnToAngle(-180, power=35)

    #kirby.drive.brake(500)

    #kirby.mechanisms.moveBackMotorDegrees(170, 400) #test
    #kirby.drive.brake(500) #test

    kirby.drive.straightTime(600, 35, targetAngle=-180)
    #kirby.drive.brake(400)

    kirby.mechanisms.moveBackMotorDegrees(100, 200)
    kirby.drive.brake(100)
    kirby.mechanisms.moveBackMotorTime(400, -300)
    kirby.drive.brake(300)

def waterSample():
    kirby.drive.straightDistance(-100, 80, targetAngle=-180)
    kirby.drive.turnToAngle(160)
    kirby.drive.straightDistance(-90, 70)
    kirby.drive.turnToAngle(180)
    kirby.drive.straightDistance(-550, 80)

    #kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 500)
    kirby.drive.turnToAngle(-88, power=90, oneWheel="right", safeExitTime=1500)
    #kirby.drive.turnToAngle(-90, power=80, safeExitTime=400)
    kirby.mechanisms.moveBackMotorDegrees(0, 700)
    kirby.drive.straightTime(600, 50)
    kirby.hub.imu.reset_heading(-90) #choca y resetea imu

def scoreSampleAndDrone():
    global samplesPositions
    """ kirby.drive.turnToAngle(-90, oneWheel="right")
    kirby.mechanisms.moveBackMotorDegrees(0, 500)
    kirby.drive.straightTime(600, 40) """
    samplesPositions = kirby.drive.driveAndScan(-750, 60)
    print(samplesPositions)
    kirby.drive.turnToAngle(0, power=85, oneWheel="right", safeExitTime=1000)
    kirby.drive.straightDistance(-820, 90)

    kirby.drive.straightDistance(950, 90)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightTime(800, -40)
    kirby.hub.imu.reset_heading(-90)

def grabLeftSample():
    kirby.drive.turnToAngle(-180, power=60)
    kirby.mechanisms.moveBackMotorDegrees(170, 400)
    kirby.drive.straightDistance(50, 40)
    kirby.mechanisms.moveBackMotorDegrees(120, 300)
    kirby.drive.straightDistance(-70, 40)
    kirby.drive.turnToAngle(-90, power=50)

def grabRightSample():
    kirby.drive.turnToAngle(-180, power=60)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200)
    kirby.drive.straightDistance(50, 40)
    kirby.mechanisms.moveFrontMotorDegrees(60, 300)
    kirby.drive.straightDistance(-70, 40)
    kirby.drive.turnToAngle(-90, power=50)
    
def whiteGreenSamples():
    samplesPositions.reverse()
    wP = samplesPositions.index("white")
    gP = samplesPositions.index("green")

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
    kirby.drive.straightDistance(distanceToLast, distanceToLast * 0.15) if distanceToLast != 0 else kirby.drive.brake(1)

def scoreWhiteGreenSamples():
    kirby.drive.turnToAngle(0, power=50)
    kirby.drive.straightDistance(340, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 150, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(105, 150, wait=False)

    kirby.drive.trackLineDistance(200, 40, side="left")
    kirby.drive.straightDistance(80, 40)

    kirby.drive.straightDistance(-300, 60)