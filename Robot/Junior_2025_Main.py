# Junior_2025_Main.py
# 24/08/2025 for WRO RoboMission Junior team chaBots Kirby
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
    kirby.moveFrontMotorDegrees(40, 500)
    kirby.driveDegrees(730, 90)
    
    kirby.moveFrontMotorDegrees(-10, 800)
    kirby.driveDegrees(-400, 90)
    
    kirby.turnInPlace(-179)
    kirby.moveFrontMotorDegrees(60, 500)
    kirby.driveDegrees(-90, 60)

def goToRover():
    kirby.driveUntilReflection(BLACK, -40)

    kirby.turnInPlace(NORTH)
    kirby.driveDegrees(190, 90)
    kirby.driveUntilReflection(BLACK, 40)
    kirby.driveDegrees(32, 50)

def rover():
    kirby.turnInPlace(EAST)
    #kirby.driveDegrees(10, 50)
    kirby.moveFrontMotorDegrees(30, 800)
    kirby.driveDegrees(-190, 90, targetAngle=EAST)

def takeWaterTanks():
    kirby.moveBackMotorDegrees(-200, 600)
    kirby.backMotor.brake()

    kirby.driveTime(500, -90, targetAngle=EAST)
    kirby.driveDegrees(40, 80, targetAngle=EAST, speedControl=False)
    kirby.driveTime(600, -90, targetAngle=EAST)

    #kirby.moveBackMotorDegrees(-185, 400)

    kirby.driveDegrees(100, 50, targetAngle=EAST, speedControl=False)
    kirby.brake(400)

def goToBox():
    kirby.turnInPlace(NORTH, power=60)
    kirby.driveDegrees(290, 90)
    kirby.driveUntilReflection(BLACK, 40)
    kirby.driveDegrees(40, 50)
    kirby.moveFrontMotorDegrees(0, 400)
    kirby.turnInPlace(-WEST, power=60)
    
def leaveWaterTanks():
    kirby.driveTime(400, 40)
    kirby.driveDegrees(-5, 50)

    kirby.moveFrontMotorDegrees(60, 500)
    kirby.frontMotor.brake()

    kirby.driveTime(700, 60)

    kirby.moveBackMotorDegrees(-55, 300)

    kirby.driveDegrees(-20, 40)
    kirby.turnInPlace(172)
    kirby.driveDegrees(-600, 90)
    kirby.turnInPlace(WEST)

def goToSamples():
    kirby.driveUntilReflection(BLACK, -40)
    kirby.moveBackMotorDegrees(-70, 300)
    kirby.driveDegrees(-20, 90)
    kirby.turnInPlace(SOUTH)
    kirby.driveTime(550, -70)
    kirby.hub.imu.reset_heading(SOUTH) #reset imu

def readSamples():
    kirby.driveAndScan(900, 90, ratio=0.2, scanningDistance=490)
    kirby.brake(100)
    #print(kirby.colorSensor.reflection())
    #kirby.driveUntilReflection(2, -40, sensor="color")
    #print(kirby.colorSensor.reflection())
    #kirby.driveDegrees(-85, 40)

def grabSample(sampleColor):
    degreesToSample = 0
    if (sampleColor == "white") or (sampleColor == "yellow"):
        kirby.turnInPlace(10)
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-35, 60)

        kirby.moveFrontMotorDegrees(0, 200)

        kirby.driveDegrees(18, 70)
        kirby.turnInPlace(SOUTH)

    elif (sampleColor == "green") or (sampleColor == "red"):
        kirby.turnInPlace(-5, power=85, oneWheel="right")
        #kirby.turnInPlace(45, oneWheel="right")
        #kirby.turnInPlace(-10)
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-150, 60)

        kirby.moveFrontMotorDegrees(0, 200)

        kirby.driveDegrees(150, 70)
        kirby.turnInPlace(SOUTH, power=95, oneWheel="right")
        #kirby.turnInPlace(45)
        #kirby.turnInPlace(SOUTH, oneWheel="right")
        #kirby.turnInPlace(SOUTH)

    elif sampleColor == "whiteAndGreen":
        kirby.turnInPlace(20)
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-85, 50)

        kirby.moveFrontMotorDegrees(0, 200)

        kirby.driveDegrees(80, 70)
        kirby.turnInPlace(SOUTH)

    elif sampleColor == "yellowLast":
        kirby.driveDegrees(60, 50)
        kirby.turnInPlace(EAST)

        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-70, 50)
        kirby.moveFrontMotorDegrees(0, 200)
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
    kirby.driveDegrees(20, 50)
    kirby.brake(80)
    kirby.turnInPlace(180, power=90, oneWheel="right")
    kirby.driveDegrees(-440, 90)
    kirby.driveUntilReflection(BLACK, -40)
    kirby.driveDegrees(-140, 50)
    kirby.moveFrontMotorDegrees(110, 125)

def takeSecondSamples():
    kirby.driveDegrees(700, 95, ratio=0.2)
    kirby.turnInPlace(SOUTH, power=90, oneWheel="right")
    kirby.brake(80)
    kirby.driveDegrees(-30, 40)
    kirby.brake(100)

    samples.reverse()
    redPosition = samples.index("red")
    yellowPosition = samples.index("yellow")

    isRedFirst = redPosition < yellowPosition

    perfectComb = yellowPosition - redPosition == 2

    if isRedFirst:
        if perfectComb:
            kirby.driveDegrees(92 * yellowPosition, 80)
            print("PERFECT COMB!!1!!!!11")
            grabSample("whiteAndGreen")
            kirby.driveDegrees(92 * (5 - yellowPosition), 70)

        else:
            kirby.driveDegrees(92 * redPosition, 80)
            kirby.brake(50)

            grabSample("red")
            kirby.driveDegrees(92 * (yellowPosition - redPosition), 80)
            kirby.brake(50)
            grabSample("yellow")
            kirby.driveDegrees(92 * (5 - yellowPosition), 70)
        
    else:
        kirby.driveDegrees(92 * yellowPosition, 80)
        kirby.brake(50)

        grabSample("yellow")

        kirby.driveDegrees(92 * (redPosition - yellowPosition), 80)
        kirby.brake(50)

        grabSample("red")

        kirby.driveDegrees(92 * (5 - redPosition), 70)

def scoreSecondSamples():
    kirby.driveDegrees(130, 90)
    kirby.turnInPlace(WEST)
    kirby.driveDegrees(-450, 90)
    kirby.driveUntilReflection(BLACK, -40)
    kirby.driveDegrees(-140, 50)
    kirby.moveFrontMotorDegrees(110, 125)

def parking():
    kirby.driveDegrees(350, 90)
    kirby.turnInPlace(NORTH, power=90, oneWheel="left")
    kirby.driveDegrees(155, 60)
    kirby.turnInPlace(EAST, power=90, oneWheel="left")
    kirby.driveDegrees(450, 95, decel=False)