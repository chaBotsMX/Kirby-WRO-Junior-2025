from Junior_2025_Main import *

checkBluetoothButton()
checkLeftButton()

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts
wait(100)

timer = StopWatch()


start()
rover()

takeWaterTanks()
goToBox()
leaveWaterTanks()

goToSamples() 
readSamples()
drone()

takeFirstSamples()
returnToWall()
takeSecondSamples()

alignToWall()

dropFirstamples()
goToDropSecondSamples()
dropSecondSamples()

parking()

print("Tiempo:", timer.time() / 1000, "s") 