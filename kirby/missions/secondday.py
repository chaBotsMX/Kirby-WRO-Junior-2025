from robot import Robot
from utils.constants import *

kirby = Robot()

def allchallenge():
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

    kirby.drive.straightDistance(-200, 95, targetAngle=0)
    kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 400)

    kirby.drive.straightTime(400, -70, targetAngle=0)
    kirby.drive.straightDistance(25, 60, targetAngle=0) #primer pelota
    kirby.drive.brake(100)
    kirby.drive.straightTime(500, -70, targetAngle=0)
    kirby.drive.straightDistance(70, 50, targetAngle=0) #segunda pelota
    
    kirby.mechanisms.moveBackMotorDegrees(170, 300, wait=False)



    kirby.drive.turnToAngle(180,power=40, safeExitTime=2000)
    kirby.drive.straightDistance(-60,40)

    kirby.mechanisms.moveBackMotorTime(1000,300)
    kirby.drive.straightDistance(20,70)
    kirby.mechanisms.moveBackMotorDegrees(170,100)
    kirby.mechanisms.moveBackMotorTime(500,500)
    kirby.drive.straightDistance(-50,70)

    kirby.drive.straightDistance(70,70)
    kirby.mechanisms.moveBackMotorDegrees(0,400)
    
    kirby.drive.waitUntilButton()

    kirby.drive.turnToAngle(-90)
    kirby.drive.straightDistance(450,80)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(200,80)
    kirby.drive.straightUntilReflection(kReflectionBlack,30)
    kirby.drive.straightDistance(550,80)
    kirby.drive.turnToAngle(90)
    kirby.drive.straightTime(600,-70)
    kirby.hub.imu.reset_heading(90)
    kirby.drive.straightDistance(800,90)
    kirby.drive.turnToAngle(180,oneWheel="left")


    kirby.drive.straightDistance(1150,90)
    kirby.drive.straightDistance(-1100,90)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightTime(700,-50)
    kirby.hub.imu.reset_heading(-90)
    kirby.drive.straightDistance(100,50)


    kirby.drive.turnToAngle(0, power=80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 200)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200)

    kirby.drive.trackLineDistance(200, 50, side="left")
    kirby.drive.straightDistance(75, 40)

    kirby.mechanisms.moveBackMotorDegrees(80, 200)
    kirby.mechanisms.moveFrontMotorDegrees(50, 200)

    kirby.drive.straightDistance(-760,80)
    kirby.drive.turnToAngle(-90, power=60)
    kirby.drive.straightTime(700,-50)
    kirby.hub.imu.reset_heading(-90)

    kirby.drive.straightDistance(460,80)
    kirby.drive.turnToAngle(-180, power=60)
    #kirby.drive.straightDistance(50, 50)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200)
    kirby.drive.straightDistance(-50, 50)
    kirby.drive.turnToAngle(-90, 50)
    kirby.drive.straightDistance(350, 50)

    kirby.drive.turnToAngle(-180, power=60)
    kirby.drive.straightDistance(50, 50)
    kirby.mechanisms.moveBackMotorDegrees(180, 200)
    kirby.drive.straightDistance(-50, 50)
    #kirby.drive.turnToAngle(-90, 50)

    kirby.drive.turnToAngle(0, power=80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 200)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200)

    kirby.drive.trackLineDistance(200, 50, side="left")
    kirby.drive.straightDistance(75, 40)

    kirby.mechanisms.moveBackMotorDegrees(80, 200)
    kirby.mechanisms.moveFrontMotorDegrees(50, 200)

    kirby.drive.straightDistance(-760,80)
    kirby.drive.turnToAngle(90, power=60)
    kirby.drive.straightTime(700,-50)
    kirby.hub.imu.reset_heading(90)

    kirby.drive.straightDistance(76, 70)
    
    kirby.drive.turnToAngle(180, power=60)
    #kirby.drive.straightDistance(50, 50)
    kirby.mechanisms.moveFrontMotorDegrees(95, 200)
    kirby.drive.straightDistance(-50, 50)
    kirby.drive.turnToAngle(90, 50)
    kirby.drive.straightDistance(130, 50)

    kirby.drive.turnToAngle(180, power=60)
    kirby.drive.straightDistance(50, 50)
    kirby.mechanisms.moveBackMotorDegrees(180, 200)
    kirby.drive.straightDistance(-150, 50)

    kirby.drive.waitUntilButton()

    kirby.mechanisms.moveBackMotorDegrees(0, 300, wait=False)
    kirby.mechanisms.moveFrontMotorDegrees(0, 300, wait=False)
    kirby.drive.turnToAngle(-92)
    print(kirby.hub.imu.heading())

    kirby.drive.straightTime(700, -60)
    kirby.hub.imu.reset_heading(-90)

    kirby.drive.straightDistance(515, 80)
    kirby.drive.turnToAngle(-180)
    print(kirby.hub.imu.heading())
    kirby.drive.straightDistance(-750, 90)