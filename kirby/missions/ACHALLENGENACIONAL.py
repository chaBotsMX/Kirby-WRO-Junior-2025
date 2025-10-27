""" from Junior_2025_National import *

checkBluetoothButton()
checkLeftButton()

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts
wait(10)

timer = StopWatch()
#<Honore_villanueva>
#chaBots_Kirby
#frontmotor "arriba"=(700,700)

NORTH = -90
      =-45
EAST  = 0
      = 45 
SOUTH = 90
      = 135
WEST  = 180
      = 225

print("go")
#kirby.hub.speaker.beep(1000,100)
#kirby.driveTime(400,-MID_SPEED)
#kirby.hub.imu.reset_heading(EAST)

kirby.driveTime(750, -40)
kirby.hub.imu.reset_heading(EAST)

drone()
goToRover()


kirby.turnInPlace(EAST)
kirby.driveDegrees(-180, MID_SPEED, targetAngle=EAST)


takeWaterTanks()
goToBox()
leaveWaterTanks() 

goToSamples()

kirby.driveDegrees(150,MIN_SPEED)
kirby.driveUntilReflection(BLACK,40)
kirby.turnInPlace(NORTH)
kirby.moveFrontMotorTime(700,400)
kirby.brake(200)
kirby.driveDegrees(-465,60)#agarrar negra
kirby.brake(500)
kirby.moveFrontMotorDegrees(0,200)
kirby.driveTime(1000,-MID_SPEED)
kirby.hub.imu.reset_heading(NORTH)

kirby.driveDegrees(300,MID_SPEED)
kirby.driveUntilReflection(BLACK,40)
kirby.driveDegrees(20,MID_SPEED)
kirby.brake(200)
kirby.turnInPlace(WEST)
kirby.driveDegrees(-800,MID_SPEED)
kirby.moveFrontMotorDegrees(60, 300)


#kirby.driveTime(2000,-MID_SPEED)





kirby.moveFrontMotorDegrees(110,125)#deja negra


kirby.brake(500)


kirby.driveDegrees(400,MAX_SPEED)
kirby.driveUntilReflection(BLACK,40)
kirby.turnInPlace(NORTH)
kirby.driveDegrees(-300,MID_SPEED)
kirby.moveFrontMotorDegrees(0,700)
kirby.driveTime(1000,-MID_SPEED)
kirby.hub.imu.reset_heading(NORTH)

kirby.driveDegrees(150,MID_SPEED)
kirby.brake(500)
kirby.turnInPlace(WEST)
kirby.moveFrontMotorTime(700,400)#AGARRA MUESTRA ROJA
kirby.driveUntilReflection(BLACK,-40)
kirby.driveDegrees(-170,50)
kirby.moveFrontMotorDegrees(0,120)
kirby.driveDegrees(1400,MAX_SPEED)
kirby.turnInPlace(NORTH)
kirby.driveTime(2000,-MID_SPEED)
kirby.hub.imu.reset_heading(NORTH)

kirby.driveDegrees(120,MID_SPEED)
kirby.turnInPlace(EAST)
kirby.driveUntilReflection(BLACK,-40)
kirby.driveDegrees(0,MID_SPEED)
kirby.moveFrontMotorDegrees(120,100)#deja las muestras 1
kirby.driveDegrees(1000,MAX_SPEED)
kirby.turnInPlace(NORTH)
kirby.driveUntilReflection(BLACK,40)
kirby.driveDegrees(300,MID_SPEED)
kirby.turnInPlace(SOUTH)
kirby.moveFrontMotorDegrees(0,700)
kirby.driveTime(1000,-MID_SPEED)
kirby.hub.imu.reset_heading(SOUTH)


kirby.driveDegrees(130,MID_SPEED)#avance de muestra verde
kirby.turnInPlace(WEST)
kirby.driveDegrees(-200, MID_SPEED)
kirby.driveUntilReflection(BLACK,-40)
kirby.moveFrontMotorTime(700,400)

kirby.driveDegrees(-150,MID_SPEED)#retrocede para muestras
kirby.moveFrontMotorDegrees(0,120)
kirby.driveDegrees(560,MID_SPEED)
kirby.turnInPlace(NORTH)
kirby.driveDegrees(-300,MID_SPEED)
kirby.driveUntilReflection(BLACK,-40)
kirby.driveDegrees(-130,MID_SPEED)
kirby.turnInPlace(-125)
kirby.moveFrontMotorDegrees(120,100)
kirby.brake(100)#deja las muestras 2
kirby.driveDegrees(50,MID_SPEED)
kirby.turnInPlace(WEST)
kirby.driveDegrees(500,MID_SPEED)
kirby.driveUntilReflection(BLACK,40)
kirby.driveDegrees(-10,MID_SPEED)
kirby.turnInPlace(NORTH)
kirby.moveFrontMotorDegrees(0,300)
kirby.driveTime(2500,-80)
kirby.hub.imu.reset_heading(NORTH)
kirby.driveDegrees(400,90)
kirby.driveUntilReflection(BLACK,40)

#segunda caja


kirby.driveDegrees(32, 50)
kirby.turnInPlace(-360, timeout=900)

kirby.hub.imu.reset_heading(EAST)

kirby.moveBackMotorDegrees(-200, 600) #down for water
kirby.backMotor.brake()

kirby.driveTime(1100, -50, targetAngle=EAST)
kirby.driveDegrees(40, 70, targetAngle=EAST, speedControl=False)
kirby.moveBackMotorDegrees(-190, 300)
kirby.driveDegrees(800,MID_SPEED)
kirby.turnInPlace(NORTH)
kirby.driveDegrees(30,MID_SPEED)
kirby.turnInPlace(WEST)
kirby.driveDegrees(-850,MID_SPEED)


print("time:", timer.time() / 1000, "s") """