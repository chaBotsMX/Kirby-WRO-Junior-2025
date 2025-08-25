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

def grabSample(order):
    degreesToSample = 0
    if order == 0:
        kirby.turnInPlace(10)
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-35, 60)

        kirby.moveFrontMotorDegrees(0, 200)

        kirby.driveDegrees(18, 70)
        kirby.turnInPlace(SOUTH)
    elif order == 1:
        kirby.turnInPlace(-5, power=85, oneWheel="right")
        #kirby.turnInPlace(45, oneWheel="right")
        #kirby.turnInPlace(-10)
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-158, 60)

        kirby.moveFrontMotorDegrees(0, 200)

        kirby.driveDegrees(158, 70)
        kirby.turnInPlace(SOUTH, power=95, oneWheel="right")
        #kirby.turnInPlace(45)
        #kirby.turnInPlace(SOUTH, oneWheel="right")
        #kirby.turnInPlace(SOUTH)

    elif order == 2:
        kirby.turnInPlace(20)
        kirby.moveFrontMotorDegrees(120, 200)
        kirby.driveDegrees(-85, 50)

        kirby.moveFrontMotorDegrees(0, 200)

        kirby.driveDegrees(80, 70)
        kirby.turnInPlace(SOUTH)

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
            grabSample(2)
            kirby.driveDegrees(94 * (whitePosition - 5), 90)
        else:
            grabSample(0)
            kirby.driveDegrees(94 * (whitePosition - greenPosition), 80)
            kirby.brake(50)
            grabSample(1)
            kirby.driveDegrees(94 * (greenPosition - 5), 90)
        
    else:
        kirby.driveDegrees(-85 - (94 * greenPosition), 80)
        kirby.brake(50)
        grabSample(1)
        kirby.driveDegrees(94 * (greenPosition - whitePosition), 80)
        kirby.brake(50)
        grabSample(0)
        kirby.driveDegrees(94 * (whitePosition - 5), 90)

def scoreFirstSamples():
    kirby.brake(80)
    kirby.turnInPlace(180, power=90, oneWheel="right")
    kirby.driveDegrees(-440, 90)
    kirby.driveUntilReflection(BLACK, -40)
    kirby.driveDegrees(-140, 50)
    kirby.moveFrontMotorDegrees(110, 125)

#generalizar verde y blanco
def grabGreenWhiteSample():
    kirby.turnInPlace(WEST) #oeste

    kirby.moveBackMotorDegrees(55, 700) #abrir garra
    kirby.driveDegrees(520, MIN_SPEED) #avanzar a muestra
    #kirby.driveDegrees(130, 35) #avanzar a muestra
    kirby.moveBackMotorDegrees(0,500) #cerrar garra
    kirby.driveDegreesAccelDecel(510, -MID_SPEED) #regresar

def grabGreenWhiteSample2():
    kirby.turnInPlace(WEST) #oeste

    kirby.moveBackMotorDegrees(55, 700) #abrir garra
    kirby.driveDegrees(450, MIN_SPEED) #avanzar a muestra
    #kirby.driveDegrees(100, 35) #avanzar a muestra

    kirby.moveBackMotorDegrees(0,500) #cerrar garra
    kirby.driveDegreesAccelDecel(510, -MID_SPEED) #regresar

def takeSecondSamples():
    global areSamplesInOrder, clawPositionToSamples, CLAW_THREE

    samples.reverse() #reversar el orden de la lista

    posGreen = samples.index("green")
    posWhite = samples.index("white")
    print(posGreen)
    print(posWhite)

    spacingDegrees = 165

    #si el verde es antes del blanco
    if posGreen < posWhite:
        #si la diferencia es de uno (estan al lado)
        if posWhite - posGreen == 1:
            kirby.driveDegrees(515, MID_SPEED) #avanzar n grados
            kirby.driveDegreesAccelDecel(spacingDegrees * posGreen, MID_SPEED) #avanzar hasta posicion de verde

            grabGreenWhiteSample()

            kirby.turnInPlace(270)
            kirby.driveDegreesAccelDecel((spacingDegrees * (5 - posWhite)) * -1, MAX_SPEED) #avanzar hasta la ultima posicion

        #si la diferencia es de dos (estan separados por uno)
        #elif posWhite - posGreen == 2:
            #kirby.driveDegrees(600, MID_SPEED) #avanza algo
            #kirby.driveDegrees(spacingDegrees * posGreen, MID_SPEED) #avanzar hasta posicion de verde

            #grabGreenWhiteSample()

        #otro caso
        else:
            kirby.driveDegrees(510, MID_SPEED) #avanzar
            kirby.driveDegreesAccelDecel(spacingDegrees * posGreen, MID_SPEED) #avanzar hasta verde
            grabGreenWhiteSample2() #tomar muestra verde

            kirby.turnInPlace(90)
            kirby.driveDegreesAccelDecel(spacingDegrees * (posWhite - posGreen - 1), MID_SPEED) #avanzar hasta blanco

            grabGreenWhiteSample() #tomar muestra blanca

            kirby.turnInPlace(270)
            kirby.driveDegreesAccelDecel((spacingDegrees * (5 - posWhite)) * -1, MAX_SPEED) #avanzar hasta la ultima posicion

    #si el blanco es antes de verde
    else:
        kirby.driveDegrees(320, MID_SPEED) #avanzar hasta primer espacio
        kirby.driveDegreesAccelDecel(spacingDegrees * posWhite, MID_SPEED) #avanzar hasta posicion de muestra blanca

        grabGreenWhiteSample() #tomar muestra blanca

        kirby.turnInPlace(SOUTH) #SUR
        kirby.driveDegreesAccelDecel(spacingDegrees * (posGreen - posWhite + 1) + 100, MID_SPEED) #avanzar hasta verde
        
        grabGreenWhiteSample() #tomar muestra verde

        kirby.turnInPlace(270)
        kirby.driveDegreesAccelDecel((spacingDegrees * (5 - posGreen)) * -1, MAX_SPEED) #avanzar hasta la ultima posicion

def alignToWall():
    #kirby.turnInPlace(270, timeLimit=1500) #norte

    kirby.driveDegreesAccelDecel(-300, MAX_SPEED) #atras
    kirby.driveTime(400, -MID_SPEED) #atras hasta pared
    kirby.hub.imu.reset_heading(-90) #reset imu


def leaveRedSample():
    kirby.turnInPlace(20) #20 grados a la derecha

    kirby.driveDegrees(80, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(140, 300) #bajar sample rojo

    kirby.driveDegrees(30, -MIN_SPEED) #atras
    kirby.moveFrontMotorDegrees(30, -700) #subir mecanismo
    #kirby.driveDegrees(30, -MID_SPEED) #atras

    kirby.turnInPlace(EAST) #este

def leaveRedSample2():
    kirby.turnInPlace(20) #20 grados a la derecha

    kirby.driveDegrees(80, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(140, 300) #bajar sample rojo

    kirby.driveDegrees(40, -MIN_SPEED) #atras
    #kirby.moveFrontMotorDegrees(30, -700) #subir mecanismo
    #kirby.driveDegrees(30, -MID_SPEED) #atras

    kirby.turnInPlace(EAST) #este

def leaveYellowSample():
    kirby.turnInPlace(-20) #20 grados a la izquierda

    kirby.driveDegrees(35, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(140, 200) #bajar sample amarillo

    kirby.driveDegrees(30, -MIN_SPEED) #atras
    kirby.moveFrontMotorDegrees(30, -700) #subir mecanismo frente
    #kirby.driveDegrees(30, -MID_SPEED) #atras

    kirby.turnInPlace(EAST) #este

def leaveYellowSample2():
    kirby.turnInPlace(-25) #20 grados a la izquierda

    kirby.driveDegrees(60, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(140, 200) #bajar sample amarillo

    kirby.driveDegrees(30, -MIN_SPEED) #atras
    #kirby.moveFrontMotorDegrees(30, -700) #subir mecanismo frente
    kirby.driveDegrees(40, -MID_SPEED) #atras

    kirby.turnInPlace(EAST) #este

def dropFirstamples():
    kirby.driveDegreesAccelDecel(210, MID_SPEED) #adelante
    kirby.turnInPlace(EAST) #este

    kirby.driveDegreesAccelDecel(500, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 10
    kirby.driveDegrees(160, MID_SPEED) #adelante

    kirby.turnInPlace(EAST) #este

    #si primero agarraste rojo
    if isRedFirst == True:
        leaveYellowSample() #dejar sample amarillo
        leaveRedSample2() #dejar sample rojo
        
    #si primer agarraste amarillo
    else:
        leaveRedSample() #dejar sample rojo
        leaveYellowSample2() #dejar sample amarillo

def goToDropSecondSamples():
    #kirby.driveUntilReflection(BLACK, -70)
    #kirby.driveDegrees(550,-90)

    kirby.driveDegreesAccelDecel(850, -MAX_SPEED) #atras
    kirby.turnInPlace(NORTH) #norte

    kirby.driveDegreesAccelDecel(550, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 8
    kirby.driveDegreesAccelDecel(650, MAX_SPEED) #adelante

    kirby.turnInPlace(-270, timeLimit=1700) #sur
    kirby.driveDegrees(100, -MAX_SPEED) #atras
    kirby.driveTime(800, -MID_SPEED) #atras para pared
    kirby.hub.imu.reset_heading(90) #reset imu

    kirby.driveDegreesAccelDecel(180, MID_SPEED) #adelante
    kirby.turnInPlace(EAST) #este

    kirby.driveDegreesAccelDecel(380, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 9

def dropSecondSamples():
    kirby.driveDegreesAccelDecel(540, MID_SPEED) #adelante

    #kirby.turnInPlace(EAST) #10 grados a la derecha
    
    kirby.moveBackMotorDegrees(90, 500) #abrir garra
    kirby.moveFrontMotorDegrees(0,700) #subir mecanismo frente
    kirby.driveDegrees(200, -MIN_SPEED) #atras

    kirby.moveFrontMotorDegrees(160, 700) #bajar mecanismo frente
    #kirby.driveDegrees(50, MIN_SPEED) #adelante
    kirby.moveLeftDriveMotorDegrees(160, 500) #adelante motor izquierdo
    wait(10)

    kirby.moveLeftDriveMotorDegrees(-160, 500) #atras motor izquierdo

    #kirby.moveRightDriveMotorDegrees(150, 500) #atras motor DERECHO
    #kirby.moveRightDriveMotorDegrees(-150, 500) #atras motor DERECHO

    kirby.driveDegrees(60, -MAX_SPEED) #atras

def parking():
    kirby.driveUntilReflection(BLACK, -MIN_SPEED) #atras hasta linea 9
    kirby.driveDegreesAccelDecel(550, -MID_SPEED) #atras

    kirby.moveBackMotorDegrees(0, 700) #cerrar garra
    kirby.moveFrontMotorDegrees(0,700) #subir mecanismo frente

    kirby.turnInPlace(SOUTH) #sur

    kirby.driveDegreesAccelDecel(640, MAX_SPEED)
    kirby.brake(50)
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 8
    kirby.brake(50)
    kirby.driveDegrees(40, -MIN_SPEED) #atras
    kirby.turnInPlace(EAST) #este

    kirby.driveDegrees(1350, MAX_SPEED) #adelante