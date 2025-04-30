from Junior_2025_Main import *

checkBluetoothButton()
checkLeftButton()

print(kirby.hub.battery.voltage(), "mv") #bateria de kirby en miliVolts
wait(100)

tiempo=StopWatch()

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

letsamples()

letsamples2()

finish()

print("Tiempo transcurrido:", tiempo.time()/1000, "s")
