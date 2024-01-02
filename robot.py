class Robot():
    def __init__(self, x_start: int, y_start: int, orient_start: str, move: list):
        """
        Robot class with each instance representing a single robot

        Args:
            x_start (int): initial x coordinate of robot
            y_start (int): initial y coordinate of robot
            orient_start (str): initial orientation of robot
            move (list): movement instructions of robot
        
        Returns:
            None
        """
        self.x = x_start
        self.y = y_start
        self.orient = orient_start
        self.move = move
        self.next_move = 0
        self.lost = False
        self.load_command_library()
        assert type(self.move) == list and all(x in self.move_mapping.keys() for x in self.move), 'Unknown robot command type.'
        assert len(self.move) <= 100, 'Robot command too long, limit is 100'
        assert type(self.x) == int, 'Robot initial x coordinate not valid.'
        assert type(self.y) == int, 'Robot initial y coordinate not valid.'
        assert self.orient in set(['N', 'S', 'W', 'E']), 'Robot orientation not valid.'

    def execute_next_move(self):
        """
        Execute next move in the movement command queue

        Args:
            None
        
        Returns:
            None
        """
        self.x, self.y, self.orient = self.move_intepreter(self.move[self.next_move], self.x, self.y, self.orient)
        self.next_move += 1
    
    def move_in_queue(self):
        """
        Check whether there are more moves to be executed in queue

        Args:
            None

        Returns:
            bool: True is more moves in queue false otherwise
        """
        return len(self.move) > self.next_move

    def move_intepreter(self, next_move: int, x: int, y: int, orient: str):
        """
        Translates str robots command to robot position changes

        Args:
            next_move (int): index for next move as specified
            x (int): robot x coordinate
            y (int): robot y coordinate
            orient (str): robot orientation

        Returns:
            x (int): robot x coordinate after next move
            y (int): robot y coordinate after next move
            orient (str): robot orientation after next move
        """
        x += self.move_mapping[next_move][orient][0]
        y += self.move_mapping[next_move][orient][1]
        orient = self.move_mapping[next_move][orient][2]

        return x, y, orient
    
    def load_command_library(self):
        """
        Load the command library for interpretation and execution of commands
        Additional command types should be inplemented here (e.g., included below)

        Args:
            None

        Returns:
            None
        """
        # Define robot move commands
        # Additional commands can be implemented by adding to dict
        # For each command and current orientation, define a tupple
        # (x_move, y_move, new_orientation)
        self.move_mapping = {
            'L':{
                'N':(0,0,'W'),
                'E':(0,0,'N'),
                'S':(0,0,'E'),
                'W':(0,0,'S'),
            },
            'R':{
                'N':(0,0,'E'),
                'E':(0,0,'S'),
                'S':(0,0,'W'),
                'W':(0,0,'N'),
            },
            'F':{
                'N':(0,1,'N'),
                'E':(1,0,'E'),
                'S':(0,-1,'S'),
                'W':(-1,0,'W'),
            },
            # e.g., new command 'T' turning back and move 1 step
            # 'T':{
            #     'N':(0,-1,'S'),
            #     'E':(-1,0,'W'),
            #     'S':(0,1,'N'),
            #     'W':(1,0,'E'),
            # }
        }

    def report_availability(self):
        """
        Report whether the robot is lost

        Args:
            None
        
        Returns:
            str: ' LOST' if lost, '' if not
        """
        if self.lost:
            return ' LOST'
        else:
            return ''