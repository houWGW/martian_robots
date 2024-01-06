from robot import Robot

class Grid:
    def __init__(self, x_max: int, y_max: int):
        """
        Class of the grid representing the Martian surface
        Defines the size of the grid and keeps track of 
        last positions of lost robots
        Bottom left corner of the grid is assumed (0,0)

        Args:
            x_max (int): x coordinate of top right corner of grid
            y_max (int): y coordinate of top right corner of grid
        """
        self.x_max = x_max
        self.y_max = y_max
        self.loss_point = set()
        assert type(self.x_max) == int and type(self.y_max) == int, 'Grid size input is not valid'
        assert 0 <= self.x_max <= 50 and 0 <= self.y_max <= 50, 'Grid size too large, limit is 50 x 50'
    
    def load_robot(self, robot: Robot):
        """
        Load robot onto grid

        Args:
            robot (Robot): Robot instance

        Returns:
            None
        """
        self.robot = robot
        assert type(self.robot) == Robot, 'Robot have to be an instance of Robot'
        assert self.in_grid_boundary, 'Robot initial position outside of grid boundary'
        self.get_robot_condition()

    def get_robot_condition(self):
        """
        Retrieve current robot location and orientation

        Args:
            None

        Returns:
            None
        """
        self.last_x = self.robot.x
        self.last_y = self.robot.y
        self.last_orient = self.robot.orient

    def add_loss_memory(self):
        """
        Add the last position of last robot to memory

        Args:
            None
        
        Returns:
            None
        """
        if self.robot.next_move != 0 and self.robot.lost:
            self.loss_point.add((self.last_x, self.last_y))
        else:
            pass

    def prevent_loss(self):
        """
        Prevent robot move if going to result in loss at a loss point

        Args:
            None
        
        Returns:
            None
        """
        if (self.last_x, self.last_y) in self.loss_point and self.robot.lost == True:
            self.robot.lost = False
            self.robot.x = self.last_x
            self.robot.y = self.last_y
            self.robot.orient = self.last_orient
        else:
            pass

    def in_grid_boundary(self):
        """
        Check if robot is in grid boundary

        Args:
            None
        
        Returns:
            bool: true if robot is in boundary, false otherwise
        """
        return 0 <= self.robot.x <= self.x_max and 0 <= self.robot.y <= self.y_max
    
    def record_lost(self):
        """
        Record the robot is lost and record last position in grid

        Args:
            None

        Returns:
            None
        """
        self.robot.lost = True

    def report_last_condition(self):
        """
        Report last condition of robot

        Args:
            None

        Returns:
            str: last x, y and orientation of robot
        """
        return f'{self.last_x} {self.last_y} {self.last_orient}'