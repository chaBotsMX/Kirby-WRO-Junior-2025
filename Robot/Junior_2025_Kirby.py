from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Axis, Side, Stop, Button, Color, Icon
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

import umath

MAX_LIGHT = 0
MIN_LIGHT = 100

VALUE_BLACK = 5
VALUE_WHITE = 36
VALUE_LINE = (VALUE_BLACK + VALUE_WHITE) / 2

KP_FORWARD = 6.5 #6
KD_FORWARD = 0.01

KP_TURNING = 11       #12
KD_TURNING = 0.5

samples = []

DETECTION_INTERVAL = 900

CLAW_DEFAULT = 60
CLAW_THREE = 90

isRedFirst = False

areSamplesInOrder = False

clawPositionToSamples = CLAW_DEFAULT

samplesState = 0

POSITION_TO_RED = 135
POSITION_TO_YELLOW = 135

frontPositionToSamples = POSITION_TO_RED

class Kirby:
    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.X, front_side=-Axis.Y)

        self.leftDriveMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.leftDriveMotor.reset_angle(0)
        #self.leftDriveMotor.control.limits()

        self.rightDriveMotor = Motor(Port.E, Direction.CLOCKWISE)
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

    def getCurrentPos(self):
        pos = (abs(self.leftDriveMotor.angle()) + abs(self.rightDriveMotor.angle())) / 2
        return pos

    def getAngle(self, heading):
        return (heading + 180) % 360 - 180

    def driveDegrees(self, targetDegrees, power, kP = KP_FORWARD, kD = KD_FORWARD):
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

            lastError = error

            self.leftDriveMotor.dc(power + correction)
            self.rightDriveMotor.dc(power - correction)

            if currentDegrees > targetDegrees:
                break

            wait(1)

        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()
        wait(10)

    '''
    def driveDegrees(self, targetDegrees, maxPower, accel=20, basePower = 22, kP=KP_FORWARD, kD=KD_FORWARD):
        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        # Get the initial heading for PD correction
        targetAngle = self.hub.imu.heading()
        lastError = 0
        watch = StopWatch()

        # (1 for forward, -1 for backward)
        direction = 1 if targetDegrees >= 0 else -1
        targetDegrees = abs(targetDegrees)  # Work with positive distance for math

        # Formula: s = v² / (2a), from kinematics
        accelDistance = decelDistance = (maxPower * maxPower) / (2 * accel)

        cruiseDistance = max(0, targetDegrees - accelDistance - decelDistance)

        while True:
            currentAngle = self.hub.imu.heading()
            currentDegrees = abs(self.getCurrentPos())
            remainingDegrees = targetDegrees - currentDegrees

            print("curr degs", currentDegrees)
            print("acc dist", accelDistance)

            # speed based on position in the motion profile
            if currentDegrees < accelDistance:
                # acceleration: v = sqrt(2as)
                currentPower = basePower + umath.sqrt(2 * accel * (currentDegrees+1))
            elif currentDegrees < accelDistance + cruiseDistance:
                # cruise: constant max power
                currentPower = maxPower
            else:
                # deceleration: v = sqrt(2a * remaining distance)
                currentPower = basePower + umath.sqrt(2 * accel * max(remainingDegrees, 0))

            currentPower = min(currentPower, maxPower)

            print("curr pow", currentPower)

            # PD control
            error = self.getAngle(targetAngle - currentAngle)
            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (derivative * kD)
            lastError = error

            # Apply motor powers, considering direction
            self.leftDriveMotor.dc(direction * currentPower + correction)
            self.rightDriveMotor.dc(direction * currentPower - correction)

            # Exit when target distance is reached
            if currentDegrees >= targetDegrees:
                break

            wait(1)  # 1 ms delay to prevent overloading the CPU

        # Stop motors
        self.brake(10)
    '''

    def driveDegreesAccelDecel(self, targetDegrees, maxPower, accel=10, basePower=30, kP=KP_FORWARD, kD=KD_FORWARD):
        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        # Get the initial heading for PD correction
        targetAngle = self.hub.imu.heading()
        lastError = 0
        watch = StopWatch()

        # Direction of movement: 1 for forward, -1 for backward
        direction = 1 if targetDegrees >= 0 else -1
        targetDegrees = abs(targetDegrees)

        # Ratios for profile shape
        accelRatio = 0.3
        decelRatio = 0.5
        cruiseRatio = 1 - accelRatio - decelRatio

        # Calculate raw accel/decel distances
        accelDistance = targetDegrees * accelRatio
        decelDistance = targetDegrees * decelRatio

        # Minimum distances to ensure effectiveness
        minAccelDistance = 30
        minDecelDistance = 30

        accelDistance = max(minAccelDistance, accelDistance)
        decelDistance = max(minDecelDistance, decelDistance)

        # Scale down if accel+decel > total
        totalAD = accelDistance + decelDistance
        if totalAD > targetDegrees:
            scale = targetDegrees / totalAD
            accelDistance *= scale
            decelDistance *= scale

        cruiseDistance = max(0, targetDegrees - accelDistance - decelDistance)

        while True:
            currentAngle = self.hub.imu.heading()
            currentDegrees = abs(self.getCurrentPos())
            remainingDegrees = targetDegrees - currentDegrees

            #print("curr degs", currentDegrees)
            #print("acc dist", accelDistance)

            # Compute power based on position in motion profile
            if currentDegrees < accelDistance:
                # Accelerating: v = basePower + sqrt(2as)
                currentPower = basePower + umath.sqrt(2 * accel * currentDegrees)
            elif currentDegrees < accelDistance + cruiseDistance:
                # Cruising at maxPower
                currentPower = maxPower
            else:
                # Decelerating: v = basePower + sqrt(2a * remaining)
                currentPower = (basePower-10) + umath.sqrt(2 * accel * max(remainingDegrees, 0))

            # Clamp to max power
            currentPower = min(currentPower, maxPower)

            #print("curr pow", currentPower)

            # PD correction
            error = self.getAngle(targetAngle - currentAngle)
            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (derivative * kD)
            lastError = error

            # Apply power with correction and direction
            self.leftDriveMotor.dc(direction * currentPower + correction)
            self.rightDriveMotor.dc(direction * currentPower - correction)

            # Exit condition
            if currentDegrees >= targetDegrees:
                break

            wait(1)  # small delay

        self.brake(10)

    def driveTime(self, time, power):
        self.leftDriveMotor.dc(power)
        self.rightDriveMotor.dc(power)

        wait(time)

        self.brake(10)

    def driveUntilReflection(self, targetReflection, power, kP = KP_FORWARD, kD = KD_FORWARD):
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

            lastError = error

            self.leftDriveMotor.dc(power + correction)
            self.rightDriveMotor.dc(power - correction)

            if currentReflection < targetReflection:
                self.hub.speaker.beep(400, 200)
                break

            wait(1)

        self.brake(10)
        wait(10)

    def turnInPlace (self, angle, power = 60, kP = KP_TURNING, kD = KD_TURNING, timeLimit=1000):
        targetAngle = angle

        lastError = 0

        watch = StopWatch()
        watch2 = StopWatch()
        angleDebounce = StopWatch()

        time = 0

        while True:
            currentAngle = self.hub.imu.heading()
            error = targetAngle - currentAngle

            dt = watch.time() / 1000
            derivative = (error - lastError) /dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (kD * derivative)

            correction = max(min(correction, power), -power)

            lastError = error

            '''
            print("angle", currentAngle)
            print("error", error)
            print("time", time)
            '''

            self.leftDriveMotor.dc(correction)
            self.rightDriveMotor.dc(-correction)

            #if abs(error) < 3:
                #kP *= 1.05

            if watch2.time() > timeLimit:
                print("time limit exceeded", watch2.time())
                break

            if abs(error) < 0.1:
                if(angleDebounce.time() > 100):
                    print("correction made succesfully")
                    break
                else:
                    angleDebounce.reset()

            wait(1)

        self.brake(10)
        wait(10)

    def brake(self, time):
        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()
        wait(time)

    def determineSamples(self):
        h_total = 0
        s_total = 0
        v_total = 0

        for i in range(10):
            h = self.colorSensor.hsv().h
            s = self.colorSensor.hsv().s
            v = self.colorSensor.hsv().v

            h_total += h
            s_total += s
            v_total += v
            wait(10)

        h_avg = h_total / 10
        s_avg = s_total / 10
        v_avg = v_total / 10

        print("HSV Avg:", h_avg, s_avg, v_avg)

        if (h_avg >= 330 or h_avg <= 30) and s_avg > 20:
            print("red")
            self.hub.speaker.beep(100, 100)
            samples.append("red")

        elif 40 <= h_avg <= 70 and s_avg > 30:
            print("yellow")
            self.hub.speaker.beep(300, 100)
            samples.append("yellow")

        elif 100 <= h_avg <= 170 and s_avg > 30:
            print("green")
            self.hub.speaker.beep(400, 100)
            samples.append("green")

        elif h_avg < 5 and s_avg < 5 and v_avg < 5:
            print("blank")
            self.hub.speaker.beep(500, 100)
            self.hub.speaker.beep(500, 100)
            samples.append("blank")

        else:
            print("white")
            self.hub.speaker.beep(200, 100)
            samples.append("white")


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