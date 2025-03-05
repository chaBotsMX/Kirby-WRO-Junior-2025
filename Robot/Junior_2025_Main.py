from Junior_2025_Kirby import *

kirby = Kirby()

if(Button.BLUETOOTH in kirby.hub.buttons.pressed()):
    kirby.hub.speaker.beep(500, 500)
    wait(200)
    while True:
        #print("Line Sensor:", kirby.lineSensor.reflection())
        #print("Color sensor:", kirby.colorSensor.color())
        #print("color sensor: ", kirby.colorSensor.hsv())
        #print("heading: ", kirby.getAngle(kirby.hub.imu.heading()))
        print("battery voltage", kirby.hub.battery.voltage())
        kirby.hub.display.number(kirby.hub.battery.voltage()/1000)

wait(100)

print(kirby.hub.battery.voltage(), "mv")

#kirby.driveStraightDegrees(1000, 60, 0.9, 0.1)
#kirby.turnInPlace(90, 60, 0.9, 0)
#kirby.moveFrontMotorDegrees(90, 300)
kirby.moveBackMotorDegrees(-90, 500)