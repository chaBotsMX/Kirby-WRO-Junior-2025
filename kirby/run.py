from missions.mainDayOne import testMission, initialize, startToRover, grabWater, goToWaterBox
from pybricks.tools import StopWatch

print("Start")

runTimer = StopWatch()

#testMission()

initialize()

startToRover()
grabWater()
goToWaterBox()

print("time:", runTimer.time() / 1000, "s")