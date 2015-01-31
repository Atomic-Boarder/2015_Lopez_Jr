__author__ = 'nikolojedison'
from wpilib.command import PIDSubsystem

class Mast(PIDSubsystem):

    def __init__(self, robot)
        super().__init__()
        self.robot = robot
        self.mast_pot = wpilib.AnalogPotentiometer(0)

    def initDefaultCommand(self):
        pass
