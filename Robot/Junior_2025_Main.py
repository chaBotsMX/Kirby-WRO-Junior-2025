from Junior_2025_Kirby import *

kirby = Kirby()

isRedFirst = False

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
    kirby.driveStraightDegrees(320, 60)
    kirby.brake(1)
    kirby.driveStraightUntilReflection(10,50)
    kirby.driveStraightDegrees(100, 70)
    
    kirby.turnInPlace(-90, 50)
    
    kirby.driveStraightTime(1200, -70)
    kirby.hub.imu.reset_heading(-90)
    wait(100)
    kirby.driveStraightDegrees(200,70)
    kirby.driveStraightUntilReflection(10,40)
    kirby.driveStraightDegrees(130, 70)
    

def rover():
    kirby.turnInPlace(0, 40)
    wait(100)
    kirby.driveStraightDegrees(170,70)
    kirby.moveFrontMotorDegrees(130,700)
    wait(100)

def takeWaterTanks():
    kirby.driveStraightDegrees(170, -70)
    kirby.moveFrontMotorDegrees(0,500)
    kirby.turnInPlace(-90,60)
    wait(100)
    kirby.driveStraightUntilReflection(8,-40)
    wait(100)
    kirby.driveStraightDegrees(15,60)
    kirby.turnInPlace(0,50)
    wait(100)
    
    kirby.driveStraightDegrees(190, -70)
    wait(100)
    kirby.turnInPlace(0,50)
    kirby.moveBackMotorTime(1000,700)
    kirby.backMotor.brake()
    wait(100)
    kirby.driveStraightTime(800,-60)
    kirby.driveStraightDegrees(70, 60)
    
    kirby.moveBackMotorTime(100,700)
    kirby.driveStraightTime(700,-60)
    kirby.turnInPlace(0, 50)
    kirby.driveStraightDegrees(110,60)
    wait(100)

def goToBox():
    kirby.moveBackMotorDegrees(50, 150)
    kirby.turnInPlace(-90, 60)
    kirby.brake(100)
    kirby.driveStraightDegrees(500, 70)
    kirby.driveStraightUntilReflection(10, 40)
    kirby.driveStraightDegrees(200, -70)
    kirby.turnInPlace(-179, 70)
    kirby.brake(100)
    kirby.driveStraightUntilReflection(10, -50)
    
    kirby.turnInPlace(-180, 60)
    kirby.moveFrontMotorDegrees(190,700)
    #avancedetanquesito
    kirby.driveStraightDegrees(275, 70)
    kirby.moveFrontMotorDegrees(60,100)
    kirby.driveStraightDegrees(70, 60)
    kirby.driveStraightDegrees(60, 40)
    
def leaveWaterTanks():
    kirby.driveStraightUntilReflection(10,-40)
    wait(10)
    kirby.driveStraightDegrees(100,60)
    wait(100)
    kirby.turnInPlace(-90,60)
    kirby.driveStraightUntilReflection(10,40)
    wait(10)
    kirby.turnInPlace(-90,60)
    kirby.brake
    kirby.driveStraightDegrees(30,-40)
    kirby.turnInPlace(-180,40)
    kirby.moveFrontMotorDegrees(100,200)
    kirby.moveFrontMotorTime(500,200)
    kirby.driveStraightDegrees(150,60)
    
    wait(100)
    kirby.moveBackMotorDegrees(90,100)
    wait(500)
    kirby.moveBackMotorDegrees(0,370)
  
def goToSamples():
    kirby.driveStraightDegrees(400,-60)
    kirby.turnInPlace(-90,60)
    kirby.driveStraightDegrees(100,60)
    kirby.turnInPlace(0,60)
    
    kirby.driveStraightDegrees(400,60)

def readSamples():
    kirby.driveStraightUntilReflection(10, 40)
    kirby.driveStraightDegrees(200, 60)
    kirby.turnInPlace(90,60)
    kirby.driveStraightTime(1300, -80)
    kirby.hub.imu.reset_heading(90)
    kirby.driveStraightDegrees(515, 60)
    kirby.brake(100)

    for i in range(6):
        print(kirby.colorSensor.hsv())
        kirby.determineSamples()
        kirby.driveStraightDegrees(165, 60)
        kirby.brake(100)

def drone():
    kirby.moveFrontMotorDegrees(0,500)
   
    kirby.driveStraightDegrees(100,70)
    kirby.turnInPlace(180,70)
    kirby.moveBackMotorDegrees(20,500)
    kirby.moveFrontMotorDegrees(150,400)
    kirby.driveStraightDegrees(1700,70)
    kirby.driveStraightDegrees(1790,-70)
    kirby.turnInPlace(270,70)
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
    kirby.turnInPlace(180,50)
    kirby.moveFrontMotorDegrees(130,70)
    kirby.driveStraightDegrees(150,60)
    kirby.moveFrontMotorDegrees(70,70)
    kirby.driveStraightDegrees(150,-60)
    kirby.turnInPlace(270,40)
    wait(100)
    kirby.brake(100)

    if py-pr<0:
        kirby.driveStraightDegrees(160*abs(py-pr),-60)
    else:
        kirby.driveStraightDegrees(160*abs(py-pr),60)
        

        
    wait(100)
    kirby.turnInPlace(180,50)
    kirby.moveFrontMotorDegrees(130,70)
    kirby.driveStraightDegrees(170,60)
    kirby.moveFrontMotorDegrees(30,70)
    kirby.driveStraightDegrees(170,-60)
    kirby.turnInPlace(270,40)

def grabSample(pos):
    kirby.driveStraightDegrees(160 * pos, 60)
    kirby.turnInPlace(180, 50)
    kirby.moveFrontMotorDegrees(135, 70)
    kirby.driveStraightDegrees(160, 60)
    kirby.moveFrontMotorDegrees(40, 70)
    kirby.driveStraightDegrees(160, -60)
    kirby.turnInPlace(270, 40)
    kirby.brake(100)

def takeFirstSamples():
    global isRedFirst
    kirby.driveStraightDegrees(500,60)

    samples.reverse()
    pr=samples.index("red")
    py=samples.index("yellow")
   
    print(pr)
    print(py)

    #si el rojo es primero que el amarillo
    if pr < py:
        isRedFirst = True
        #recoger rojo
        grabSample(pr)
        #recoger anarillo
        grabSample(py-pr)
        kirby.driveStraightDegrees(160 * (5-py), 60)

    else:
        isRedFirst = False
        grabSample(py)
        grabSample(pr-py)
        kirby.driveStraightDegrees(160 * (5-pr), 60)

def returnToWall():
    kirby.turnInPlace(90, 60)
    kirby.driveStraightDegrees(400, -60)
    kirby.driveStraightTime(300, -60)
    print(isRedFirst)

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
    kirby.driveStraightDegrees(300,70)
    kirby.turnInPlace(-90,70)
    kirby.driveStraightTime(2700,-70)
    kirby.driveStraightDegrees(250,60)
    kirby.turnInPlace(0,50)
    kirby.driveStraightUntilReflection(10,70)
    kirby.driveStraightDegrees(200,60)
    if isRedFirst == True:
        kirby.turnInPlace(-15,50)
        kirby.driveStraightDegrees(40,70)
        kirby.moveFrontMotorDegrees(130,60)
        kirby.driveStraightDegrees(40,-70)
        kirby.moveFrontMotorDegrees(30,-60)
        kirby.turnInPlace(0,50)
        

        kirby.turnInPlace(30,50)
        kirby.driveStraightDegrees(80,70)
        kirby.moveFrontMotorDegrees(130,60)
        kirby.driveStraightDegrees(50,-70)
        kirby.driveStraightDegrees(30,70)
        kirby.moveFrontMotorDegrees(30,-60)
        kirby.turnInPlace(0,50)
    else:
        kirby.turnInPlace(30,50)
        kirby.driveStraightDegrees(80,70)
        kirby.moveFrontMotorDegrees(130,60)
        kirby.driveStraightDegrees(50,-70)
        kirby.driveStraightDegrees(30,70)
        kirby.moveFrontMotorDegrees(30,-60)
        kirby.turnInPlace(0,50)


        kirby.turnInPlace(-15,50)
        kirby.driveStraightDegrees(40,70)
        kirby.moveFrontMotorDegrees(130,60)
        kirby.driveStraightDegrees(40,-70)
        kirby.moveFrontMotorDegrees(30,-60)
        kirby.turnInPlace(0,50)
    