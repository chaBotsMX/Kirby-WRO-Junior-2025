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
    #kirby.drive.turnToAngle(90)
    while True:
        print(kirby.hub.imu.heading())
    
def initialize():
    kirby.hub.imu.reset_heading(0) #0
    print(kirby.hub.battery.voltage(), "mv")

def startToRover():
    kirby.drive.straightTime(400, -60)
    kirby.hub.imu.reset_heading(0) #choca y resetea imu

    kirby.drive.straightDistance(35, 40)
    kirby.drive.turnToAngle(-35, safeExitTime=700)
    kirby.drive.straightDistance(400, 90)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(60, 30) #align

    kirby.mechanisms.moveBackMotorDegrees(40, 300, wait=False) #up for drone
    kirby.drive.turnToAngle(0, safeExitTime=700)
    kirby.drive.straightDistance(35, 40, accel=False)
    kirby.mechanisms.moveBackMotorTime(500, -350)

def grabWater():
    kirby.drive.straightDistance(-200, 95, targetAngle=0)
    kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 400)

    kirby.drive.straightTime(400, -70, targetAngle=0)
    kirby.drive.straightDistance(25, 60, targetAngle=0) #primer pelota
    kirby.drive.brake(100)
    kirby.drive.straightTime(500, -70, targetAngle=0)
    kirby.drive.straightDistance(80, 50, targetAngle=0) #segunda pelota
    
    kirby.mechanisms.moveBackMotorDegrees(170, 300, wait=False)

def scoreWater():
    kirby.drive.turnToAngle(-90, power=40)
    kirby.drive.straightDistance(420, 75)
    kirby.drive.turnToAngle(-180, power=35)

    kirby.drive.straightTime(700, 35, targetAngle=-180)

    kirby.mechanisms.moveBackMotorDegrees(100, 180)
    kirby.drive.brake(200)
    kirby.mechanisms.moveBackMotorTime(400, -330)
    kirby.drive.brake(100)

def waterSample():
    kirby.drive.straightDistance(-50, 90, targetAngle=-180)
    kirby.drive.turnToAngle(-20)
    kirby.drive.straightDistance(80, 70)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(350, 95, targetAngle=0)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(115, 60)

    kirby.drive.turnToAngle(90, power=95, oneWheel="left", safeExitTime=1500)
    kirby.drive.straightTime(600, -60)
    kirby.hub.imu.reset_heading(90) #choca y resetea imu

def scoreSampleAndDrone():
    global samplesPositions
    samplesPositions = kirby.drive.driveAndScan(950, 80)
    print(samplesPositions)
    kirby.drive.turnToAngle(180, power=95, oneWheel="left", safeExitTime=800)
    kirby.drive.straightDistance(820, 96, targetAngle=180)

    kirby.drive.straightDistance(-940, 96, targetAngle=180)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightTime(600, -70)
    kirby.hub.imu.reset_heading(-90)

def grabLeftSample(isCurrentWhiteGreen = True):
    direction = 1 if isCurrentWhiteGreen else -1
    kirby.drive.turnToAngle(-180 * direction, power=90)
    kirby.mechanisms.moveBackMotorDegrees(170, 500)
    kirby.drive.straightDistance(40, 40, targetAngle= -180 * direction)
    kirby.mechanisms.moveBackMotorDegrees(80, 300)
    kirby.drive.straightDistance(-65, 60)
    kirby.drive.turnToAngle(-90 * direction, power=90)

def grabRightSample(isCurrentWhiteGreen = True):
    direction = 1 if isCurrentWhiteGreen else -1
    kirby.drive.turnToAngle(-180 * direction, power=90)
    kirby.mechanisms.moveFrontMotorDegrees(95, 400)
    kirby.drive.straightDistance(40, 40, targetAngle= -180 * direction)
    kirby.mechanisms.moveFrontMotorDegrees(50, 300)
    kirby.drive.straightDistance(-65, 60)
    kirby.drive.turnToAngle(-90 * direction, power=90)
    
def whiteGreenSamples():
    samplesPositions.reverse()
    wP = samplesPositions.index("white")
    gP = samplesPositions.index("green")

    closestPosition = min(wP, gP)

    wallToFirstSample = kDistanceWallToWhiteSample if closestPosition == wP else kDistanceWallToGreenSample #it varies if the closest sample is white or green

    wallToClosestSample = wallToFirstSample + (kDistanceBetweenSamples * closestPosition) #distance calculation for closest sample
    kirby.drive.straightDistance(wallToClosestSample, 80, ratio=0.4)
    grabLeftSample() if closestPosition == wP else grabRightSample() #grab correct sample

    distanceDiffBetweenSamples = -160 if closestPosition == wP else 160 #for difference in distance
    distanceToNextSample = kDistanceBetweenSamples * abs(wP - gP) + distanceDiffBetweenSamples
    powerForSecondSample = abs(distanceToNextSample * 0.21) if distanceToNextSample > 30 else 40
    if powerForSecondSample > 85: powerForSecondSample = 85 #clamp
    kirby.drive.straightDistance(distanceToNextSample, powerForSecondSample, ratio=0.4)
    grabRightSample() if closestPosition == wP else grabLeftSample()

    distanceToLast = kDistanceBetweenSamples * (5 - gP) + 150 if closestPosition == wP else kDistanceBetweenSamples * (5 - wP) #go to the end
    powerForLast = distanceToLast * 0.22 if distanceToLast > 100 else 40
    if powerForLast > 80: powerForLast = 80
    kirby.drive.straightDistance(distanceToLast, powerForLast, ratio=0.4) if distanceToLast != 0 else kirby.drive.brake(1) #if robot already in the end dont drive

def scoreWhiteGreenSamples():
    kirby.drive.turnToAngle(0, power=90, safeExitTime=500) #50
    kirby.drive.straightDistance(340, 90)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 200, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(105, 200, wait=False)

    kirby.drive.trackLineDistance(200, 50, side="left")
    if kirby.hub.imu.heading() < -7 and kirby.hub.imu.heading() > 7:
        kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(80, 40)

def yellowRedSamlpes():
    kirby.drive.straightDistance(-710, 95)
    kirby.mechanisms.moveBackMotorDegrees(0, 500, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(0, 400, wait=False)
    kirby.drive.turnToAngle(90)
    kirby.drive.straightTime(700, -60)
    kirby.hub.imu.reset_heading(90)

    samplesPositions.reverse()
    yP = samplesPositions.index("yellow")
    rP = samplesPositions.index("red")

    closestPosition = min(yP, rP)

    wallToFirstSample = kDistanceWallToYellowSample if closestPosition == yP else kDistanceWallToRedSample #it varies if the closest sample is white or green

    wallToClosestSample = wallToFirstSample + (kDistanceBetweenSamples * closestPosition) #distance calculation for closest sample
    kirby.drive.straightDistance(wallToClosestSample, 80, ratio=0.4)
    grabLeftSample(isCurrentWhiteGreen=False) if closestPosition == yP else grabRightSample(isCurrentWhiteGreen=False) #grab correct sample

    distanceDiffBetweenSamples = 160 if closestPosition == yP else -165 #for difference in distance
    distanceToNextSample = kDistanceBetweenSamples * abs(yP - rP) + distanceDiffBetweenSamples
    powerForSecondSample = abs(distanceToNextSample * 0.21) if distanceToNextSample > 30 else 25
    if powerForSecondSample > 85: powerForSecondSample = 85 #clamp
    kirby.drive.straightDistance(distanceToNextSample, powerForSecondSample)
    grabRightSample(isCurrentWhiteGreen=False) if closestPosition == yP else grabLeftSample(isCurrentWhiteGreen=False)

    distanceToLast = kDistanceBetweenSamples * (5 - rP) + 60 if closestPosition == yP else kDistanceBetweenSamples * (5 - yP) + 160 + 60 #go to the end
    powerForLast = distanceToLast * 0.22 if distanceToLast > 60 else 30
    if powerForLast > 80: powerForLast = 80
    kirby.drive.straightDistance(distanceToLast, powerForLast) if distanceToLast != 0 else kirby.drive.brake(1) #if robot already in the end dont drive

def scoreYellowRedSamples():
    kirby.drive.turnToAngle(0, power=90)
    kirby.drive.straightDistance(300, 90)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 200, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200, wait=False)

    kirby.drive.trackLineDistance(200, 50, side="left")
    kirby.drive.straightDistance(85, 50)

def park():
    kirby.drive.straightDistance(-450, 90)
    kirby.mechanisms.moveBackMotorDegrees(0, 300, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(0, 300, wait=False)
    kirby.drive.turnToAngle(92)
    print(kirby.hub.imu.heading())
    kirby.drive.straightDistance(-380, 50, targetAngle=90)
    #kirby.drive.turnToAngle(180, power=90, oneWheel="right", safeExitTime=1000)
    kirby.drive.turnToAngle(-176)
    print(kirby.hub.imu.heading())
    kirby.drive.straightDistance(-750, 90)