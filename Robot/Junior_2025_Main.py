from Junior_2025_Kirby import *

kirby = Kirby()

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

def start():    
    kirby.driveStraightDegrees(320, 90)
    kirby.brake(1)
    kirby.driveStraightUntilReflection(10,50)
    kirby.driveStraightDegrees(100, 70)
    
    kirby.turnInPlace(-90, 60)
    
    kirby.driveStraightDegrees(100,-90)
    kirby.driveStraightTime(500, -70)
    kirby.hub.imu.reset_heading(-90)
    wait(100)
    kirby.driveStraightDegrees(600,90)
    kirby.driveStraightUntilReflection(10,40)
    kirby.driveStraightDegrees(130, 90)
    

def rover():
    kirby.turnInPlace(0, 60)
    wait(50)
    kirby.driveStraightDegrees(170,80)
    kirby.moveFrontMotorDegrees(130,700)
    wait(50)

def takeWaterTanks():
    kirby.driveStraightDegrees(170, -80)
    kirby.moveFrontMotorDegrees(0,700)
    kirby.turnInPlace(-90,60)
    wait(50)
    kirby.driveStraightUntilReflection(10,-40)
    wait(50)
    kirby.driveStraightDegrees(15,60)
    kirby.turnInPlace(0,60)
    wait(50)
    
    kirby.driveStraightDegrees(250, -70)
    wait(50)
    #kirby.turnInPlace(0,50)
    kirby.moveBackMotorTime(800,700)
    kirby.backMotor.brake()
    wait(50)
    kirby.driveStraightTime(600,-80)
    kirby.driveStraightDegrees(70, 100)
    
    #kirby.moveBackMotorTime(100,700)
    kirby.driveStraightTime(400,-90)
    #kirby.turnInPlace(0, 50)
    kirby.driveStraightDegrees(110,80)
    wait(100)

def goToBox():
    kirby.moveBackMotorDegrees(60, 150)
    kirby.turnInPlace(-90, 60)
    kirby.brake(50)
    kirby.driveStraightDegrees(500, 90)
    kirby.driveStraightUntilReflection(10, 40)
    kirby.driveStraightDegrees(200, -70)
    kirby.turnInPlace(-179, 60)
    kirby.brake(50)
    kirby.driveStraightUntilReflection(10, -50)
    
    #kirby.turnInPlace(-180, 60)
    #1243548
    kirby.moveFrontMotorTime(800,700)
    #kirby.moveFrontMotorDegrees(180,700)
    #avancedetanquesito
    kirby.driveStraightDegrees(275, 70)#275
    kirby.moveFrontMotorDegrees(60,100)
    kirby.driveStraightDegrees(70, 60)
    kirby.driveStraightDegrees(60, 40)
    
def leaveWaterTanks():
    
    kirby.driveStraightUntilReflection(10,-40)
    wait(10)
    kirby.driveStraightDegrees(100,80)
    wait(10)
    kirby.turnInPlace(-90,60)
    kirby.driveStraightUntilReflection(10,40)
    wait(10)
    #kirby.turnInPlace(-90,60)
    kirby.brake
    kirby.driveStraightDegrees(25,-60)
    kirby.turnInPlace(-180,70)
    kirby.moveFrontMotorDegrees(165,700)
    #kirby.moveFrontMotorTime(500,800)#500,200
    kirby.driveStraightDegrees(150,80)
    
    #wait(10)
    kirby.moveBackMotorDegrees(90,100)
    wait(10)
    kirby.moveBackMotorDegrees(0,700)
    wait(350)
def goToSamples():
    kirby.driveStraightDegrees(400,-90)
    kirby.turnInPlace(-90,60)
    kirby.driveStraightDegrees(100,90)
    kirby.turnInPlace(0,60)
    
    kirby.driveStraightDegrees(500,90)

def readSamples():
    kirby.driveStraightUntilReflection(10, 60)
    kirby.driveStraightDegrees(130, 60)
    kirby.turnInPlace(90,60)
    kirby.driveStraightTime(500, -60)
    kirby.hub.imu.reset_heading(90)
    kirby.driveStraightTime(500, -60)
    kirby.driveStraightDegrees(520, 80)
    kirby.brake(100)
    wait(100)

    for i in range(6):
        print(kirby.colorSensor.hsv())
        kirby.determineSamples()
        kirby.driveStraightDegrees(162, 60)
        kirby.brake(50)

'''
def readSamples():
    kirby.driveStraightUntilReflection(10, 50)
    kirby.driveStraightDegrees(200, 80)
    kirby.turnInPlace(90,60)
    kirby.driveStraightTime(1300, -60)
    kirby.hub.imu.reset_heading(90)
    kirby.driveStraightDegrees(540, 60)
    kirby.brake(100)
    wait(500)

    for i in range(6):
        print(kirby.colorSensor.hsv())
        kirby.determineSamples()
        kirby.driveStraightDegrees(165, 60)
        kirby.brake(100)
        wait(500)
'''
def drone():
    kirby.moveFrontMotorDegrees(0,500)
   
    kirby.driveStraightDegrees(70,90)
    kirby.turnInPlace(180,60)
    kirby.moveBackMotorDegrees(20,700)
    kirby.moveFrontMotorDegrees(130,500)
    kirby.driveStraightDegrees(300,90)
    kirby.driveStraightDegrees(1000,100)
    kirby.driveStraightDegrees(400,90)
    kirby.moveFrontMotorDegrees(0,700)
    kirby.driveStraightDegrees(1590,-100)
    kirby.driveStraightDegrees(230,-50)
    kirby.turnInPlace(270,60)
    kirby.driveStraightTime(500,-70)

def takesamples():
    kirby.driveStraightDegrees(500,60)
    #avanza X rotaciones dependiendo de dónde esté rojo
    samples.reverse()
    pr=samples.index("red")
    py=samples.index("yellow")
   
    print(pr)
    print(py)
   
    wait(30)
    kirby.driveStraightDegrees(160*pr,60)
    kirby.turnInPlace(180,60)
    kirby.moveFrontMotorDegrees(130,70)
    kirby.driveStraightDegrees(150,60)
    kirby.moveFrontMotorDegrees(70,70)
    kirby.driveStraightDegrees(150,-60)
    kirby.turnInPlace(270,60)
    wait(100)
    kirby.brake(100)

    if py-pr<0:
        kirby.driveStraightDegrees(160*abs(py-pr),-60)
    else:
        kirby.driveStraightDegrees(160*abs(py-pr),60)
        

        
    wait(100)
    kirby.turnInPlace(180,60)
    kirby.moveFrontMotorDegrees(130,70)
    kirby.driveStraightDegrees(170,60)
    kirby.moveFrontMotorDegrees(30,70)
    kirby.driveStraightDegrees(170,-60)
    kirby.turnInPlace(270,60)

def grabRedYellowSample(pos):
    global frontPositionToSamples

    kirby.driveStraightDegrees(160 * pos, 80)
    kirby.turnInPlace(180, 60)
    kirby.moveFrontMotorDegrees(frontPositionToSamples, 500)
    kirby.driveStraightDegrees(190, 60)#150
    kirby.moveFrontMotorDegrees(20, 700)
    kirby.driveStraightDegrees(140, -80)
    kirby.turnInPlace(270, 60)
    kirby.brake(100)

def takeFirstSamples():
    global isRedFirst, frontPositionToSamples, POSITION_TO_RED, POSITION_TO_YELLOW
    kirby.driveStraightDegrees(500,100)

    samples.reverse()
    pr=samples.index("red")
    py=samples.index("yellow")
   
    print(pr)
    print(py)

    #si el rojo es primero que el amarillo
    if pr < py:
        isRedFirst = True
        #recoger rojo
        frontPositionToSamples = POSITION_TO_RED
        grabRedYellowSample(pr)

        #recoger anarillo
        frontPositionToSamples = POSITION_TO_YELLOW
        grabRedYellowSample(py-pr)
        kirby.driveStraightDegrees(160 * (5-py), 60)

    else:
        isRedFirst = False
        frontPositionToSamples = POSITION_TO_YELLOW
        grabRedYellowSample(py)
        frontPositionToSamples = POSITION_TO_RED
        grabRedYellowSample(pr-py)
        kirby.driveStraightDegrees(160 * (5-pr), 60)

def returnToWall():
    kirby.turnInPlace(90, 60)
    kirby.driveStraightDegrees(400, -100)
    kirby.driveStraightTime(300, -80)
    kirby.moveFrontMotorDegrees(15,700)
    print(isRedFirst)

def grabGreenWhiteSamples(pos):
    global clawPositionToSamples, areSamplesInOrder

    if(clawPositionToSamples == CLAW_THREE):
        kirby.driveStraightDegrees((160 * pos) + 80, 60)
    else:
        kirby.driveStraightDegrees(160 * pos, 60)

    kirby.turnInPlace(180, 60)
    kirby.moveBackMotorDegrees(clawPositionToSamples, 200)

    if samplesState == 1:
        kirby.driveStraightDegrees(500, 60)
        kirby.moveBackMotorDegrees(0, 300)
        kirby.driveStraightDegrees(500, -60)
    else:
        kirby.driveStraightDegrees(400, 60)
        kirby.moveBackMotorDegrees(0, 300)
        kirby.driveStraightDegrees(400, -60)

    kirby.turnInPlace(90, 60)
    kirby.brake(100)

def takeSecondSamples():
    global areSamplesInOrder, clawPositionToSamples, CLAW_THREE
    #kirby.driveStraightDegrees(350,60)
    samples.reverse()
    pg=samples.index("green")
    pw=samples.index("white")
   
    print(pg)
    print(pw)

    x=162

    if pg < pw:
        if pw-pg==1:
            kirby.driveStraightDegrees(540,80)#avanza algo
            kirby.driveStraightDegrees(x*pg,80)#avanzar X*pg
            kirby.turnInPlace(180,60) #gira
            kirby.moveBackMotorDegrees(90,700) #abre
            kirby.driveStraightDegrees(450,70) #avanza
            kirby.moveBackMotorDegrees(0,500) #cierra
            kirby.driveStraightDegrees(450,-80) #atrás
        elif pw-pg==2:
            kirby.driveStraightDegrees(600,80)#avanza algo
            kirby.driveStraightDegrees(x*pg,80)#avanzar X*pg
            kirby.turnInPlace(180,60) #gira
            kirby.moveBackMotorDegrees(90,700) #abre
            kirby.driveStraightDegrees(450,70) #avanza
            kirby.moveBackMotorDegrees(0,500) #cierra
            kirby.driveStraightDegrees(450,-80) #atrás
        else:
            kirby.driveStraightDegrees(540,80)#avanza algo
            kirby.driveStraightDegrees(x*pg,80)#avanzar X*pg
            kirby.turnInPlace(180,60) #gira
            kirby.moveBackMotorDegrees(90,700) #abre
            kirby.driveStraightDegrees(450,70) #avanza
            kirby.moveBackMotorDegrees(0,500) #cierra
            kirby.driveStraightDegrees(450,-80) #atrás

            kirby.turnInPlace(90,60)
            kirby.driveStraightDegrees(x*(pw-pg-1),80)#avanzar X*pg
            kirby.turnInPlace(180,60) #gira
            kirby.moveBackMotorDegrees(90,700) #abre
            kirby.driveStraightDegrees(450,70) #avanza
            kirby.moveBackMotorDegrees(0,500) #cierra
            kirby.driveStraightDegrees(450,-80) #atrás
    else:
        kirby.driveStraightDegrees(300,80)#avanza algo #380
        kirby.driveStraightDegrees(x*pw,80)#avanzar X*pg
        kirby.turnInPlace(180,60) #gira
        kirby.moveBackMotorDegrees(90,700) #abre
        kirby.driveStraightDegrees(450,70) #avanza
        kirby.moveBackMotorDegrees(0,500) #cierra
        kirby.driveStraightDegrees(450,-80) #atrás

        kirby.turnInPlace(90,60)
        kirby.driveStraightDegrees(x*(pg-pw+1)+100,90)#avanzar X*pg
        kirby.turnInPlace(180,60) #gira
        kirby.moveBackMotorDegrees(90,700) #abre
        kirby.driveStraightDegrees(450,70) #avanza
        kirby.moveBackMotorDegrees(0,500) #cierra
        kirby.driveStraightDegrees(450,-80) #atrás



        


    '''
    if pg < pw:
        areSamplesInOrder = True
        if abs(pw - pg) == 1:
            print("if")
            grabGreenWhiteSamples(pw)
        elif abs(pw - pg) == 2:
            print("elif")
            clawPositionToSamples = CLAW_THREE
            grabGreenWhiteSamples(pg + 1)
        else:
            print("else")
            grabGreenWhiteSamples(pg)
            grabGreenWhiteSamples((pw - pg) + 1)
        
        kirby.driveStraightDegrees(160 * (5-pw), 60)

    else:
        grabGreenWhiteSamples(pw)
        samplesState = 1
        grabGreenWhiteSamples(pg - pw)
        kirby.driveStraightDegrees(160 * (5-pg), 60)
    '''

def detectgreen_white():
    pg=samples.index("green")
    pw=samples.index("white")
   
    print(pg)
    print(pw)
    if pw<pg:
        if pw-pg<2:            
            if py-pw<0:
                kirby.driveStraightDegrees(160*abs(py-pw),60)
            else:
                kirby.driveStraightDegrees(160*abs(py-pw),-60)
        


def letsamples():
    
    kirby.turnInPlace(270,60)
    kirby.driveStraightTime(2700,-70)
    kirby.hub.imu.reset_heading(-90)
    kirby.driveStraightDegrees(250,60)
    kirby.turnInPlace(0,60)
    kirby.driveStraightDegrees(400,90)
    kirby.driveStraightUntilReflection(10,60)
    kirby.driveStraightDegrees(130,90)
    kirby.turnInPlace(0,60)
    if isRedFirst == True:
        kirby.turnInPlace(-20,60)
        kirby.driveStraightDegrees(40,70)
        kirby.moveFrontMotorDegrees(130,300)
        kirby.driveStraightDegrees(30,-70)
        kirby.moveFrontMotorDegrees(30,-700)
        kirby.turnInPlace(0,60)
            

        kirby.turnInPlace(20,50)
        kirby.driveStraightDegrees(140,70)
        kirby.moveFrontMotorDegrees(130,300)
        kirby.driveStraightDegrees(140,-90)
        kirby.moveFrontMotorDegrees(0,-700)
        kirby.turnInPlace(0, 60)
        
    else:
        kirby.turnInPlace(15,60)
        kirby.driveStraightDegrees(40,70)
        kirby.moveFrontMotorDegrees(130,300)
        kirby.driveStraightDegrees(10,-90)
        kirby.moveFrontMotorDegrees(30,-700)
        kirby.driveStraightDegrees(30,-90)
        kirby.turnInPlace(0,60)


        kirby.turnInPlace(-15,60)
        kirby.driveStraightDegrees(130,70)
        kirby.moveFrontMotorDegrees(130,500)
        kirby.driveStraightDegrees(130,-90)
        kirby.turnInPlace(0,60)
       



def letsamples2():
    kirby.driveStraightUntilReflection(10,-70)
    kirby.driveStraightDegrees(550,-90)
    kirby.turnInPlace(-90,60)
    kirby.driveStraightDegrees(150,100)
    kirby.driveStraightUntilReflection(10,70)
    
    kirby.driveStraightDegrees(500,100)
    kirby.turnInPlace(-270,60)
    kirby.driveStraightTime(1000,-80)
    kirby.hub.imu.reset_heading(90)
    kirby.driveStraightDegrees(220,90)
    kirby.turnInPlace(0,60)
    kirby.driveStraightDegrees(300,100)
    kirby.driveStraightUntilReflection(10,60)
    kirby.driveStraightDegrees(360,90)
    
    
    
    kirby.driveStraightDegrees(120,80)
    kirby.turnInPlace(10,60)
    kirby.moveBackMotorDegrees(70,500)
    kirby.moveFrontMotorDegrees(0,700)
    kirby.driveStraightDegrees(200,-90)
    kirby.moveFrontMotorDegrees(160,700)
    kirby.driveStraightDegrees(50,80)
    kirby.moveLeftDriveMotorDegrees(170,500)
    wait(10)
    kirby.moveLeftDriveMotorDegrees(-200,500)
    kirby.driveStraightDegrees(100,-90)
    kirby.turnInPlace(0,60)

def finish():
    kirby.driveStraightUntilReflection(10,-70)
    kirby.driveStraightDegrees(500,-70)
    kirby.moveBackMotorDegrees(0,700)
    kirby.moveFrontMotorDegrees(0,700)
    kirby.turnInPlace(90,60)
    kirby.driveStraightTime(1000,-60)
    kirby.hub.imu.reset_heading(90)
    kirby.driveStraightUntilReflection(10,70)
    kirby.driveStraightDegrees(100,-50)
    kirby.turnInPlace(0,60)

    kirby.driveStraightDegrees(1000,100)
    kirby.turnInPlace(180,90)
    kirby.driveStraightTime(1500,-100)
    kirby.driveStraightDegrees(200,80)
    