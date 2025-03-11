from Junior_2025_Kirby import *

kirby = Kirby()

#debugging
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

wait(100) #comentar en competencia

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts

'''
turn in place parametros:
power = 40
kp = 5.5
kd = 0
'''

'''
drive straight parametros:
power = 60
kp = 0.8
kd = 0.1
'''

kirby.driveStraightDegrees(720, 60, 0.8, 0.1)
kirby.turnInPlace(90, 60, 5.5, 0)
kirby.driveStraightDegrees(373, -60, 0.8, 0.1)
kirby.turnInPlace(0, 60, 5.5, 0)
kirby.moveBackMotorDegrees(190, 300)
kirby.driveStraightDegrees(290, -85, 0.8, 0.1)
wait(500)
kirby.driveStraightDegrees(290, 60, 0.8, 0.1)
kirby.moveBackMotorDegrees(-190, 100)