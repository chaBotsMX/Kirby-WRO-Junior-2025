# Junior_2025_Kirby.py
# 05/09/2025 for WRO RoboMission Junior team chaBots Kirby
# Alfonso De Anda

from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Axis, Side, Stop, Button, Color, Icon
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

import umath

MAX_LIGHT = 0
MIN_LIGHT = 100

VALUE_BLACK = 5
VALUE_WHITE = 36
VALUE_LINE = (VALUE_BLACK + VALUE_WHITE) / 2

KP_FORWARD = 10
KD_FORWARD = 0.1

KP_TURNING = 7
KD_TURNING = 0.1

DEGREES_PER_MM = 1.836398895222424634189340071693

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
        self.hub = PrimeHub()

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

    def getDegreesFromMilis(self, mm):
        return int(mm * DEGREES_PER_MM)

    def driveDegrees(self, distance, maxPower, targetAngle = -1, speedControl = True, ratio = 0.3, accel = True, decel = True):
        kP = KP_FORWARD
        kD = KD_FORWARD

        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        if targetAngle == -1:
            targetAngle = self.hub.imu.heading()
        
        lastError = 0
        watch = StopWatch()

        direction = 1 if distance >= 0 else -1

        targetDegrees = abs(self.getDegreesFromMilis(distance))

        minPower = 35
        accel_distance = targetDegrees * ratio  # 30% of the total distance for accel/decel

        while True:
            currentAngle = self.hub.imu.heading()
            currentDegrees = self.getCurrentPos()
            distanceRemaining = targetDegrees - currentDegrees

            if distanceRemaining <= 0:
                break

            #Heading PD
            error = targetAngle - currentAngle
            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            correction = (error * kP) + (derivative * kD)
            watch.reset()
            lastError = error

            #Trapezoidal speed control
            if speedControl == True:
                if currentDegrees < accel_distance and accel == True:
                    # Acceleration phase
                    basePower = minPower + ((currentDegrees / accel_distance) * (maxPower - minPower))
                elif distanceRemaining < accel_distance and decel == True:
                    # Deceleration phase
                    basePower = minPower + ((distanceRemaining / accel_distance) * (maxPower - minPower))
                else:
                    # Cruise phase
                    basePower = maxPower

                basePower = max(minPower, min(basePower, maxPower))  # clamp

                self.leftDriveMotor.dc(direction * basePower + correction)
                self.rightDriveMotor.dc(direction * basePower - correction)

            else:
                self.leftDriveMotor.dc(direction * maxPower + correction)
                self.rightDriveMotor.dc(direction * maxPower - correction)


            #wait(1)

        self.brake(10)

    def driveTime(self, time, power, targetAngle = -1):
        kP = KP_FORWARD
        kD = KD_FORWARD

        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        if targetAngle == -1:
            targetAngle = self.hub.imu.heading()
    
        lastError = 0
        watch = StopWatch()

        timer = StopWatch()

        while True:
            currentAngle = self.hub.imu.heading()
            currentReflection = self.lineSensor.reflection()

            error = targetAngle - currentAngle

            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (derivative * kD)

            lastError = error

            self.leftDriveMotor.dc(power + correction)
            self.rightDriveMotor.dc(power - correction)

            if timer.time() > time:
                break

            wait(1)

        self.brake(10)
        wait(10)

    def driveUntilReflection(self, targetReflection, power, sensor="line"):
        kP = KP_FORWARD
        kD = KD_FORWARD

        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        targetAngle = self.hub.imu.heading()
        lastError = 0
        watch = StopWatch()

        while True:
            currentAngle = self.hub.imu.heading()
            currentReflection = self.lineSensor.reflection()
            if sensor=="color":
                currentReflection = self.colorSensor.reflection()

            error = targetAngle - currentAngle
            errorReflection = targetReflection - currentReflection

            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (derivative * kD)

            lastError = error

            self.leftDriveMotor.dc(power + correction)
            self.rightDriveMotor.dc(power - correction)

            if targetReflection < 50 and sensor=="line":
                if currentReflection < targetReflection:
                    self.hub.speaker.beep(100, 200)
                    break
            else:
                if currentReflection > targetReflection:
                    self.hub.speaker.beep(100, 200)
                    break

            wait(1)

        self.brake(10)
        wait(10)

    def driveAndScan(self, distance, maxPower, ratio, targetAngle = -1, distanceToFirstDetection = 410, scanningDistance = 400):
        kP = KP_FORWARD
        kD = KD_FORWARD

        distanceBetweenSamples = 175

        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        if targetAngle == -1:
            targetAngle = self.hub.imu.heading()
        
        lastError = 0
        watch = StopWatch()

        direction = 1 if distance >= 0 else -1

        targetDegrees = abs(self.getDegreesFromMilis(distance))
        scanningDistance = abs(self.getDegreesFromMilis(scanningDistance))

        minPower = 35
        accel_distance = targetDegrees * ratio

        while True:
            currentAngle = self.hub.imu.heading()
            currentDegrees = self.getCurrentPos()
            distanceRemaining = targetDegrees - currentDegrees

            #end condition
            if distanceRemaining <= 0:
                break

            #scanning
            if currentDegrees >= distanceToFirstDetection:
                space = (currentDegrees - distanceToFirstDetection)

                if space % distanceBetweenSamples <= 10:
                    detectedColor = self.scanCurrentColor(8)
                    samples.append(detectedColor)
                    self.hub.speaker.beep(1000, 100)
                    print(detectedColor)
                
                if space >= scanningDistance:
                    break


            #Heading PD
            error = targetAngle - currentAngle
            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            correction = (error * kP) + (derivative * kD)
            watch.reset()
            lastError = error

            #accel decel
            if currentDegrees < accel_distance:
                basePower = minPower + ((currentDegrees / accel_distance) * (maxPower - minPower))
            elif distanceRemaining < accel_distance:
                basePower = minPower + ((distanceRemaining / accel_distance) * (maxPower - minPower))
            else:
                basePower = maxPower

            basePower = max(minPower, min(basePower, maxPower))  # clamp

            self.leftDriveMotor.dc(direction * basePower + correction)
            self.rightDriveMotor.dc(direction * basePower - correction)

        self.brake(10)

    def turnInPlace(self, targetAngle, power=75, oneWheel = "no"):
        kP=KP_TURNING
        kD=KD_TURNING

        lastError = 0
        watch = StopWatch()
        angleDebounce = StopWatch()
        exitTimer = StopWatch()
        minPower = 32

        while True:
            currentAngle = self.hub.imu.heading()

            error = (targetAngle - currentAngle + 180) % 360 - 180

            dt = watch.time() / 1000
            derivative = (error - lastError) / dt if dt > 0 else 0
            watch.reset()
            lastError = error

            correction = (error * kP) + (kD * derivative)
            correction = max(min(correction, power), -power)

            if abs(correction) < minPower and abs(error) > 1:
                correction = minPower if correction > 0 else -minPower

            # Apply correction normally
            if oneWheel == "left":
                self.leftDriveMotor.dc(correction)
            elif oneWheel == "right":
                self.rightDriveMotor.dc(-correction)
            else:
                self.leftDriveMotor.dc(correction)
                self.rightDriveMotor.dc(-correction)

            # Exit conditions
            if exitTimer.time() > 3000:
                print("safe exit")
                break
            if abs(error) < 1:
                if angleDebounce.time() > 200:
                    #print("successful turn")
                    break
            else:
                angleDebounce.reset()

            wait(1)

        self.brake(5)

    def brake(self, time):
        self.leftDriveMotor.brake()
        self.rightDriveMotor.brake()
        wait(time)

    def scanCurrentColor(self, iterations):
        h_total = 0
        s_total = 0
        v_total = 0

        for i in range(iterations):
            h = self.colorSensor.hsv().h
            s = self.colorSensor.hsv().s
            v = self.colorSensor.hsv().v

            h_total += h
            s_total += s
            v_total += v
            wait(1)

        h_avg = h_total / iterations
        s_avg = s_total / iterations
        v_avg = v_total / iterations

        print("H ", h_avg, " S ", s_avg, " V ", v_avg)

        if (h_avg >= 330 or h_avg <= 30) and s_avg > 20:
            return("red")
            #print("red")
            #self.hub.speaker.beep(100, 100)
            #samples.append("red")

        elif 40 <= h_avg <= 70 and s_avg > 30:
            return("yellow")

        elif 100 <= h_avg <= 170 and s_avg > 30:
            return("green")

        #elif (h_avg < 50 or s_avg <= 12) and v_avg < 2:
        elif v_avg < 2:
            return("blank")

        else:
            return("white")

    def waitUntilButton(self):
        while not Button.RIGHT in self.hub.buttons.pressed():
            self.brake(0)            

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