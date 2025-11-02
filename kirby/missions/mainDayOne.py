from robot import Robot
from utils.constants import kReflectionBlack, kBackMotorWaterPosition

kirby = Robot()

def testMission():
    print(kirby.hub.battery.voltage(), "mv")
    while True:
        print(kirby.back_motor.angle())
    
def initialize():
    print(kirby.hub.battery.voltage(), "mv")

def startToRover():
    kirby.drive.straightTime(300, -50)
    kirby.hub.imu.reset_heading(0) #choca y resetea imu

    """
    kirby.drive.straightDistance(170, 80)
    kirby.drive.turnToAngle(-60)
    kirby.drive.straightDistance(140, 80)
    kirby.drive.straightUntilReflection(kReflectionBlack, 40)
    kirby.drive.straightDistance(40, 30)

    kirby.drive.turnToAngle(0)
    kirby.mechanisms.moveBackMotorDegrees(20, 300)
    kirby.drive.trackLineDistance(80, 40, side="left")
    #kirby.drive.straightDistance(80, 60)
    kirby.mechanisms.moveBackMotorDegrees(0, 500)
    """

    kirby.drive.turnToAngle(-35, oneWheel="right")
    kirby.drive.straightDistance(330, 80)
    #kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    #kirby.drive.straightDistance(100, 60)
    kirby.drive.straightUntilReflection(kReflectionBlack, 30)
    kirby.drive.straightDistance(45, 30)
    kirby.drive.turnToAngle(0)
    kirby.mechanisms.moveBackMotorDegrees(40, 300)
    kirby.drive.straightDistance(30, 60)
    #kirby.drive.trackLineDistance(30, 50, side="left")
    kirby.mechanisms.moveBackMotorDegrees(0, 500)

def grabWater():
    kirby.drive.straightDistance(-120, 80, targetAngle=0)
    kirby.mechanisms.moveBackMotorDegrees(kBackMotorWaterPosition, 400)

    kirby.drive.straightTime(400, -70, targetAngle=0)
    kirby.drive.straightDistance(35, 60, targetAngle=0) #primer pelota
    kirby.drive.brake(100)
    kirby.drive.straightTime(500, -70, targetAngle=0)
    kirby.drive.straightDistance(95, 50, targetAngle=0) #segunda pelota
    kirby.mechanisms.moveBackMotorDegrees(170, 300)

def goToWaterBox():
    kirby.drive.turnToAngle(-90, power=40)
    kirby.drive.straightDistance(400, 85)
    kirby.drive.turnToAngle(-180, power=35)
    kirby.drive.straightDistance(145, 75)
    #kirby.drive.straightTime(400, 50)
    kirby.drive.brake(400)

    kirby.mechanisms.moveBackMotorDegrees(100, 300)