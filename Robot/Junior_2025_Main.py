from Junior_2025_Kirby import *

kirby = Kirby()

BLACK = 10 #valor de reflexion en linea

MAX_SPEED = 90 #velocidad maxima
MIN_SPEED = 50 #velocidad minima
MID_SPEED = 70 #velocidad media

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
            print("Line Sensor:", kirby.lineSensor.reflection())
            #print("Color sensor:", kirby.colorSensor.color())
            #print("color sensor: ", kirby.colorSensor.hsv())
            #print("heading: ", kirby.getAngle(kirby.hub.imu.heading()))
            print("battery voltage", kirby.hub.battery.voltage())
            #kirby.hub.display.text(str(round(kirby.hub.battery.voltage()/1000, 2)))

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

#inicio del recorrido
def start():    
    kirby.driveDegrees(320, MID_SPEED)
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #detectar linea 2
    kirby.driveDegrees(100, MID_SPEED)
    
    kirby.turnInPlace(NORTH) #90 grados a la izquierda(norte)
    
    kirby.driveDegrees(300, -MID_SPEED)
    kirby.driveTime(500, -MID_SPEED) #chocar con pared

    kirby.hub.imu.reset_heading(NORTH) #resetear angulo
    wait(100)

    kirby.driveDegrees(600, MAX_SPEED)
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #detectar linea 4
    kirby.driveDegrees(100, MID_SPEED)

def rover():
    kirby.turnInPlace(EAST) #girar hacia el este
    wait(50)

    kirby.driveDegrees(120, MID_SPEED)#adelante
    kirby.moveFrontMotorDegrees(130, 700) #bajar mecanismo atras
    wait(50)

def takeWaterTanks():
    kirby.driveDegrees(120, -MID_SPEED) #atras
    kirby.moveFrontMotorDegrees(0,700) #regresar mecanismo frente

    kirby.turnInPlace(NORTH) #girar al norte
    wait(50)

    kirby.driveUntilReflection(BLACK, -MIN_SPEED) #linea 4
    wait(50)

    kirby.driveDegrees(50, MIN_SPEED) #adelante

    kirby.turnInPlace(EAST) #girar al este
    kirby.brake(50)
    kirby.driveDegrees(320, -MID_SPEED) #atras
    wait(50)

    kirby.moveBackMotorTime(900, 700) #bajar mecanismo atras
    kirby.backMotor.brake()
    wait(50)

    kirby.driveTime(900, -MAX_SPEED) #recoger agua
    kirby.driveDegrees(70, MID_SPEED) #adelante
    
    kirby.driveTime(400, -MID_SPEED) #recoger segunda agua
    kirby.driveDegrees(125, MID_SPEED) #adelante
    wait(100)

def goToBox():
    kirby.moveBackMotorDegrees(60, 150) #subir mecanismo atras

    kirby.turnInPlace(NORTH)
    kirby.brake(50)

    kirby.driveDegrees(500, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 6
    kirby.driveDegrees(240, -MID_SPEED) #atras #200

    kirby.turnInPlace(-179) #oeste
    kirby.brake(50)

    kirby.driveUntilReflection(BLACK, -MIN_SPEED) #atras hasta negro
    kirby.brake(30)
    
    kirby.moveFrontMotorTime(650, 700) #bajar mecanismo frente

    kirby.driveDegrees(285, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(60, 100) #subir mecanismo frente
    kirby.driveTime(250, MID_SPEED) #adelante tiempo
    
def leaveWaterTanks():
    kirby.driveUntilReflection(10, -MIN_SPEED) #atras hasta linea 5
    wait(10)

    kirby.driveDegrees(130, MID_SPEED) #adelante
    wait(10)

    kirby.turnInPlace(NORTH) #norte

    kirby.driveUntilReflection(BLACK, MIN_SPEED) #adelante linea 6
    wait(10)
    
    kirby.driveDegrees(25, -MID_SPEED) #atras

    kirby.turnInPlace(-180) #oeste

    kirby.moveFrontMotorDegrees(165, 700) #bajar mecanismo frente
    kirby.driveDegrees(160, MID_SPEED) #adelante
    
    kirby.moveBackMotorDegrees(90, 80) #bajar mecanismo atras
    wait(100)

    kirby.moveBackMotorDegrees(0, 600) #subir mecanismo atras
    wait(500)

def goToSamples():
    kirby.driveDegrees(400, -MAX_SPEED) #atras
    kirby.turnInPlace(NORTH) #norte

    kirby.driveDegrees(100, MAX_SPEED) #adelante
    kirby.turnInPlace(EAST) #este
    
    kirby.driveDegrees(500, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 7
    kirby.driveDegrees(100, MID_SPEED) #adelante
    
    kirby.turnInPlace(SOUTH) #sur

    kirby.driveDegrees(50, -MIN_SPEED) #adelante
    kirby.driveTime(900, -MIN_SPEED) #atras para pared
    kirby.hub.imu.reset_heading(SOUTH) #reset imu
    kirby.brake(100)

def readSamples():
    kirby.driveDegrees(420, MID_SPEED) #adelante
    kirby.driveDegrees(110, MIN_SPEED) #adelante
    kirby.brake(100)

    for i in range(6):
        print(kirby.colorSensor.hsv())
        kirby.determineSamples() #detectar samples

        kirby.driveDegrees(162, MID_SPEED) #adelante
        kirby.brake(60)

def drone():
    kirby.moveFrontMotorDegrees(0,500) #subir mecanismo frente
    kirby.driveDegrees(70, MID_SPEED) #adelante

    kirby.turnInPlace(180) #oeste

    kirby.moveBackMotorDegrees(20, 700) #abrir garra
    kirby.moveFrontMotorDegrees(130, 500) #bajar mecanismo frente

    kirby.driveDegrees(300, MID_SPEED) #adelante
    kirby.driveDegrees(1000, MAX_SPEED) #adelante
    kirby.driveDegrees(200, MID_SPEED) #adelante

    kirby.moveFrontMotorDegrees(0,700) #subir mecanismo frente

    kirby.driveDegrees(300, -MID_SPEED) #atras
    kirby.driveDegrees(1090, -MAX_SPEED) #atras
    kirby.driveDegrees(230, -MID_SPEED) #atras

    kirby.turnInPlace(270) #norte
    kirby.driveTime(500, -MID_SPEED) #pared


#funcion para generalizar el agarre de primeros samples
def grabRedYellowSample(pos):
    global frontPositionToSamples

    kirby.driveDegrees(161 * pos, MID_SPEED) #adelante n posiciones

    kirby.turnInPlace(180) #este

    kirby.moveFrontMotorDegrees(frontPositionToSamples, 300) #mover motor delantero x grados

    kirby.driveDegrees(100, MID_SPEED) #adelante
    kirby.driveDegrees(60, 35) #adelante
    kirby.moveFrontMotorDegrees(20, 700) #subir motor delantero
    kirby.driveDegrees(145, -MID_SPEED) #atras

    kirby.turnInPlace(270) #norte
    kirby.brake(100)

def takeFirstSamples():
    global isRedFirst, frontPositionToSamples, POSITION_TO_RED, POSITION_TO_YELLOW
    kirby.driveDegrees(470, MID_SPEED) #adelante 480

    samples.reverse() #se cambia el orden de la lista de samples

    #se guardan las posiciones de los samples
    posRed = samples.index("red")
    posYellow = samples.index("yellow")
    print(posRed)
    print(posYellow)

    #si el rojo es primero que el amarillo
    if posRed < posYellow:
        isRedFirst = True #se guarda
        #recoger rojo
        frontPositionToSamples = POSITION_TO_RED
        grabRedYellowSample(posRed)

        #recoger amarillo
        frontPositionToSamples = POSITION_TO_YELLOW
        grabRedYellowSample(posYellow - posRed) #posicion de diferencia

        kirby.driveDegrees(161 * (5 - posYellow), MAX_SPEED) #avanzar hasta la ultima posicion

    #si el amarillo es primero que el rojo
    else:
        isRedFirst = False #se guarda

        frontPositionToSamples = POSITION_TO_YELLOW
        grabRedYellowSample(posYellow) #recoger sample amarillo primero

        frontPositionToSamples = POSITION_TO_RED
        grabRedYellowSample(posRed - posYellow)

        kirby.driveDegrees(161 * (5 - posRed), MAX_SPEED) #avanzar hasta la ultima posicion


def returnToWall():
    kirby.turnInPlace(SOUTH) #sur

    kirby.driveDegrees(400, -MAX_SPEED) #atras
    kirby.driveTime(300, -MID_SPEED) #pared
    kirby.hub.imu.reset_heading(SOUTH) #reset imu

    kirby.moveFrontMotorDegrees(15, 700) #subir motor de frente


#generalizar verde y blanco
def grabGreenWhiteSample():
    kirby.turnInPlace(WEST) #oeste

    kirby.moveBackMotorDegrees(55, 700) #abrir garra
    kirby.driveDegrees(400, MID_SPEED) #avanzar a muestra
    kirby.driveDegrees(130, 35) #avanzar a muestra
    kirby.moveBackMotorDegrees(0,500) #cerrar garra
    kirby.driveDegrees(530, -MIN_SPEED) #regresar

def grabGreenWhiteSample2():
    kirby.turnInPlace(WEST) #oeste

    kirby.moveBackMotorDegrees(55, 700) #abrir garra
    kirby.driveDegrees(400, MID_SPEED) #avanzar a muestra
    kirby.driveDegrees(100, 35) #avanzar a muestra

    kirby.moveBackMotorDegrees(0,500) #cerrar garra
    kirby.driveDegrees(510, -MIN_SPEED) #regresar

def takeSecondSamples():
    global areSamplesInOrder, clawPositionToSamples, CLAW_THREE

    samples.reverse() #reversar el orden de la lista

    posGreen = samples.index("green")
    posWhite = samples.index("white")
    print(posGreen)
    print(posWhite)

    spacingDegrees = 160

    #si el verde es antes del blanco
    if posGreen < posWhite:
        #si la diferencia es de uno (estan al lado)
        if posWhite - posGreen == 1:
            kirby.driveDegrees(510, MID_SPEED) #avanzar n grados
            kirby.driveDegrees(spacingDegrees * posGreen, MID_SPEED) #avanzar hasta posicion de verde

            grabGreenWhiteSample()

        #si la diferencia es de dos (estan separados por uno)
        #elif posWhite - posGreen == 2:
            #kirby.driveDegrees(600, MID_SPEED) #avanza algo
            #kirby.driveDegrees(spacingDegrees * posGreen, MID_SPEED) #avanzar hasta posicion de verde

            #grabGreenWhiteSample()

        #otro caso
        else:
            kirby.driveDegrees(510, MID_SPEED) #avanzar
            kirby.driveDegrees(spacingDegrees * posGreen, MID_SPEED) #avanzar hasta verde
            grabGreenWhiteSample2() #tomar muestra verde

            kirby.turnInPlace(90)
            kirby.driveDegrees(spacingDegrees * (posWhite - posGreen - 1), MID_SPEED) #avanzar hasta blanco

            grabGreenWhiteSample() #tomar muestra blanca

    #si el blanco es antes de verde
    else:
        kirby.driveDegrees(300, MID_SPEED) #avanzar hasta primer espacio
        kirby.driveDegrees(spacingDegrees * posWhite, MID_SPEED) #avanzar hasta posicion de muestra blanca

        grabGreenWhiteSample() #tomar muestra blanca

        kirby.turnInPlace(SOUTH) #SUR
        kirby.driveDegrees(spacingDegrees * (posGreen - posWhite + 1) + 100, MID_SPEED) #avanzar hasta verde
        
        grabGreenWhiteSample() #tomar muestra verde

def alignToWall():
    kirby.turnInPlace(270) #norte

    kirby.driveDegrees(800, -MAX_SPEED) #atras
    kirby.driveTime(800, -MID_SPEED) #atras hasta pared
    kirby.hub.imu.reset_heading(-90) #reset imu


def leaveRedSample():
    kirby.turnInPlace(20) #20 grados a la derecha

    kirby.driveDegrees(90, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(130, 300) #bajar sample rojo

    kirby.driveDegrees(30, -MID_SPEED) #atras
    kirby.moveFrontMotorDegrees(30, -700) #subir mecanismo
    #kirby.driveDegrees(30, -MID_SPEED) #atras

    kirby.turnInPlace(EAST) #este

def leaveYellowSample():
    kirby.turnInPlace(-20) #20 grados a la izquierda

    kirby.driveDegrees(50, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(130, 200) #bajar sample amarillo

    kirby.driveDegrees(30, -MID_SPEED) #atras
    kirby.moveFrontMotorDegrees(30, -700) #subir mecanismo frente
    #kirby.driveDegrees(30, -MID_SPEED) #atras

    kirby.turnInPlace(EAST) #este

def leaveYellowSample2():
    kirby.turnInPlace(-25) #20 grados a la izquierda

    kirby.driveDegrees(90, MIN_SPEED) #adelante
    kirby.moveFrontMotorDegrees(130, 200) #bajar sample amarillo

    kirby.driveDegrees(30, -MID_SPEED) #atras
    #kirby.moveFrontMotorDegrees(30, -700) #subir mecanismo frente
    kirby.driveDegrees(30, -MID_SPEED) #atras

    kirby.turnInPlace(EAST) #este

def dropFirstamples():
    kirby.driveDegrees(210, MID_SPEED) #adelante
    kirby.turnInPlace(EAST) #este

    kirby.driveDegrees(400, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 10
    kirby.driveDegrees(170, MID_SPEED) #adelante

    kirby.turnInPlace(EAST) #este

    #si primero agarraste rojo
    if isRedFirst == True:
        leaveYellowSample() #dejar sample amarillo
        leaveRedSample() #dejar sample rojo
        
    #si primer agarraste amarillo
    else:
        leaveRedSample() #dejar sample rojo
        leaveYellowSample2() #dejar sample amarillo

def goToDropSecondSamples():
    #kirby.driveUntilReflection(BLACK, -70)
    #kirby.driveDegrees(550,-90)

    kirby.driveDegrees(850, -MAX_SPEED) #atras
    kirby.turnInPlace(NORTH) #norte

    kirby.driveDegrees(150, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 8
    kirby.driveDegrees(500, MAX_SPEED) #adelante

    kirby.turnInPlace(-270) #sur
    kirby.driveDegrees(-300, MAX_SPEED) #adelante
    kirby.driveTime(800, -MID_SPEED) #atras para pared
    kirby.hub.imu.reset_heading(90) #reset imu

    kirby.driveDegrees(200, MID_SPEED) #adelante
    kirby.turnInPlace(EAST) #este

    kirby.driveDegrees(300, MID_SPEED) #adelante
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 9
    kirby.driveDegrees(360, MID_SPEED) #adelante

def dropSecondSamples():
    kirby.driveDegrees(135, MID_SPEED) #adelante

    kirby.turnInPlace(0) #10 grados a la derecha
    
    kirby.moveBackMotorDegrees(70, 500) #abrir garra
    kirby.moveFrontMotorDegrees(0,700) #subir mecanismo frente
    kirby.driveDegrees(200, -MID_SPEED) #atras

    kirby.moveFrontMotorDegrees(160, 700) #bajar mecanismo frente
    kirby.driveDegrees(50, MIN_SPEED) #adelante
    kirby.moveLeftDriveMotorDegrees(140, 500) #adelante motor izquierdo
    wait(10)

    kirby.moveLeftDriveMotorDegrees(-150, 500) #atras motor izquierdo

    kirby.moveLeftDriveMotorDegrees(150, 500) #atras motor DERECHO
    kirby.moveLeftDriveMotorDegrees(-150, 500) #atras motor DERECHO
    
    kirby.driveDegrees(60, -MAX_SPEED) #atras
    kirby.turnInPlace(EAST) #este

def parking():
    kirby.driveUntilReflection(BLACK, -MIN_SPEED) #atras hasta linea 9
    kirby.driveDegrees(600, -MID_SPEED) #atras

    kirby.moveBackMotorDegrees(0, 700) #cerrar garra
    kirby.moveFrontMotorDegrees(0,700) #subir mecanismo frente

    kirby.turnInPlace(SOUTH) #sur

    kirby.driveDegrees(400, MID_SPEED)
    kirby.driveUntilReflection(BLACK, MIN_SPEED) #linea 8
    kirby.brake(50)
    kirby.driveDegrees(50, -MID_SPEED) #atras
    kirby.turnInPlace(EAST) #este

    kirby.driveDegrees(1400, MAX_SPEED) #adelante