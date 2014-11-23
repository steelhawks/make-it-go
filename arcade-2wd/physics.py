#
# See the notes for the other physics sample
#


from pyfrc import wpilib
from pyfrc.physics import drivetrains


class PhysicsEngine(object):
    '''
       Simulates a 2-wheel robot using Tank Drive joystick control 
    '''
    
    # Specified in feet
    ROBOT_WIDTH = 5
    ROBOT_HEIGHT = 4
    
    ROBOT_STARTING_X = 18.5
    ROBOT_STARTING_Y = 12
    
    # In degrees, 0 is east, 90 is south
    STARTING_ANGLE = 180
    
    # Tank drive
    JOYSTICKS = [1, 2] # which joysticks to use for controlling?
                       # first is left, second is right. 1-based index. 
    
    
    def __init__(self, physics_controller):
        '''
            :param physics_controller: `pyfrc.physics.core.Physics` object
                                       to communicate simulation effects to
        '''
        
        self.physics_controller = physics_controller
        
        self.position = 0
        self.last_tm = None
            
    def update_sim(self, now, tm_diff):
        '''
            Called when the simulation parameters for the program need to be
            updated. This is mostly when wpilib.Wait is called.
            
            :param now: The current time as a float
            :param tm_diff: The amount of time that has passed since the last
                            time that this function was called
        '''
        
        # Simulate the drivetrain
        l_motor = wpilib.DigitalModule._pwm[0].Get()
        r_motor = wpilib.DigitalModule._pwm[1].Get()
         
        speed, rotation = drivetrains.two_motor_drivetrain(-l_motor, r_motor, 5) #fix to account for joystick negatives/axes switched in sim
        self.physics_controller.drive(speed, rotation, tm_diff)