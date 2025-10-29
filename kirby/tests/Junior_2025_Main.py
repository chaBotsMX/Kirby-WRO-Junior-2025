""" # Junior_2025_Main.py
# 05/09/2025 for WRO RoboMission Junior team chaBots Kirby
# Alfonso De Anda

from Junior_2025_Kirby import *

kirby = Kirby()

BLACK = 17 #valor de reflexion en linea
WHITE = 59

MAX_SPEED = 95 #velocidad maxima
MIN_SPEED = 50 #velocidad minima
MID_SPEED = 85 #velocidad media

NORTH = -90
EAST = 0
SOUTH = 90
WEST = 180  


#accion de boton derecho (imprmir datos)
def checkBluetoothButton():
    if(Button.BLUETOOTH in kirby.hub.buttons.pressed()):
        kirby.hub.speaker.beep(500, 500)
        wait(200)
        while True:
            #print("Line Sensor:", kirby.lineSensor.reflection())
            #print("color sensor: ", kirby.colorSensor.hsv())
            print("heading: ", kirby.getAngle(kirby.hub.imu.heading()))
            #print("battery voltage", kirby.hub.battery.voltage())

#accion de boton izquierdo (calibrar sensor linea)
def checkLeftButton():
    global MAX_LIGHT, MIN_LIGHT
    if(Button.LEFT in kirby.hub.buttons.pressed()):
        kirby.hub.speaker.beep(200, 400)
        for i in range (50000):
            if MAX_LIGHT < kirby.lineSensor.reflection():
                MAX_LIGHT = kirby.lineSensor.reflection()
            if MIN_LIGHT > kirby.lineSensor.reflection():
                MIN_LIGHT = kirby.lineSensor.reflection()
        kirby.hub.speaker.beep(100, 400)
        print("black: ", MIN_LIGHT)
        print("white: ", MAX_LIGHT)

def drone():
    kirby.moveFrontMotorDegrees(40, 500) #up for drone
    kirby.driveDegrees(730, 90)
    
    kirby.moveFrontMotorDegrees(-10, 800) #grab drone
    kirby.driveDegrees(-400, 90)
    
    kirby.turnInPlace(-179) #west
    kirby.moveFrontMotorDegrees(60, 500)
    kirby.driveDegrees(-90, 60)

def goToRover():
    kirby.driveUntilReflection(BLACK, -40)
    kirby.driveDegrees(-10, 40)

    kirby.turnInPlace(NORTH)
    kirby.driveDegrees(185, 90, accel=False)
    kirby.driveUntilReflection(BLACK, 40) #rover and water line
    kirby.driveDegrees(32, 50)

def rover():
    kirby.turnInPlace(EAST, power=85)
    #kirby.waitUntilButton()
    kirby.moveFrontMotorDegrees(32, 800) #down for drone
    kirby.driveDegrees(-195, 90, targetAngle=EAST)

def takeWaterTanks():
    kirby.moveBackMotorDegrees(-200, 600) #down for water
    kirby.backMotor.brake()

    kirby.driveTime(500, -90, targetAngle=EAST)
    kirby.driveDegrees(40, 80, targetAngle=EAST, speedControl=False)
    kirby.driveTime(600, -90, targetAngle=EAST)

    kirby.driveDegrees(100, 50, targetAngle=EAST, speedControl=False)
    kirby.brake(400)

def goToBox():
    kirby.turnInPlace(NORTH, power=60)
    kirby.driveDegrees(290, 90)
    kirby.driveUntilReflection(BLACK, 40) #water line
    kirby.driveDegrees(40, 50)
    kirby.moveFrontMotorDegrees(0, 400)
    kirby.turnInPlace(-WEST, power=60)
    
def leaveWaterTanks():
    kirby.driveTime(360, 40) #align
    kirby.driveDegrees(-7, 40)

    kirby.moveFrontMotorDegrees(60, 500)
    kirby.frontMotor.brake()

    kirby.driveTime(700, 60)

    kirby.moveBackMotorDegrees(-50, 300) #score waters
    kirby.brake(150)

    kirby.driveDegrees(-40, 40)
    kirby.turnInPlace(172)
    kirby.moveBackMotorDegrees(-70, 400) #safe position
    kirby.driveDegrees(-625, 90)
    kirby.turnInPlace(WEST)

def goToSamples():
    kirby.driveUntilReflection(BLACK, -40)
    kirby.driveDegrees-(20, 60)
    kirby.turnInPlace(SOUTH)
    kirby.driveTime(500, -70)
    kirby.hub.imu.reset_heading(SOUTH) #reset imu

def readSamples():
    kirby.driveAndScan(900, 90, ratio=0.2, scanningDistance=490)
    kirby.brake(100)

def grabSample(sampleColor):
    degreesToSample = 0
    if (sampleColor == "white") or (sampleColor == "yellow"):
        kirby.turnInPlace(10)
        kirby.moveFrontMotorDegrees(120, 200) #down for sample
        kirby.driveDegrees(-35, 60)

        kirby.moveFrontMotorDegrees(10, 200) #up for sample

        kirby.driveDegrees(18, 70)
        kirby.turnInPlace(SOUTH)

    elif (sampleColor == "green") or (sampleColor == "red"):
        kirby.turnInPlace(-5, power=85, oneWheel="right")
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-150, 60)

        kirby.moveFrontMotorDegrees(10, 200)

        kirby.driveDegrees(150, 70)
        kirby.turnInPlace(SOUTH, power=95, oneWheel="right")

    elif sampleColor == "whiteAndGreen":
        kirby.turnInPlace(20)
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-85, 50)

        kirby.moveFrontMotorDegrees(10, 200)

        kirby.driveDegrees(80, 70)
        kirby.turnInPlace(SOUTH)

    elif sampleColor == "yellowLast":
        kirby.driveDegrees(60, 50)
        kirby.turnInPlace(EAST)

        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-70, 50)
        kirby.moveFrontMotorDegrees(10, 200)
        kirby.driveDegrees(70, 50)
        kirby.turnInPlace(SOUTH)

        kirby.driveDegrees(-50, 50)

def takeFirstSamples():
    samples.reverse()
    whitePosition = samples.index("white")
    greenPosition = samples.index("green")

    isWhiteFirst = whitePosition < greenPosition

    perfectComb = greenPosition - whitePosition == 2

    if isWhiteFirst:
        kirby.driveDegrees(-85 - (94 * whitePosition), 80)
        kirby.brake(50)

        if perfectComb:
            print("PERFECT COMB!!1!!!!11")
            grabSample("whiteAndGreen")
            kirby.driveDegrees(94 * (whitePosition - 5), 90, ratio=0.4)
        else:
            grabSample("white")
            kirby.driveDegrees(94 * (whitePosition - greenPosition), 80)
            kirby.brake(50)
            grabSample("green")
            kirby.driveDegrees(94 * (greenPosition - 5), 65, ratio=0.4)
        
    else:
        kirby.driveDegrees(-85 - (94 * greenPosition), 80)
        kirby.brake(50)
        grabSample("green")
        kirby.driveDegrees(94 * (greenPosition - whitePosition), 80)
        kirby.brake(50)
        grabSample("white")
        kirby.driveDegrees(94 * (whitePosition - 5), 65, ratio=0.4)

def scoreFirstSamples():
    kirby.brake(80)
    kirby.driveDegrees(30, 40)
    kirby.brake(120)
    kirby.turnInPlace(180, power=90, oneWheel="right")
    kirby.driveDegrees(-440, 95)
    kirby.driveUntilReflection(BLACK, -40) #white green line
    kirby.driveDegrees(-140, 50)
    kirby.moveFrontMotorDegrees(110, 125)

def takeSecondSamples():
    kirby.driveDegrees(790, 95, ratio=0.3)
    kirby.turnInPlace(SOUTH)
    kirby.brake(80)
    kirby.driveTime(770, -70)
    kirby.hub.imu.reset_heading(SOUTH) #reset imu

    samples.reverse()
    redPosition = samples.index("red")
    yellowPosition = samples.index("yellow")

    isRedFirst = redPosition < yellowPosition

    perfectComb = yellowPosition - redPosition == 2

    if isRedFirst:
        if perfectComb:
            kirby.driveDegrees(230 + (92 * yellowPosition), 80)
            print("PERFECT COMB!!1!!!!11")
            grabSample("whiteAndGreen")
            kirby.driveDegrees(162 + (92 * (5 - yellowPosition)), 70)

        else:
            kirby.driveDegrees(230 + (92 * redPosition), 80)
            kirby.brake(50)

            grabSample("red")
            kirby.driveDegrees(92 * (yellowPosition - redPosition), 80)
            kirby.brake(50)
            grabSample("yellow")
            kirby.driveDegrees(162 + (92 * (5 - yellowPosition)), 70)
        
    else:
        kirby.driveDegrees(230 + (92 * yellowPosition), 80)
        kirby.brake(50)

        grabSample("yellow")

        kirby.driveDegrees(92 * (redPosition - yellowPosition), 80)
        kirby.brake(50)

        grabSample("red")

        kirby.driveDegrees(162 + (92 * (5 - redPosition)), 70)

def scoreSecondSamples():
    kirby.turnInPlace(WEST)
    kirby.driveDegrees(-530, 95)
    kirby.driveUntilReflection(BLACK, -40) #yellow red line
    kirby.driveDegrees(-150, 50)
    kirby.moveFrontMotorDegrees(110, 125) #score

def surpriseRule():
    kirby.driveDegrees(-10, 50)
    kirby.turnInPlace(10)
    kirby.moveFrontMotorDegrees(-10, 800)
    kirby.turnInPlace(EAST)
    kirby.driveDegrees(-1700, 95)
    kirby.turnInPlace(WEST)

def parking():
    kirby.driveDegrees(450, 95)
    kirby.turnInPlace(NORTH)
    kirby.driveTime(750, -70)
    kirby.hub.imu.reset_heading(NORTH) #reset imu
    kirby.driveDegrees(430, 90, ratio=0.4)
    kirby.turnInPlace(EAST, power=95, oneWheel="left")
    #kirby.waitUntilButton()
    kirby.driveTime(1000, 95)
    kirby.turnInPlace(-20) """