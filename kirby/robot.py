from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, Motor

from systems.drive import DriveSystem
from systems.mechanisms import MechanismsSystem
from systems.colorScanning import ColorScanSystem

class Robot:
    def __init__(self):
        self.hub = PrimeHub()

        self.left_drive_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_drive_motor = Motor(Port.E, Direction.CLOCKWISE)
        
        self.back_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.front_motor = Motor(Port.D, Direction.CLOCKWISE)

        self.line_sensor = ColorSensor(Port.C)
        self.color_sensor = ColorSensor(Port.F)

        self.drive = DriveSystem(
            self.hub,
            self.left_drive_motor,
            self.right_drive_motor,
            self.line_sensor,
            self.color_sensor
        )

        self.mechanisms = MechanismsSystem(
            self.front_motor,
            self.back_motor
        )

        self.color_scan = ColorScanSystem(
            self.color_sensor
        )