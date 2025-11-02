from robot import Robot

kirby = Robot()

def testMission():
    print(kirby.hub.battery.voltage(), "mv")

    """ while True:
        print(kirby.line_sensor.reflection()) """
    kirby.drive.trackLineDistance(5000, 40, side="left")