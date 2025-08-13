from Junior_2025_Main import *

checkBluetoothButton()
checkLeftButton()

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts
wait(10)

timer = StopWatch()

kirby.hub.imu.reset_heading(-WEST) #reset imu

drone()
rover()
takeWaterTanks()
goToBox()
leaveWaterTanks()

print("time:", timer.time() / 1000, "s")