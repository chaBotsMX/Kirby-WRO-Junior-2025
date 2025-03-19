from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Axis, Side, Stop, Button, Color, Icon
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

MAX_LIGHT = 0
MIN_LIGHT = 100

VALUE_BLACK = 5
VALUE_WHITE = 36
VALUE_LINE = (VALUE_BLACK + VALUE_WHITE) / 2

class Kirby:
    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.X, front_side=-Axis.Y)

        self.leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self.leftDriveMotor.reset_angle(0)
        #self.leftDriveMotor.control.limits()

        self.rightDriveMotor = Motor(Port.A, Direction.CLOCKWISE)
        self.rightDriveMotor.reset_angle(0)
        #self.rightDriveMotor.control.limits()

        self.backMotor = Motor(Port.B, Direction.CLOCKWISE)
        self.backMotor.reset_angle(0)
        #self.backMotor.control.limits()

        self.frontMotor = Motor(Port.D, Direction.CLOCKWISE)
        self.frontMotor.reset_angle(0)
        #self.frontMotor.control.limits()

        self.lineSensor = ColorSensor(Port.C)
        self.colorSensor = ColorSensor(Port.F)

        Color.WHITE = Color(h=0, s=5, v=19)
        Color.RED = Color(h=354, s=93, v=7)
        Color.YELLOW = Color(h=47, s=69, v=22)
        Color.GREEN = Color(h=150, s=64, v=5)
        Color.NONE = Color(h=0, s=0, v=0)

        self.sensorColors = (Color.WHITE, Color.RED, Color.YELLOW, Color.GREEN, Color.NONE)

        self.colorSensor.detectable_colors(self.sensorColors)

    def getCurrentPos(self):
        pos = (abs(self.leftDriveMotor.angle()) + abs(self.rightDriveMotor.angle())) / 2
        return pos

    def getAngle(self, heading):
        return (heading + 180) % 360 - 180

    def driveStraightDegrees(self, targetDegrees, power, kP, kD):
        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        targetAngle = self.hub.imu.heading()
        lastError = 0
        watch = StopWatch()
        while True:
            currentAngle = self.hub.imu.heading()
            currentDegrees = self.getCurrentPos()

            error = targetAngle - currentAngle
            errorDegrees = targetDegrees - currentDegrees

            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (derivative * kD)

            #correction = max(min(correction, 100), -100)

            lastError = error

            self.leftDriveMotor.dc(power + correction)
            self.rightDriveMotor.dc(power - correction)

            print(abs(currentDegrees - targetDegrees))
            print("left", self.leftDriveMotor.angle())
            print("right", self.rightDriveMotor.angle())
            print("average", self.getCurrentPos())

            if currentDegrees > targetDegrees:
                break

            wait(1)

        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()
        wait(10)

    def driveStraightTime(self, time, power):
        self.leftDriveMotor.dc(power)
        self.rightDriveMotor.dc(power)
        wait(time)
        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()
        wait(10)

    def driveStraightUntilReflection(self, targetReflection, power, kP, kD):
        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        targetAngle = self.hub.imu.heading()
        lastError = 0
        watch = StopWatch()

        while True:
            currentAngle = self.hub.imu.heading()
            currentReflection = self.lineSensor.reflection()

            error = targetAngle - currentAngle
            errorReflection = targetReflection - currentReflection

            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (derivative * kD)

            #correction = max(min(correction, 100), -100)

            lastError = error

            self.leftDriveMotor.dc(power + correction)
            self.rightDriveMotor.dc(power - correction)

            print(abs(currentReflection - targetReflection))
            print("left", self.leftDriveMotor.angle())
            print("right", self.rightDriveMotor.angle())
            print("average", self.getCurrentPos())

            if currentReflection < targetReflection:
                break

            wait(1)

        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()
        wait(10)

    def turnInPlace (self, angle, power, kP, kD, timeLimit=1500):
        targetAngle = angle

        lastError = 0

        watch = StopWatch()

        watch2 = StopWatch()

        while True:
            #currentAngle = self.getAngle(self.hub.imu.heading())
            currentAngle = self.hub.imu.heading()
            error = targetAngle - currentAngle

            dt = watch.time() / 1000
            derivative = (error - lastError) /dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (kD * derivative)
            #correction = (error * kP)

            correction = max(min(correction, power), -power)

            lastError = error

            self.leftDriveMotor.dc(correction)
            self.rightDriveMotor.dc(-correction)

            print("error", error)
            print("correction", correction)
            print("current angle", currentAngle)
            print("target", targetAngle)
            print("time", watch2.time())
            print('\n')

            if watch2.time() > timeLimit:
                print("time limit exceeded", watch2.time())
                break

            if abs(error) < 0.1:
                print("correction made succesfully")
                break

            wait(1)

        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()
        wait(10)

    def lineFollowDegrees(self, targetDegrees, power, kP, kD):
        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        targetReflection = VALUE_LINE
        lastError = 0
        watch = StopWatch()

        while True:
            currentReflection = self.lineSensor.reflection()
            currentDegrees = self.getCurrentPos()

            error = currentReflection - targetReflection

            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (kD * derivative)

            correction = max(min(correction, 100), -100)

            lastError = error

            self.leftDriveMotor.dc(power - correction)
            self.rightDriveMotor.dc(power + correction)

            if currentDegrees > targetDegrees:
                break

            wait(1)

        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()

    def moveLeftDriveMotorDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.leftDriveMotor.run_angle(speed, degrees, then, wait)

    def moveLeftDriveMotorTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.leftDriveMotor.run_time(speed, time, then, wait)


    def moveRightDriveMotorDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.rightDriveMotor.run_angle(speed, degrees, then, wait)

    def moveRightDriveMotorTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.rightDriveMotor.run_time(speed, time, then, wait)


    def moveBackMotorDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.backMotor.run_target(speed, degrees, then, wait)

    def moveBackMotorTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.backMotor.run_time(speed, time, then, wait)


    def moveFrontMotorDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.frontMotor.run_target(speed, degrees, then, wait)

    def moveFrontMotorTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.frontMotor.run_time(speed, time, then, wait)