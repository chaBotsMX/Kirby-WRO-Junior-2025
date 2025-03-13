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
        #kirby.hub.display.text(str(round(kirby.hub.battery.voltage()/1000, 2)))

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

#kirby.driveStraightDegrees(600, 80, 1.5, 0.1)
#kirby.turnInPlace(90, 70, 5.5, 0.1)
#kirby.driveStraightDegrees(600, 80, 1.5, 0.1)

'''
kirby.turnInPlace(90, 60, 10, 0.1)
kirby.turnInPlace(180, 60, 10, 0.1)
kirby.turnInPlace(270, 60, 10, 0.1)
kirby.turnInPlace(360, 60, 10, 0.1)
'''

#kirby.lineFollowDegrees(10000, 60, 1, 1)

#ROVER
kirby.frontMotor.brake()
kirby.driveStraightDegrees(780, -60, 1.5, 0.1)
kirby.turnInPlace(-90, 60, 10, 0.1)
#kirby.driveStraightDegrees(500, 60, 1.5, 0.1)
kirby.driveStraightTime(1300, 60)
kirby.hub.imu.reset_heading(-90)
wait(400)
kirby.driveStraightDegrees(673, -60, 1.5, 0.1)
wait(200)
kirby.moveFrontMotorDegrees(-90,200)
kirby.turnInPlace(0, 40, 10, 0.1)
kirby.moveBackMotorDegrees(185, 300)
wait(500)
kirby.moveFrontMotorDegrees(0,500)
kirby.turnInPlace(0,60,10,0.1)
#TOMAR PELOTAS


kirby.driveStraightDegrees(350, 60, 1.5, 0.1)
kirby.turnInPlace(0,60,10,0.1)
wait(200)
kirby.driveStraightDegrees(100, -60,1.5,0.1)
wait(200)
kirby.driveStraightDegrees(150, 60, 1.5, 0.1)
wait(400)
kirby.driveStraightDegrees(210, -60,1.5,0.1)
kirby.moveBackMotorDegrees(0, 200)
kirby.turnInPlace(0, 60, 10, 0.1)
kirby.driveStraightDegrees(100,60,1.5,0.1)
kirby.turnInPlace(90,60,10,0.1)
#kirby.lineFollowDegrees(900, 60, 0.6, 1)
wait(100)
kirby.driveStraightDegrees(900,80,1.5,0.1)
kirby.driveStraightTime(1500, 60)
kirby.driveStraightDegrees(350,-60,1.5,0.1)
kirby.turnInPlace(0, 60, 10, 0.1)
kirby.driveStraightDegrees(100,-60,1.5,0.1)
kirby.moveBackMotorDegrees(187, 300)
wait(200)
kirby.driveStraightDegrees(88,60,1.5,0.1)
kirby.moveBackMotorDegrees(120, 500)
kirby.driveStraightDegrees(85,60,1.5,0.1)
kirby.driveStraightDegrees(100,-60,1.5,0.1)
#DEJAR PELOTAS

kirby.moveFrontMotorDegrees(-300,600)
kirby.turnInPlace(200, 60, 10, 0.1)
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







#kirby.moveFrontMotorDegrees(-90,200)
#kirby.driveStraightDegrees(200, 60, 1.5, 0.1)


'''
wait(100)
kirby.turnInPlace(0, 40, 8.5, 0)
kirby.moveBackMotorDegrees(190, 300)
kirby.driveStraightDegrees(290, 85, 1.5, 0.1)
wait(500)
kirby.driveStraightDegrees(290, -60, 1.5, 0.1)
kirby.moveBackMotorTime(800, -200)
'''