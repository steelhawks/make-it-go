try:
    import wpilib
except ImportError:
    from pyfrc import wpilib


class MyRobot(wpilib.SimpleRobot):
    '''Main robot class'''
    
    def __init__(self):
        '''Constructor'''
        super().__init__()
        
        self.stick = wpilib.Joystick(1)
        self.left_motor = wpilib.Talon(1)
        self.right_motor = wpilib.Talon(2)
        self.robot_drive = wpilib.RobotDrive(self.left_motor, self.right_motor)
         
    def Disabled(self):
        '''Called when the robot is disabled'''
        while self.IsDisabled():
            wpilib.Wait(0.01)

    def Autonomous(self):
        while self.IsAutonomous() and self.IsEnabled():
            wpilib.Wait(0.04)

    def OperatorControl(self):
        '''Called when operation control mode is enabled'''
        dog = self.GetWatchdog()
        dog.SetEnabled(True)
        dog.SetExpiration(0.25)

        while self.IsOperatorControl() and self.IsEnabled():
            dog.Feed()
            self.robot_drive.ArcadeDrive(self.stick)
            wpilib.Wait(0.04)


def run():
    '''Called by RobotPy when the robot initializes'''
    
    robot = MyRobot()
    robot.StartCompetition()
    
    return robot


if __name__ == '__main__':
    
    wpilib.require_version('2014.7.2')
    
    import physics
    wpilib.internal.physics_controller.setup(physics)
    
    wpilib.run()