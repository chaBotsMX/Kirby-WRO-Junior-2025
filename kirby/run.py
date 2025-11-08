# run.py
# 11/02/25 - chaBots Kirby
# Alfonso De Anda

# Robot run

from missions.mainDayOne import testMission, initialize, startToRover, grabWater, scoreWater, waterSample, scoreSampleAndDrone, whiteGreenSamples
from pybricks.tools import StopWatch

print("Start")

runTimer = StopWatch()

#testMission()

initialize() # pre run mandatories

""" startToRover()
grabWater()
scoreWater()
waterSample()
scoreSampleAndDrone() """
whiteGreenSamples()

print("time:", runTimer.time() / 1000, "s")