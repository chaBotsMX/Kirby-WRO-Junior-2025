# run.py
# 11/02/25 - chaBots Kirby
# Alfonso De Anda

# Robot run

from missions.secondday2011 import *
from pybricks.tools import StopWatch

print("Start")

runTimer = StopWatch()

roberydron()
blancaAmarilla()
roja()
blanca()
irAInicio()
dron2()
blacksamples()
last()



print("time:", runTimer.time() / 1000, "s")