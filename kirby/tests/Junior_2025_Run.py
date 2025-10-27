""" # Junior_2025_Run.py
# 24/08/2025 for WRO RoboMission Junior team chaBots Kirby
# Alfonso De Anda

#from Junior_2025_Main import *
from Junior_2025_National import *

checkBluetoothButton()
checkLeftButton()

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts
wait(10)

timer = StopWatch()

kirby.hub.speaker.beep(1000, 100)

kirby.driveTime(650, -70)
kirby.hub.imu.reset_heading(EAST)

drone()
goToRover()
rover()
takeWaterTanks()
goToBox()
leaveWaterTanks() 

goToSamples()
readSamples()
print(samples)
takeFirstSamples()
scoreFirstSamples()
takeSecondSamples()
scoreSecondSamples()
parking()

print("time:", timer.time() / 1000, "s") """