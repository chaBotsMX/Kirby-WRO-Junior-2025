from Junior_2025_Kirby import *

kirby = Kirby()

if(Button.BLUETOOTH in kirby.hub.buttons.pressed()):
    kirby.hub.speaker.beep(500, 500)
    wait(200)
    while True:
        #print("Line Sensor:", kirby.lineSensor.reflection())
        #print("Color sensor:", kirby.colorSensor.color())
        #print("color sensor: ", kirby.colorSensor.hsv())
        #print("heading: ", kirby.getAngle(kirby.imu.heading()))
        kirby.hub.display.number(kirby.hub.battery.voltage()/1000)

print(kirby.hub.battery.voltage(), "mv")

kirby.driveStraightDegrees(1000, 50, 0.8, 0.5)