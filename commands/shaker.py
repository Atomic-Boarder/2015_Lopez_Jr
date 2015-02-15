__author__ = 'nikolojedison'

from wpilib.command import Command

from .drive_straight import DriveStraight
from .grab_tote import GrabTote

class Shaker(Command):
    """This is the simple auton."""
    def __init__(self, robot):
        super().__init__()
        self.grab_command = GrabTote(robot)
        self.drive_left = DriveStraight(robot, .25, 0, timeout=.2)
        self.drive_right = DriveStraight(robot, -.25, 0, timeout=.2)
        self.driving_right = True

    def initialize(self):
        self.grab_command.start()
        self.drive_right.start()

    def execute(self):
        if self.driving_right:
            if not self.drive_right.running:
                self.drive_left.start()
                self.driving_right = False
        else:
            if not self.drive_left.running:
                self.drive_right.start()
                self.driving_right = True
        super().execute()

    def cancel(self):
        self.grab_command.cancel()
        self.drive_left.cancel()
        self.drive_right.cancel()
        super().cancel()

    def isFinished(self):
        return False