# run.py
# 11/02/25 - chaBots Kirby
# Alfonso De Anda

# Robot run

from missions.secondDay0811 import todoaki

from pybricks.tools import StopWatch

print("Start")

runTimer = StopWatch()

todoaki()

print("time:", runTimer.time() / 1000, "s")