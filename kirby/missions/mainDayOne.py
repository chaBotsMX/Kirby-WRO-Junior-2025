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
    print(kirby.hub.battery.voltage(), "mv")
    while True:    
        print(kirby.front_motor.angle())
"""     while True:
        print(kirby.line_sensor.reflection()) """
    
def initialize():
    kirby.hub.imu.reset_heading(0) #0
    print(kirby.hub.battery.voltage(), "mv")

def startToRover():
    kirby.drive.straightTime(450, -50)
    kirby.hub.imu.reset_heading(0) #choca y resetea imu

    kirby.drive.straightDistance(35, 40)
    kirby.drive.turnToAngle(-35, safeExitTime=700)
    kirby.drive.straightDistance(380, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(55, 30) #align

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
    kirby.drive.straightDistance(70, 50, targetAngle=0) #segunda pelota
    
    kirby.mechanisms.moveBackMotorDegrees(170, 300, wait=False)

def scoreWater():
    kirby.drive.turnToAngle(-91, power=40)
    kirby.drive.straightDistance(310, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(60, 35)
    kirby.drive.turnToAngle(-180, power=40)

    kirby.drive.straightTime(750, 35, targetAngle=-180)

    kirby.mechanisms.moveBackMotorDegrees(100, 180)
    kirby.drive.brake(200)
    kirby.mechanisms.moveBackMotorTime(400, -330)
    kirby.drive.brake(100)

def waterSample():
    kirby.drive.straightDistance(-50, 90, targetAngle=-180)
    kirby.drive.turnToAngle(-20)
    kirby.drive.straightDistance(120, 60)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(350, 80, targetAngle=0)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(210, 40) #115 + 80 ? !!!!!210
    #kirby.drive.straightDistance(-70, 40)

    """ 
    kirby.drive.straightDistance(-50, 90, targetAngle=-180)

    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(300, 60, ratio=0.4)
    kirby.drive.turnToAngle(-20)
    kirby.drive.straightDistance(80, 70)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(115, 50) #115 + 80 ?
    """

    """     kirby.drive.turnToAngle(-20)
    kirby.drive.straightDistance(80, 70)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(350, 70, targetAngle=0)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(195, 50) #115 + 80 ?
    kirby.drive.straightDistance(-60, 50) """

    #kirby.drive.turnToAngle(90, power=80, oneWheel="left", safeExitTime=1500)
    kirby.drive.turnToAngle(90)
    kirby.drive.straightTime(600, -60)
    kirby.hub.imu.reset_heading(90) #choca y resetea imu

def scoreSampleAndDrone():
    global samplesPositions
    samplesPositions = kirby.drive.driveAndScan(800, 90)
    print(samplesPositions)
    kirby.drive.brake(10)
    kirby.drive.turnToAngle(180, power=80, oneWheel="left", safeExitTime=800)
    kirby.drive.straightDistance(820, 96, targetAngle=180)
    #kirby.drive.leftDegrees(60, 300)
    #kirby.drive.brake(10)
    #kirby.drive.turnToAngle(180, oneWheel="left", safeExitTime=800)

    kirby.drive.straightDistance(-950, 90, targetAngle=180)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightTime(750, -45)
    kirby.hub.imu.reset_heading(-90)

def grabLeftSample(isCurrentWhiteGreen = True):
    direction = 1 if isCurrentWhiteGreen else -1
    kirby.drive.turnToAngle(-180 * direction, power=80)
    kirby.mechanisms.moveBackMotorDegrees(170, 350)
    kirby.drive.straightDistance(55, 40, targetAngle= -180 * direction)
    kirby.mechanisms.moveBackMotorDegrees(80, 200)
    kirby.drive.straightDistance(-65, 60)
    kirby.drive.turnToAngle(-90 * direction, power=70)

def grabRightSample(isCurrentWhiteGreen = True):
    direction = 1 if isCurrentWhiteGreen else -1
    kirby.drive.turnToAngle(-180 * direction, power=80)
    kirby.mechanisms.moveFrontMotorDegrees(93, 300)
    kirby.drive.straightDistance(55, 40, targetAngle= -180 * direction)
    kirby.mechanisms.moveFrontMotorDegrees(50, 150)
    kirby.drive.brake(15)
    kirby.drive.straightDistance(-65, 60)
    kirby.drive.turnToAngle(-90 * direction, power=70)
    
def whiteGreenSamples():
    samplesPositions.reverse()
    wP = samplesPositions.index("white")
    gP = samplesPositions.index("green")

    closestPosition = min(wP, gP)

    wallToFirstSample = kDistanceWallToWhiteSample if closestPosition == wP else kDistanceWallToGreenSample #it varies if the closest sample is white or green

    wallToClosestSample = wallToFirstSample + (kDistanceBetweenSamples * closestPosition) #distance calculation for closest sample
    kirby.drive.straightDistance(wallToClosestSample, 60, ratio=0.4)
    grabLeftSample() if closestPosition == wP else grabRightSample() #grab correct sample

    distanceDiffBetweenSamples = -160 if closestPosition == wP else 155 #for difference in distance
    distanceToNextSample = kDistanceBetweenSamples * abs(wP - gP) + distanceDiffBetweenSamples
    if wP - gP == -1: distanceToNextSample = -145

    powerForSecondSample = abs(distanceToNextSample * 0.21) if distanceToNextSample > 30 else 30
    if powerForSecondSample > 75: powerForSecondSample = 75 #clamp
    
    kirby.drive.straightDistance(distanceToNextSample, powerForSecondSample, ratio=0.4)
    grabRightSample() if closestPosition == wP else grabLeftSample()

    distanceToLast = kDistanceBetweenSamples * (5 - gP) + 195 if closestPosition == wP else kDistanceBetweenSamples * (5 - wP) + 25 #go to the end
    
    powerForLast = distanceToLast * 0.2 if distanceToLast > 100 else 25
    if powerForLast > 80: powerForLast = 80
    
    kirby.drive.straightDistance(distanceToLast, powerForLast, ratio=0.4) if distanceToLast != 0 else kirby.drive.brake(1) #if robot already in the end dont drive

def scoreWhiteGreenSamples():
    kirby.drive.turnToAngle(0, power=70, safeExitTime=600) #50
    kirby.drive.straightDistance(330, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 200, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(100, 200, wait=False)

    kirby.drive.trackLineDistance(200, 50, side="left")
    if kirby.hub.imu.heading() < -7 and kirby.hub.imu.heading() > 7:
        kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(80, 40)

def yellowRedSamlpes():
    kirby.drive.straightDistance(-720, 85)
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
    kirby.drive.straightDistance(wallToClosestSample, 70, ratio=0.4)
    grabLeftSample(isCurrentWhiteGreen=False) if closestPosition == yP else grabRightSample(isCurrentWhiteGreen=False) #grab correct sample

    distanceDiffBetweenSamples = 140 if closestPosition == yP else -165 #for difference in distance
    distanceToNextSample = kDistanceBetweenSamples * abs(yP - rP) + distanceDiffBetweenSamples
    if yP - rP == 1: distanceToNextSample = -150

    powerForSecondSample = abs(distanceToNextSample * 0.2) if distanceToNextSample > 30 else 25
    if powerForSecondSample > 85: powerForSecondSample = 85 #clamp
    
    kirby.drive.straightDistance(distanceToNextSample, powerForSecondSample)
    grabRightSample(isCurrentWhiteGreen=False) if closestPosition == yP else grabLeftSample(isCurrentWhiteGreen=False)

    distanceToLast = kDistanceBetweenSamples * (5 - rP) + 50 if closestPosition == yP else kDistanceBetweenSamples * (5 - yP) + 160 + 40 #go to the end
    
    powerForLast = distanceToLast * 0.21 if distanceToLast > 60 else 30
    if powerForLast > 80: powerForLast = 80
    
    kirby.drive.straightDistance(distanceToLast, powerForLast) if distanceToLast != 0 else kirby.drive.brake(1) #if robot already in the end dont drive

def scoreYellowRedSamples():
    kirby.drive.turnToAngle(0, power=80)
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
    kirby.drive.turnToAngle(-92)
    print(kirby.hub.imu.heading())

    kirby.drive.straightTime(600, -60)
    kirby.hub.imu.reset_heading(-90)

    kirby.drive.straightDistance(515, 80)
    kirby.drive.turnToAngle(-180)
    print(kirby.hub.imu.heading())
    kirby.drive.straightDistance(-700, 90)