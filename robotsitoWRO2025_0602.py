from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop, Button, Color
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()

line_sensor = ColorSensor(Port.C)
color_sensor = ColorSensor(Port.E)

left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
colita = Motor(Port.A, Direction.CLOCKWISE)
separador = Motor(Port.F, Direction.CLOCKWISE)

drive_base = DriveBase(left, right, 62.4, 150)

elapsedTime = StopWatch()

Color.WHITE = Color(h=0, s=5, v=19)
Color.RED = Color(h=354, s=93, v=7)
Color.YELLOW = Color(h=47, s=69, v=22)
Color.GREEN = Color(h=150, s=64, v=5)
Color.NONE = Color(h=0, s=0, v=0)

my_colors = (Color.WHITE, Color.RED, Color.YELLOW, Color.GREEN, Color.NONE)

color_sensor.detectable_colors(my_colors)

garritaSubir = -250
garritaBajar = 250

SENSOR_BLACK = 14

def robotSetup():
    print('UPLOADED |', 'BATTERY VOLTAGE: ', prime_hub.battery.voltage())
    if prime_hub.battery.voltage() >= 8200:
        print('OVERPOWER')
    elif prime_hub.battery.voltage() >= 7600 and prime_hub.battery.voltage() <= 8200:
        print('OK')
    else:
        print('LOW BATTERY')
       # raise SystemExit


    left.reset_angle(0)
    right.reset_angle(0)
    separador.reset_angle(0)
    prime_hub.imu.reset_heading(0)
    drive_base.settings(straight_speed=700)
    while not Button.LEFT in prime_hub.buttons.pressed():
        wait(1)


def line_follow(targetTicks, speed, leftOrRight):
    left.reset_angle()
    right.reset_angle()

    kP = 0.4
    kI = 0.0
    kD = 0.0
    
    lastError = 0
    integral = 0
    while True:
        currentTicks = (left.angle() + right.angle()) / 2
        error = line_sensor.reflection() - SENSOR_BLACK

        #print(currentTicks)

        p = error * kP
        integral += error
        i = integral * kI
        derivative = error - lastError
        lastError = error
        d = derivative * kD
        correction = p + i + d

        if leftOrRight == 1:
            left.dc(speed + correction)
            right.dc(speed - correction)
        elif leftOrRight == 2:
            left.dc(speed - correction)
            right.dc(speed + correction)

        if currentTicks >= targetTicks:
            break

    stop_motors()
    wait(100)

def get_robot_angle():
    angle = prime_hub.imu.heading()
    #if angle >= 180:
    #    angle -= 360
    #if angle <= -180:
    #    angle += 360
    return angle

def turn_to_angle(targetAngle, maxSpeed, maxTime):
    elapsedTime.reset()
    kP = 6.5
    kI = 0.0
    kD = 0.0
    
    lastError = 0
    integral = 0

    while True:
        currentAngle = get_robot_angle()

        error =  targetAngle - currentAngle
        #print("error", error)

        p = error * kP
        #print("p", p)
        integral += error
        i = integral * kI
        derivative = error - lastError
        lastError = error
        d = derivative * kD
        correction = p + i + d
        correction = max(-maxSpeed, min(correction, maxSpeed))

        left.dc(correction)
        right.dc(-correction)

        #print("correccion", correction)

        if elapsedTime.time() > maxTime:
            break
    stop_motors()
    wait(100)

def forwardUntilBlack(power):
    while not line_sensor.reflection() <= 50:
        print(line_sensor.reflection())
        drive_base.drive(power, 0)

def stop_motors():
    left.brake()
    right.brake()

def inicio():
    drive_base.straight(385)
    turn_to_angle(-90, 80, 1000)
    forwardUntilBlack(200)

    stop_motors()
    wait(50)

    #line_follow(465, 50, 2)

    drive_base.straight(120)

def rover():
    turn_to_angle(-180, 75, 1500)
    drive_base.straight(-150)
    colita.run_angle(400, 85)
    drive_base.straight(210)

def roverToSamples():
    turn_to_angle(-90, 80, 1500)
    #line_follow(1000, 50, 1)
    forwardUntilBlack(200)
    drive_base.straight(100)
    turn_to_angle(-20, 80, 1500)
    forwardUntilBlack(300)

    stop_motors()
    wait(50)

    turn_to_angle(0, 80, 500)

    drive_base.settings(straight_speed=100)
    drive_base.straight(125)
    colita.run_angle(300, -89)
    '''
    turn_to_angle(90, 80, 1500)
    drive_base.straight(-200)
    '''
    right.run_angle(1200,-1000)

def takeWater():
    turn_to_angle(-90, 80, 1000)
    drive_base.straight(-85)
    turn_to_angle(0, 80, 2000)

    colita.run_angle(300, 10)

    drive_base.straight(-250)
    drive_base.straight(150)

    drive_base.straight(-150)
    drive_base.straight(140)

    colita.run_angle(300, -30)
    separador.run_angle(300, garritaBajar)

def leaveWater():
    right.run_angle(400, -400)
    turn_to_angle(90, 80, 1500)
    drive_base.straight(-80)
    forwardUntilBlack(-300)



def samples():
    turn_to_angle(90, 80, 1000)
    drive_base.settings(straight_speed=100)
    drive_base.straight(120)

    stop_motors()
    wait(100)

    for i in range(6):
        color = color_sensor.color()
        print(color)
        print(color_sensor.hsv())

        if color == Color.WHITE:
            print("BLANCO")
            print(color_sensor.hsv())
            #while separador.angle() <= 20:
            #    separador.run(300)
            separador.run_angle(1000, 30)
            drive_base.straight(50)
            separador.run_angle(1000,-30)
            drive_base.straight(50)
            stop_motors()
            wait(500)
            #separador.run_angle(300,30)
        elif color==Color.YELLOW:
            print("AMARILLO")
            print(color_sensor.hsv())
            separador.run_angle(1000,-30)
            #while separador.angle() >= -20:
            #    separador.run(-300)
            drive_base.straight(50)
            separador.run_angle(1000,30)
            drive_base.straight(50)
            stop_motors()
            wait(500)
            #separador.run_angle(300,-30)
        elif color==Color.GREEN:
            print("verde")
            print(color_sensor.hsv())
            separador.run_angle(100,30)
            #while separador.angle() <= 20:
            #    separador.run(300)
            drive_base.straight(50)
            separador.run_angle(1000,-30)
            drive_base.straight(50)
            stop_motors()
            wait(500)
            #separador.run_angle(300,30)
        elif color==Color.RED:
            print("Rojo")
            print(color_sensor.hsv())
            separador.run_angle(1000,-30)
            #while separador.angle() >= -20:
            #    separador.run(-300)
            drive_base.straight(50)
            separador.run_angle(1000,30)
            drive_base.straight(50)
            stop_motors()
            wait(500)
            #separador.run_angle(300,-30)
        elif color==Color.NONE:
            print("nadota")
            print(color_sensor.hsv())
            drive_base.straight(100)
            wait(1000)

def letsamples():
  #right.run_angle(1000,700)
  #drive_base.straight(600)
  separador.run_angle(400, -40)
  drive_base.settings(straight_speed=600)
  drive_base.straight(-20)
  right.run_angle(400, 450)
  #turn_to_angle(-30, 80, 1000)
  #forwardUntilBlack(300)
  drive_base.straight(800)
  turn_to_angle(0, 80, 1000)
  #forwardUntilBlack(200)
  drive_base.straight(150)
  #forwardUntilBlack(200)
  #drive_base.straight(150)
  
  #separador.run_angle(400, -)

  stop_motors()
  wait(500)

  drive_base.straight(-200)
  #forwardUntilBlack(-300)

  turn_to_angle(-180, 80, 1000)

  #colita.run_angle(500, 100)
  #drive_base.straight(-80)
  #turn_to_angle(-175, 80, 500)
  #turn_to_angle(175, 80, 500)

  #turn_to_angle(-170, 80, 1000)

  #forwardUntilBlack(400)
  drive_base.straight(1500)

  drive_base.straight(-1000)

  turn_to_angle(-90, 80, 2000)

  drive_base.straight(-500)

  drive_base.straight(100)
  forwardUntilBlack(300)

  turn_to_angle(90, 80, 2000)

  drive_base.straight(-600)

  drive_base.straight(200)
  turn_to_angle(0, 80, 1500)
  drive_base.straight(700)
  separador.run_angle(1000, 40)
  drive_base.straight(-750)
  turn_to_angle(-90, 80, 1000)
  forwardUntilBlack(-200)

def final():
    drive_base.straight(100)
    turn_to_angle(-180, 80, 2000)
    drive_base.settings(straight_speed=900)
    drive_base.straight(-800)


robotSetup()
#while True:
 #   print(separador.angle())

inicio()

rover()
roverToSamples()
samples()

letsamples()

final()
#takeWater()
#leaveWater()