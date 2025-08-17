from Junior_2025_Main import *

checkBluetoothButton()
checkLeftButton()

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts
wait(10)

timer = StopWatch()

drone()
goToRover()
rover()
takeWaterTanks()
goToBox()
leaveWaterTanks()
goToSamples()

print("time:", timer.time() / 1000, "s")