from robot import Robot
from utils.constants import *

kirby = Robot()

def bajarTodos():
    kirby.mechanisms.moveBackMotorDegrees(170, 180)
    kirby.mechanisms.moveFrontMotorDegrees(95, 150)

def subirIzq():
    kirby.mechanisms.moveBackMotorDegrees(80, 180)

def bajarIzq():
    kirby.mechanisms.moveBackMotorDegrees(180, 180)

def subirDer():
    kirby.mechanisms.moveFrontMotorDegrees(50, 150)

def bajaDer():
    kirby.mechanisms.moveFrontMotorDegrees(95, 150)

def roberydron():
    kirby.drive.straightTime(450, -50)
    kirby.hub.imu.reset_heading(0) #choca y resetea imu

    kirby.drive.straightDistance(35, 40)
    kirby.drive.turnToAngle(-35, safeExitTime=700)
    kirby.drive.straightDistance(380, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(55, 30) #align

    kirby.drive.turnToAngle(180)
    kirby.mechanisms.moveBackMotorDegrees(150,300)#baja alita
    kirby.drive.straightDistance(-100,70)
    kirby.mechanisms.moveBackMotorDegrees(100,300)#sube alita

    kirby.drive.straightDistance(100,80)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightDistance(390, 80)
    kirby.drive.turnToAngle(180)

    #kirby.drive.waitUntilButton()

    kirby.drive.straightDistance(-200,70)

    kirby.mechanisms.moveBackMotorDegrees(170,300)
    #kirby.mechanisms.moveBackMotorTime(800,200)#agarra dron
    kirby.drive.straightDistance(190,70)
    kirby.drive.turnToAngle(-90,power=50)
    kirby.drive.straightDistance(-750,80)

    #kirby.drive.waitUntilButton()

    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(-280,70)
    kirby.mechanisms.moveBackMotorDegrees(0,400) # dejar dron

def blancaAmarilla():
    kirby.drive.straightDistance(280,70)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightDistance(710,80)
    kirby.drive.straightTime(1000,30)#abance hacia antes de blanca
    kirby.hub.imu.reset_heading(-90)
    kirby.drive.straightDistance(-60,40)
    kirby.drive.turnToAngle(0)

    kirby.drive.straightDistance(1000,90)
    #kirby.drive.waitUntilButton()
    kirby.drive.straightUntilReflection(kReflectionBlack,30)

    kirby.mechanisms.moveFrontMotorDegrees(95, 200)

    kirby.drive.trackLineDistance(200, 50, side="left")
    kirby.drive.straightDistance(85, 40)
    kirby.mechanisms.moveFrontMotorDegrees(50, 200)

    kirby.drive.straightDistance(-400, 70)

    kirby.drive.turnToAngle(90,power=60)
    kirby.drive.straightDistance(720, 80)


    kirby.drive.turnToAngle(0, power=60)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(180, 200)

    kirby.drive.trackLineDistance(200, 50, side="left")
    kirby.drive.straightDistance(85, 40)
    kirby.mechanisms.moveBackMotorDegrees(80, 200)

    #kirby.drive.waitUntilButton()

    kirby.drive.straightDistance(-600, 70)
    kirby.drive.turnToAngle(-90,power=60)
    kirby.drive.straightDistance(200,70)
    kirby.drive.straightUntilReflection(kReflectionBlack,40)
    kirby.drive.turnToAngle(0,power=60)
    kirby.drive.straightDistance(160,70)
    bajarTodos()

def roja():
    kirby.drive.straightDistance(-160,70)
    kirby.drive.turnToAngle(-90)
    subirIzq()
    kirby.drive.straightDistance(-300,80)
    kirby.drive.straightTime(800,-50)
    kirby.hub.imu.reset_heading(-90)
    kirby.drive.straightDistance(100,60)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightUntilReflection(kReflectionBlack,40)

    bajaDer()

    kirby.drive.trackLineDistance(200, 50, side="left")
    kirby.drive.straightDistance(85, 40)
    subirDer()

    #kirby.drive.waitUntilButton()

def blanca():
    kirby.drive.straightDistance(-450, 70)
    kirby.drive.turnToAngle(-90, power=70)
    kirby.drive.straightDistance(720, 60)
    kirby.drive.turnToAngle(0, power=70)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)

    kirby.mechanisms.moveBackMotorDegrees(170, 150)

    kirby.drive.trackLineDistance(200, 50, side="left")
    kirby.drive.straightDistance(85, 40)
    subirIzq()

def irAInicio():
    kirby.drive.straightDistance(-100, 70)
    kirby.drive.turnToAngle(180, power=70, safeExitTime=1400)

    kirby.drive.straightDistance(1300, 90)
    kirby.drive.turnToAngle(90,power=60)
    kirby.drive.straightDistance(630,70)
    kirby.drive.turnToAngle(180,power=60)
    kirby.drive.straightDistance(110,80)
    bajarTodos()

def dron2():
    
    kirby.drive.straightDistance(-200,80)
    subirIzq()
    subirDer()
    kirby.drive.turnToAngle(90)
    kirby.drive.straightDistance(110,50)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(1370,70)

def blacksamples():
    kirby.drive.straightDistance(-600,70)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightTime(700,-70)
    kirby.hub.imu.reset_heading(-90)
    kirby.drive.straightDistance(700,80)
    kirby.drive.turnToAngle(0)
    kirby.drive.straightDistance(-300,50)
    kirby.drive.turnToAngle(-90)
    kirby.drive.straightDistance(-400,70)
    kirby.drive.turnToAngle(180,oneWheel="left")
    kirby.drive.straightDistance(-300,80)

def last():
    kirby.drive.straightDistance(100,70)
    kirby.drive.turnToAngle(-90)

    kirby.drive.straightUntilReflection(kReflectionBlack,40)
    kirby.drive.turnToAngle(0,power=60)
    bajarTodos()
    kirby.drive.straightDistance(160,70)
    subirDer()
    subirIzq()
    kirby.drive.turnToAngle(180,power=60)
    kirby.drive.straightDistance(-650, 90)
    kirby.drive.straightTime(700,-70)
    kirby.drive.straightDistance(50,50)
    bajarTodos()
    
