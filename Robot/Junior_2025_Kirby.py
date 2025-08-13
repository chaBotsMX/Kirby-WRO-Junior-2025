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

    def driveDegrees(self, distance, maxPower, kP = KP_FORWARD, kD = KD_FORWARD, targetAngle = -1, speedControl = True, accel = True, decel = True, scanColors = False):
        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        if targetAngle == -1:
            targetAngle = self.hub.imu.heading()
        
        lastError = 0
        watch = StopWatch()

        direction = 1 if distance >= 0 else -1

        targetDegrees = abs(self.getDegreesFromMilis(distance))

        minPower = 35
        accel_distance = targetDegrees * 0.3  # 30% of the total distance for accel/decel

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

            print("pos ", currentDegrees)

            if scanColors == True and currentDegrees > 400:
                space = currentDegrees - 400
                print("space ", space)
                if space < 900 and ((space % 180 > 0 and space % 180 < 16) or (space % 180 < 180 and space % 180 > 164) or (space < 20)):
                    print("READINGGGGGGGGGG")
                    detectedColor = self.scanCurrentColor(20)
                    samples.append(detectedColor)
                    print("color ", detectedColor)

            #wait(1)

        self.brake(10)
        print(samples)

    def driveTime(self, time, power, kP = KP_FORWARD, kD = KD_FORWARD, targetAngle = -1):
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

            if targetReflection < 50:
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

    def turnInPlace (self, angle, power = 75, kP = KP_TURNING, kD = KD_TURNING):
        targetAngle = angle

        lastError = 0

        watch = StopWatch()
        angleDebounce = StopWatch()
        exitTimer = StopWatch()

        minPower = 32

        while True:
            currentAngle = self.hub.imu.heading()
            error = targetAngle - currentAngle

            dt = watch.time() / 1000
            derivative = (error - lastError) /dt if dt > 0 else 0
            watch.reset()

            correction = (error * kP) + (kD * derivative)

            correction = max(min(correction, power), -power)

            if abs(correction) < minPower and abs(error) > 1:
                if correction > 0:
                    correction = minPower
                else:
                    correction = -minPower

            lastError = error

            #print("angle", currentAngle)
            #print("error", error)
            #print("correction", correction)
            #print("time", angleDebounce.time())

            self.leftDriveMotor.dc(correction)
            self.rightDriveMotor.dc(-correction)

            if exitTimer.time() > 3000:
                print("safe exit")
                break;
            
            if abs(error) < 1:
                if(angleDebounce.time() > 200):
                    print("succesfull turn")
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

        elif (h_avg < 50 or s_avg <= 12) and v_avg < 2:
            return("blank")

        else:
            return("white")

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

        elif (h_avg < 50 or s_avg <= 12) and v_avg < 2:
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