__author__ = 'nikolojedison'
from wpilib.command import Command

class CloseClaw(Command):

    def __init__(self, robot):
        pass
        
    def initialize(self):
        '''Called just before this Command runs the first time'''
        pass
        
    def execute(self):
        '''Called repeatedly when this Command is scheduled to run'''
        pass
        
    def isFinished(self):
        '''Make this return true when this Command no longer needs to run execute()'''
        pass
    
    def end(self):
        '''Called once after isFinished returns true'''
        pass
            
    def interrupted(self):
        '''Called when another command which requires one or more of the same
           subsystems is scheduled to run'''
        pass