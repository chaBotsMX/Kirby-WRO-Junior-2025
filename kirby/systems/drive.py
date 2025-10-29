from pybricks.tools import StopWatch, wait
from pybricks.parameters import Stop

from utils.pd import PDControl
from utils.constants import kPForward, kDForward, kPTurning, kDTurning, kDegreesInMM, kMinPower

class DriveSystem:
    def __init__(self, hub, left_motor, right_motor, line_sensor=None, color_sensor = None):
        self.hub = hub

        self.left = left_motor
        self.left.reset_angle(0)

        self.right = right_motor
        self.right.reset_angle(0)

        self.lineSensor = line_sensor
        self.colorSensor = color_sensor

        self.straight_pid = PDControl(kPForward, kDForward)
        self.turn_pid = PDControl(kPTurning, kDTurning)

    def getCurrentPos(self):
        pos = (abs(self.left.angle()) + abs(self.right.angle())) / 2
        return pos
    
    def getDegreesFromMilis(self, mm):
        return int(mm * kDegreesInMM)
    
    def resetAngles(self):
        self.left.reset_angle(0)
        self.right.reset_angle(0)

    def brake(self, time):
        self.left.brake()
        self.right.brake()
        wait(time)
    
    def straightDistance(self, distance, maxPower, targetAngle = -1, speedControl = True, ratio = 0.3, accel = True, decel = True):
        self.straight_pid.reset()
    
        self.resetAngles()

        if targetAngle == -1:
            targetAngle = self.hub.imu.heading()

        targetDegrees = abs(self.getDegreesFromMilis(distance))

        direction = 1 if distance >= 0 else -1

        accel_distance = targetDegrees * ratio  # 30% of the total distance for accel/decel

        minPower = kMinPower

        distanceRemaining = targetDegrees

        while distanceRemaining >= 0:
            currentAngle = self.hub.imu.heading()
            currentDegrees = self.getCurrentPos()
            distanceRemaining = targetDegrees - currentDegrees

            #Heading PD
            error = targetAngle - currentAngle
            correction = self.straight_pid.compute(error)

            #Trapezoidal speed control
            if speedControl == True:
                if currentDegrees < accel_distance and accel == True:
                    # Acceleration phase
                    basePower = kMinPower + ((currentDegrees / accel_distance) * (maxPower - kMinPower))
                elif distanceRemaining < accel_distance and decel == True:
                    # Deceleration phase
                    basePower = kMinPower + ((distanceRemaining / accel_distance) * (maxPower - kMinPower))
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

    def turnToAngle(self, targetAngle, power=75, oneWheel = "no"):
        self.turn_pid.reset()
        angleDebounce = StopWatch()
        exitTimer = StopWatch()

        while True:
            currentAngle = self.hub.imu.heading()

            error = (targetAngle - currentAngle + 180) % 360 - 180

            correction = self.turn_pid.compute(error)

            correction = max(min(correction, power), -power)

            # Exit conditions
            if exitTimer.time() > 3000:
                print("safe exit")
                break
            if abs(error) < 0.8:
                if angleDebounce.time() > 200:
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

    def leftDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.left.run_angle(speed, degrees, then, wait)

    def leftTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.left.run_time(speed, time, then, wait)

    def rightDegrees(self, degrees, speed, then = Stop.HOLD, wait = True):
        self.right.run_angle(speed, degrees, then, wait)

    def rightTime(self, time, speed, then = Stop.HOLD, wait = True):
        self.right.run_time(speed, time, then, wait)