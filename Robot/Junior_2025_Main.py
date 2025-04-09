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
            #print("battery voltage", kirby.hub.battery.voltage())
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
    kirby.frontMotor.brake()
    kirby.driveStraightDegrees(350, 50)
    kirby.brake(1)
    kirby.driveStraightUntilReflection(10,40)
    kirby.driveStraightDegrees(100, 60)
    kirby.turnInPlace(-90, 60)
    kirby.driveStraightTime(1300, -80)
    kirby.hub.imu.reset_heading(-90)
    wait(100)
    kirby.driveStraightDegrees(200,70)
    kirby.driveStraightUntilReflection(10,40)
    kirby.driveStraightDegrees(130, 60)

def rover():
    kirby.turnInPlace(0, 40)
    wait(100)
    kirby.driveStraightDegrees(150,60)
    kirby.moveFrontMotorDegrees(130,200)
    wait(100)
    #kirby.turnInPlace(0,60)

def takeWaterTanks():
    kirby.driveStraightDegrees(150, -60)
    kirby.moveFrontMotorDegrees(0,500)
    kirby.turnInPlace(-90,60)
    wait(100)
    kirby.driveStraightUntilReflection(8,-40)
    wait(100)
    kirby.driveStraightDegrees(20,60)
    kirby.turnInPlace(0,50)
    wait(300)
    
    kirby.driveStraightDegrees(250, -50)
    wait(400)
    kirby.turnInPlace(0,60)
    kirby.moveBackMotorTime(700,500)
    kirby.backMotor.brake()
    kirby.driveStraightTime(500,-60)
    kirby.driveStraightDegrees(180, 60)
    kirby.turnInPlace(0, 60)
   
    kirby.moveBackMotorDegrees(70, 40)
    wait(300)
    
    kirby.moveBackMotorTime(500,150)
    kirby.driveStraightTime(500,-60)
    kirby.turnInPlace(0, 60)
    kirby.driveStraightDegrees(120,60)
    wait(100)

def goToBox():
    kirby.moveBackMotorDegrees(50, 150)
    kirby.turnInPlace(-90, 60)
    kirby.driveStraightDegrees(500, 60)
    kirby.driveStraightUntilReflection(10, 40)
    kirby.driveStraightDegrees(220, -60)
    kirby.turnInPlace(-179, 60)
    kirby.moveFrontMotorDegrees(190,100)
    kirby.driveStraightDegrees(245, 60)
    kirby.moveFrontMotorDegrees(40,100)
    kirby.driveStraightDegrees(70, 60)
    kirby.driveStraightDegrees(60, 40)
    
def leaveWaterTanks():
    kirby.turnInPlace(190, 60, 10, 0.1)
    kirby.moveFrontMotorDegrees(-300,600)
    kirby.driveStraightDegrees(150,60,1.5,0.1)
    wait(500)
    kirby.moveFrontMotorDegrees(-390,300)
    wait(500)
    kirby.moveFrontMotorDegrees(-270,300)
    wait(500)
    kirby.moveFrontMotorDegrees(-420,300)
    wait(500)
    kirby.driveStraightDegrees(100,-60,1.5,0.1)
    kirby.turnInPlace(90, 60, 10, 0.1)
    kirby.moveFrontMotorDegrees(0,200)
    kirby.moveBackMotorDegrees(0, 200)
    kirby.driveStraightTime(1300,-60)

def goToSamples():
    kirby.driveStraightDegrees(40,60,1.5,0.1)
    kirby.turnInPlace(0,60,10,0.1)
    kirby.driveStraightDegrees(400,60,1.5,0.1)
    kirby.driveStraightUntilReflection(10,70,10,0.1)
    kirby.driveStraightDegrees(60,-60,1.5,0.1)

    kirby.turnInPlace(90,60,10,0.1)
    kirby.driveStraightTime(1300, -80)
def samples():
    kirby.driveStraightDegrees(200,-70,10,0.1)
    kirby.brake(100)
    for i in range (6):
        if kirby.colorSensor.color() == Color.RED:
            print("red")
        elif kirby.colorSensor.color() == Color.WHITE:
            print("white")
            kirby.moveFrontMotorDegrees(360,200)
        elif kirby.colorSensor.color() == Color.YELLOW:
            print("yellow")
        elif kirby.colorSensor.color() == Color.GREEN:
            print("green")
            kirby.moveFrontMotorDegrees(360,200)
        else:
            print("none")
        kirby.driveStraightDegrees(170,-50,10,0.1)
        kirby.brake(100)
        wait(500)
    



#def detectSamples():