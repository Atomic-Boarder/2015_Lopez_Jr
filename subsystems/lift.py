__author__ = 'nikolojedison'
import wpilib
from wpilib.command import PIDSubsystem
import subsystems
import setpoints

class Lift(PIDSubsystem):

    def __init__(self, robot):
        super().__init__(40, 0, 0)
        self.robot = robot
        self.is_two_inch = False
        self.lift_pot = wpilib.AnalogPotentiometer(1)
        self.motor = wpilib.CANTalon(0)
        self.setAbsoluteTolerance(.01)

    def initDefaultCommand(self):
        pass

    def manualSet(self, output):
        position = self.lift_pot.get()
        if position < setpoints.kBottom and output < 0:
            self.motor.set(0)
        elif position > setpoints.kTop and output > 0:
            self.motor.set(0)
        else:
            self.motor.set(output*1)

    def log(self):
        wpilib.SmartDashboard.putNumber("Elevator Pot", self.lift_pot.get()) #publishes to the Dash

    def returnPIDInput(self):
        return self.lift_pot.get()

    def usePIDOutput(self, output):
        if output > 1:
            output = 1
        elif output < -1:
            ouput = -1
        self.motor.set(output*1)

    def isUp(self):
        """If the lift is all the way up..."""
        self.lift_pot.get() > setpoints.kUp