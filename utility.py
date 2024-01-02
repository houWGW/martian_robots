class Utility():
    def __init__(self, input_file: str, output_file: str = "output.txt"):
        """
        Class containing utility / tools required

        Args:
            input_file (str): file path of input file
            output_file (str): file path of output file

        Returns:
            None
        """
        self.robot_number = 0
        self.input_file = input_file
        self.output_file = output_file
        self.grid_size, self.robots_command = self.input_loader()
        self.output = ''
    def input_loader(self):
        """
        Load input txt file

        Args:
            file (str): file name of the input txt file in the same directory
        
        Returns:
            grid_size (tuple): upper right corner coordinates of grid
            robots_command (dict): containing initial position and 
                commands for each robot
        """
        with open(self.input_file, "r") as file:
            grid_size = None
            robots_command = {}
            robot_number = 0
            new_robot = True
            for line in file:
                # Read first line of input file as definition for grid size
                if grid_size == None:
                    try:
                        grid_size = line.strip().split()
                        assert(len(grid_size) == 2)
                    except:
                        print("First line for grid size input not valid")
                        break
                # Ignore empty line seperators for different block of input
                elif line.strip() == '':
                    pass
                # Read input for robot initial position
                elif grid_size != None and new_robot == True:
                    robots_command[str(robot_number)] = {}
                    try:
                        robots_command[str(robot_number)]['init_pos'] = line.strip().split()
                        assert(len(robots_command[str(robot_number)]['init_pos']) == 3)
                    except:
                        print("Inputs for robot initial position not valid")
                        break
                    new_robot = False
                # Read input for robot movements
                elif grid_size != None and new_robot == False:
                    try:
                        robots_command[str(robot_number)]['move'] = [*line.strip()]
                    except:
                        print("Inputs for robot movements not valid")
                        break
                    new_robot = True
                    robot_number += 1

        return grid_size, robots_command
    
    def get_grid_size(self):
        """
        Specify size of grid

        Args:
            None

        Returns:
            x_max (int): x coordinate of upper right corner of grid
            y_max (int): y coordinate of upper right corner of grid
        """
        x_max = int(self.grid_size[0])
        y_max = int(self.grid_size[1])

        return x_max, y_max
    
    def get_next_robot(self):
        """
        Specify deployment metrics for the next robot in queue

        Args:
            None
        
        Returns:
            x_start (int): initial x-coordinate of robot
            y_start (int): initial y-coordinate of robot
            orient_start (str): initial orientation of robot
            move (list): movement instructions of robot
        """
        robot_index = self.robot_number
        # Retrieve robot initial condition and movement instructures from input
        x_start = int(self.robots_command[str(robot_index)]['init_pos'][0])
        y_start = int(self.robots_command[str(robot_index)]['init_pos'][1])
        orient_start = self.robots_command[str(robot_index)]['init_pos'][2]
        move = self.robots_command[str(robot_index)]['move']
        # Update index for the next robot to be deployed
        self.robot_number += 1

        return x_start, y_start, orient_start, move
    
    def robots_in_queue(self):
        """
        Checks whether there is any more robots in queue

        Args:
            None
        
        Returns:
            bool: True if there is a next robot in queue, false otherwise
        """

        return int(list(self.robots_command.keys())[-1])>=self.robot_number

    def aggregate_output(self, output):
        """
        Aggregate output from next robot

        Args:
            output (str): string output for next robot
        
        Returns:
            None
        """
        self.output += (output + '\n')
    
    def write_output(self):
        """
        Write the aggregated output to an output file

        Args:
            None

        Returns:
            None
        """
        with open(self.output_file, 'w') as file:
            file.write(self.output)