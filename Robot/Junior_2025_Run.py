from Junior_2025_Main import *

checkBluetoothButton()
checkLeftButton()

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts
wait(100)
kirby.hub.speaker.beep(200, 100)

#kirby.driveStraightDegreesAndMoveMotor(1000, 60, 1.5, 0.1)

start()


rover()
takeWaterTanks()
goToBox()
leaveWaterTanks()

