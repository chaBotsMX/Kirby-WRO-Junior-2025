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

    kirby.drive.straightDistance(35, 40)
    kirby.drive.turnToAngle(-35, safeExitTime=700)
    #kirby.drive.turnToAngle(-33, power=85, oneWheel="right", safeExitTime=700)
    kirby.drive.straightDistance(400, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(60, 30) #align

    kirby.mechanisms.moveBackMotorDegrees(40, 300) #up for drone
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(35, 30)
    #kirby.mechanisms.moveBackMotorDegrees(0, 500)
    kirby.mechanisms.moveBackMotorTime(500, -350)

def grabWater():
    kirby.drive.straightDistance(-200, 80, targetAngle=0)
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

    kirby.drive.straightTime(700, 35, targetAngle=-180)
    #kirby.drive.brake(400)

    kirby.mechanisms.moveBackMotorDegrees(100, 180)
    kirby.drive.brake(200)
    kirby.mechanisms.moveBackMotorTime(400, -330)
    kirby.drive.brake(300)

def waterSample():
    kirby.drive.straightDistance(-50, 80, targetAngle=-180)
    kirby.drive.turnToAngle(-20)
    kirby.drive.straightDistance(80, 60)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(350, 80, targetAngle=0)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(115, 45)

    kirby.drive.turnToAngle(90, power=95, oneWheel="left", safeExitTime=1500)
    kirby.drive.straightTime(600, -50)
    kirby.hub.imu.reset_heading(90) #choca y resetea imu

def scoreSampleAndDrone():
    global samplesPositions
    samplesPositions = kirby.drive.driveAndScan(950, 60)
    print(samplesPositions)
    kirby.drive.turnToAngle(180, power=90, oneWheel="left", safeExitTime=800)
    kirby.drive.straightDistance(820, 90, targetAngle=180)

    kirby.drive.straightDistance(-960, 90, targetAngle=180)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightDistance(-100, 60)
    kirby.drive.straightTime(400, -40)
    kirby.hub.imu.reset_heading(-90)

def grabLeftSample(isCurrentWhiteGreen = True):
    direction = 1 if isCurrentWhiteGreen else -1
    kirby.drive.turnToAngle(-180 * direction, power=50)
    kirby.mechanisms.moveBackMotorDegrees(170, 400)
    kirby.drive.straightDistance(40, 40, targetAngle= -180 * direction)
    kirby.mechanisms.moveBackMotorDegrees(120, 300)
    kirby.drive.straightDistance(-65, 40)
    kirby.drive.turnToAngle(-90 * direction, power=45)

def grabRightSample(isCurrentWhiteGreen = True):
    direction = 1 if isCurrentWhiteGreen else -1
    kirby.drive.turnToAngle(-180 * direction, power=50)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200)
    kirby.drive.straightDistance(40, 40, targetAngle= -180 * direction)
    kirby.mechanisms.moveFrontMotorDegrees(60, 300)
    kirby.drive.straightDistance(-65, 40)
    kirby.drive.turnToAngle(-90 * direction, power=45)
    
def whiteGreenSamples():
    samplesPositions.reverse()
    wP = samplesPositions.index("white")
    gP = samplesPositions.index("green")

    closestPosition = min(wP, gP)

    wallToFirstSample = kDistanceWallToWhiteSample if closestPosition == wP else kDistanceWallToGreenSample #it varies if the closest sample is white or green

    wallToClosestSample = wallToFirstSample + (kDistanceBetweenSamples * closestPosition) #distance calculation for closest sample
    kirby.drive.straightDistance(wallToClosestSample, 60)
    grabLeftSample() if closestPosition == wP else grabRightSample() #grab correct sample

    distanceDiffBetweenSamples = -160 if closestPosition == wP else 160 #for difference in distance
    distanceToNextSample = kDistanceBetweenSamples * abs(wP - gP) + distanceDiffBetweenSamples
    powerForSecondSample = abs(distanceToNextSample * 0.2) if distanceToNextSample > 30 else 30
    if powerForSecondSample > 85: powerForSecondSample = 85 #clamp
    kirby.drive.straightDistance(distanceToNextSample, powerForSecondSample)
    grabRightSample() if closestPosition == wP else grabLeftSample()

    distanceToLast = kDistanceBetweenSamples * (5 - gP) + 160 if closestPosition == wP else kDistanceBetweenSamples * (5 - wP) #go to the end
    powerForLast = distanceToLast * 0.22
    if powerForLast > 65: powerForLast = 65
    kirby.drive.straightDistance(distanceToLast, powerForLast) if distanceToLast != 0 else kirby.drive.brake(1) #if robot already in the end dont drive

def scoreWhiteGreenSamples():
    kirby.drive.turnToAngle(0, power=50, safeExitTime=600)
    kirby.drive.straightDistance(340, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 150, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(105, 150, wait=False)

    kirby.drive.trackLineDistance(200, 40, side="left")
    if kirby.hub.imu.heading() < -7 and kirby.hub.imu.heading() > 7:
        kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(80, 40)

def yellowRedSamlpes():
    kirby.drive.straightDistance(-720, 80)
    kirby.mechanisms.moveBackMotorDegrees(0, 400, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(0, 400, wait=False)
    kirby.drive.turnToAngle(90)
    kirby.drive.straightTime(800, -40)
    kirby.hub.imu.reset_heading(90)

    samplesPositions.reverse()
    yP = samplesPositions.index("yellow")
    rP = samplesPositions.index("red")

    closestPosition = min(yP, rP)

    wallToFirstSample = kDistanceWallToYellowSample if closestPosition == yP else kDistanceWallToRedSample #it varies if the closest sample is white or green

    wallToClosestSample = wallToFirstSample + (kDistanceBetweenSamples * closestPosition) #distance calculation for closest sample
    kirby.drive.straightDistance(wallToClosestSample, 60)
    grabLeftSample(isCurrentWhiteGreen=False) if closestPosition == yP else grabRightSample(isCurrentWhiteGreen=False) #grab correct sample

    distanceDiffBetweenSamples = 160 if closestPosition == yP else -165 #for difference in distance
    distanceToNextSample = kDistanceBetweenSamples * abs(yP - rP) + distanceDiffBetweenSamples
    powerForSecondSample = abs(distanceToNextSample * 0.2) if distanceToNextSample > 30 else 25
    if powerForSecondSample > 85: powerForSecondSample = 85 #clamp
    kirby.drive.straightDistance(distanceToNextSample, powerForSecondSample)
    grabRightSample(isCurrentWhiteGreen=False) if closestPosition == yP else grabLeftSample(isCurrentWhiteGreen=False)

    distanceToLast = kDistanceBetweenSamples * (5 - rP) if closestPosition == yP else kDistanceBetweenSamples * (5 - yP) + 160 #go to the end
    powerForLast = distanceToLast * 0.22 if distanceToLast > 30 else 30
    if powerForLast > 80: powerForLast = 80
    kirby.drive.straightDistance(distanceToLast + 60, powerForLast) if distanceToLast != 0 else kirby.drive.brake(1) #if robot already in the end dont drive

def scoreYellowRedSamples():
    kirby.drive.turnToAngle(0, power=50)
    kirby.drive.straightDistance(300, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 150, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(95, 150, wait=False)

    kirby.drive.trackLineDistance(200, 40, side="left")
    kirby.drive.straightDistance(85, 40)

def park():
    kirby.drive.straightDistance(-450, 80)
    kirby.mechanisms.moveBackMotorDegrees(0, 300, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(0, 300, wait=False)
    kirby.drive.turnToAngle(90)
    print(kirby.hub.imu.heading())
    kirby.drive.straightDistance(-375, 50, targetAngle=90)
    #kirby.drive.turnToAngle(180, power=90, oneWheel="right", safeExitTime=1000)
    kirby.drive.turnToAngle(180, safeExitTime=800)
    print(kirby.hub.imu.heading())
    kirby.drive.straightDistance(-600, 90, targetAngle=180)