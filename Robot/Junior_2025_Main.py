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
            kirby.hub.display.text(str(round(kirby.hub.battery.voltage()/1000, 2)))

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
    kirby.driveStraightDegrees(350, -50, 1.5, 0.1)
    kirby.brake(1)

    kirby.driveStraightUntilReflection(10,-40,1.5,0.1)
    kirby.driveStraightDegrees(100, -60, 1.5, 0.1)
    kirby.turnInPlace(-90, 60, 8, 0.1)
    kirby.driveStraightTime(1300, 80)
    kirby.hub.imu.reset_heading(-90)
    wait(100)
    kirby.driveStraightUntilReflection(10,-40,1.5,0.1)
    kirby.driveStraightDegrees(104, 80, 1.5, 0.1)




def rover():
    kirby.moveFrontMotorDegrees(-90,200)
    kirby.turnInPlace(0, 40, 10, 0.1)
    wait(100)
    kirby.moveBackMotorDegrees(189, 300)
    wait(500)
    kirby.moveFrontMotorDegrees(0,500)
    kirby.turnInPlace(0,60,10,0.1)

def takeWaterTanks():
    

    kirby.driveStraightDegrees(350, 60, 1.5, 0.1)
    kirby.turnInPlace(0,60,10,0.1)
    wait(200)
    kirby.driveStraightDegrees(100, -60,1.5,0.1)
    wait(200)
    kirby.driveStraightDegrees(150, 60, 1.5, 0.1)
    wait(400)
    kirby.driveStraightDegrees(180, -60,1.5,0.1)
    kirby.moveBackMotorDegrees(0, 200)
    kirby.turnInPlace(0, 60, 10, 0.1)
    kirby.driveStraightDegrees(120,60,1.5,0.1)
    kirby.turnInPlace(90,40,10,0.1)
    wait(100)

def goToBox():
    kirby.driveStraightUntilReflection(10,40,1.5,0.1)
    kirby.driveStraightDegrees(500,60,1.5,0.1)
    kirby.driveStraightUntilReflection(10,80,1.5,0.1)
    kirby.driveStraightTime(1500, 60)
    kirby.driveStraightUntilReflection(10,-40,1.5,0.1)

    kirby.turnInPlace(90,60,10,0.1)

    kirby.driveStraightDegrees(50,-60,1.5,0.1)
    kirby.turnInPlace(0,60,10,0.1)
    wait(100)
    kirby.driveStraightUntilReflection(10,-40,1.5,0.1)

    kirby.turnInPlace(0, 60, 10, 0.1)
    
    kirby.driveStraightDegrees(150,-60,1.5,0.1)
    kirby.turnInPlace(0, 30, 10, 0.1)
    kirby.moveBackMotorDegrees(190, 300)
    wait(200)
    kirby.driveStraightUntilReflection(10,40,1.5,0.1)
    kirby.driveStraightDegrees(10,-60,1.5,0.1)
    
    #kirby.moveBackMotorDegrees(110, 700)
    kirby.moveBackMotorTime(500, -600)
    kirby.driveStraightDegrees(85,60,1.5,0.1)
    kirby.moveBackMotorDegrees(130, 700)
    kirby.driveStraightDegrees(100,-60,1.5,0.1)
    
def leaveWaterTanks():
    kirby.turnInPlace(200, 60, 10, 0.1)
    kirby.moveFrontMotorDegrees(-300,600)
    kirby.driveStraightDegrees(150,-60,1.5,0.1)
    wait(500)
    kirby.moveFrontMotorDegrees(-390,300)
    wait(500)
    kirby.moveFrontMotorDegrees(-270,300)
    wait(500)
    kirby.moveFrontMotorDegrees(-420,300)
    wait(500)
    kirby.driveStraightDegrees(100,60,1.5,0.1)
    kirby.turnInPlace(90, 60, 10, 0.1)
    kirby.moveFrontMotorDegrees(0,200)
    kirby.moveBackMotorDegrees(0, 200)
    kirby.driveStraightTime(1300, 60)