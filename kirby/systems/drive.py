# run.py
# 10/02/25 - chaBots Kirby
# Alfonso De Anda

# Stores all of the methods used for accurate driving in a class

from pybricks.tools import StopWatch, wait
from pybricks.parameters import Stop

from utils.pd import PDControl
from utils.constants import kPForward, kDForward, kPTurning, kDTurning, kPLine, kDLine, kDegreesInMM, kMinPower, kReflectionBlack, kReflectionWhite, kReflectionAvg, kDegreesBetweenSamples, kDegreesToStartScanning
from systems.colorScanning import ColorScanSystem

class DriveSystem:
    def __init__(self, hub, left_motor, right_motor, line_sensor=None, color_sensor = None):
        # Initialize motors and sensors
        self.hub = hub

        self.left = left_motor
        self.left.reset_angle(0)

        self.right = right_motor
        self.right.reset_angle(0)

        self.lineSensor = line_sensor
        self.colorSensor = color_sensor

        self.colorScan = ColorScanSystem(color_sensor)

        # Declare PD controllers

        self.straight_pid = PDControl(kPForward, kDForward)
        self.turn_pid = PDControl(kPTurning, kDTurning)
        self.line_pid = PDControl(kPLine, kDLine)

    # Returns average of position of the drive motors in degrees
    def getCurrentPos(self):
        pos = (abs(self.left.angle()) + abs(self.right.angle())) / 2
        return pos
    
    # Converts millimiters to degrees
    def getDegreesFromMilis(self, mm):
        return int(mm * kDegreesInMM)
    
    # Resets drive motors encoders
    def resetAngles(self):
        self.left.reset_angle(0)
        self.right.reset_angle(0)

    # Stop driving by time
    def brake(self, time):
        self.left.brake()
        self.right.brake()
        wait(time)
    
    # Method for straight driving using PD correction for heading and motion profile for speed control
    def straightDistance(self, distance, maxPower, targetAngle = -1, speedControl = True, ratio = 0.3, accel = True, decel = True):
        self.straight_pid.reset()
    
        self.resetAngles()

        # If there is not an specific heading, calculate error with the starting heading (default)
        if targetAngle == -1:
            targetAngle = self.hub.imu.heading()

        targetDegrees = abs(self.getDegreesFromMilis(distance))

        direction = 1 if distance >= 0 else -1

        accel_distance = targetDegrees * ratio
        decel_distance = targetDegrees * ratio if direction == 1 else targetDegrees * 0.6

        distanceRemaining = targetDegrees

        while distanceRemaining >= 0:
            currentAngle = self.hub.imu.heading()
            currentDegrees = self.getCurrentPos()
            distanceRemaining = targetDegrees - currentDegrees

            #Heading PD
            error = targetAngle - currentAngle
            correction = self.straight_pid.compute(error)

            #Trapezoidal speed control
            if speedControl == True and distance != 0:
                if currentDegrees < accel_distance and accel == True:
                    # Acceleration phase
                    basePower = kMinPower + ((currentDegrees / accel_distance) * (maxPower - (kMinPower-3)))
                elif distanceRemaining < decel_distance and decel == True:
                    # Deceleration phase
                    basePower = kMinPower + ((distanceRemaining / decel_distance) * (maxPower - (kMinPower-3)))
                else:
                    # Cruise phase
                    basePower = maxPower

                basePower = max(kMinPower, min(basePower, maxPower))  # clamp

                leftPower = direction * basePower + correction
                rightPower = direction * basePower - correction

                self.left.dc(leftPower)
                self.right.dc(rightPower)

            else:
                self.left.dc(direction * maxPower + correction)
                self.right.dc(direction * maxPower - correction)

            #wait(1)

        self.brake(10)

    # PD heading correction by ms
    def straightTime(self, time, power, targetAngle = -1):
        self.resetAngles()

        if targetAngle == -1:
            targetAngle = self.hub.imu.heading()
    
        self.straight_pid.reset()

        driveTimer = StopWatch()

        while driveTimer.time() < time:
            currentAngle = self.hub.imu.heading()

            error = targetAngle - currentAngle

            correction = self.straight_pid.compute(error)

            left = power + correction
            right = power - correction
            
            self.left.dc(left)
            self.right.dc(right)

        self.brake(10)

    # PD heading until black line detected
    def straightUntilReflection(self, targetReflection, power, sensor="line"):
        self.resetAngles()

        targetAngle = self.hub.imu.heading()
        
        self.straight_pid.reset()

        while True:
            currentAngle = self.hub.imu.heading()
            currentReflection = self.lineSensor.reflection()
            
            if sensor=="color":
                currentReflection = self.colorSensor.reflection()

            error = targetAngle - currentAngle

            correction = self.straight_pid.compute(error)

            self.left.dc(power + correction)
            self.right.dc(power - correction)

            if targetReflection < 50 and sensor=="line":
                if currentReflection < targetReflection:
                    self.hub.speaker.beep(100, 200)
                    break
            else:
                if currentReflection > targetReflection:
                    self.hub.speaker.beep(100, 200)
                    break

        self.brake(10)

    # Line following
    def trackLineDistance(self, distance, basePower, side=None):
        self.resetAngles()
        self.line_pid.reset()

        targetReflection = kReflectionAvg
        targetDegrees = abs(self.getDegreesFromMilis(distance))

        direction = 0
        if side is not None:
            if side == "right": direction = 1
            elif side == "left": direction = -1

        while abs(self.getCurrentPos()) < targetDegrees:
            currentReflection = self.lineSensor.reflection()

            # Compute PID correction
            error = targetReflection - currentReflection
            correction = self.line_pid.compute(error)

            # Compute left/right motor power
            leftPower = basePower + correction * direction
            rightPower = basePower - correction * direction

            # Normalize to avoid exceeding ±100 and preserve ratios
            maxVal = max(abs(leftPower), abs(rightPower), 100)
            leftPower = (leftPower / maxVal) * 100
            rightPower = (rightPower / maxVal) * 100

            # Apply motor power
            self.left.dc(leftPower)
            self.right.dc(rightPower)

        self.brake(10)

    def driveAndScan(self, distance, maxPower, scanningDistance = 500):
        self.resetAngles()
        self.straight_pid.reset()
        
        targetAngle = -90 #self.hub.imu.heading()
        
        direction = 1 if distance >= 0 else -1

        targetDegrees = abs(self.getDegreesFromMilis(distance))
        scanningDistance = abs(self.getDegreesFromMilis(scanningDistance))

        ratio = 0.2
        accel_distance = targetDegrees * ratio

        samplesPositions = []

        while True:
            currentAngle = self.hub.imu.heading()
            currentDegrees = self.getCurrentPos()
            distanceRemaining = targetDegrees - currentDegrees

            #end condition
            if distanceRemaining <= 0:
                break

            #scanning
            if currentDegrees >= kDegreesToStartScanning:
                distanceDetecting = (currentDegrees - kDegreesToStartScanning)

                if distanceDetecting % kDegreesBetweenSamples <= 10:
                    detectedColor = self.colorScan.scanCurrentColor(5)
                    samplesPositions.append(detectedColor)

                    self.hub.speaker.beep(1000, 100)
                    print(detectedColor)
                
                if distanceDetecting >= scanningDistance:
                    break

            #Heading PD
            error = targetAngle - currentAngle
            correction = self.straight_pid.compute(error)

            #accel decel
            if currentDegrees < accel_distance:
                basePower = kMinPower + ((currentDegrees / accel_distance) * (maxPower - kMinPower))
            elif distanceRemaining < accel_distance:
                basePower = kMinPower + ((distanceRemaining / accel_distance) * (maxPower - kMinPower))
            else:
                basePower = maxPower

            basePower = max(kMinPower, min(basePower, maxPower))  # clamp

            self.left.dc(direction * basePower + correction)
            self.right.dc(direction * basePower - correction)

        self.brake(10)
        return samplesPositions

    # PD turning method, use oneWheel parameter to specify the desired wheel to rotate
    def turnToAngle(self, targetAngle, power=75, oneWheel = "no", safeExitTime=1800):
        self.turn_pid.reset()
        angleDebounce = StopWatch()
        exitTimer = StopWatch()

        while True:
            currentAngle = self.hub.imu.heading()

            error = (targetAngle - currentAngle + 180) % 360 - 180

            correction = self.turn_pid.compute(error)

            correction = max(min(correction, power), -power)

            # Exit conditions
            if exitTimer.time() > safeExitTime:
                print("safe exit")
                break
            if abs(error) < 0.9:
                if angleDebounce.time() > 180:
                    print("successful turn")
                    break
            else:
                angleDebounce.reset()

            if abs(correction) < kMinPower and abs(error) > 1:
                correction = kMinPower if correction > 0 else -kMinPower

            # Apply correction normally
            if oneWheel == "left":
                self.left.dc(correction)
            elif oneWheel == "right":
                self.right.dc(-correction)
            else:
                self.left.dc(correction)
                self.right.dc(-correction)

            wait(1)

        self.brake(5)

    # Individual motor control

    def leftDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.left.run_angle(speed, degrees, then, wait)

    def leftTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.left.run_time(speed, time, then, wait)

    def rightDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.right.run_angle(speed, degrees, then, wait)

    def rightTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.right.run_time(speed, time, then, wait)