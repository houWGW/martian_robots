from grid import Grid
from robot import Robot
from utility import Utility

def run_programme():
    """
    Execution of the martian robot programme
    """

    # Initiate utility to process input and output
    utility = Utility('input.txt')
    # Initiate grid instance
    grid = Grid(*utility.get_grid_size())
    # For all robots defined in input, execute one by one
    while utility.robots_in_queue():
        # Initiate robot instance based on input
        robot = Robot(*utility.get_next_robot())
        # Load robot to grid
        grid.load_robot(robot)
        while robot.move_in_queue() and not robot.lost:
            # While there is command remaining in queue
            # execute next command
            robot.execute_next_move()
            # If robot after next command is in boundary, record the 
            # position and orientation, otherwise record lost
            if grid.in_grid_boundary():
                grid.get_robot_condition()
            else:
                grid.record_lost()
            # Prevent loss if robot has been lost from that point before
            grid.prevent_loss()
            # Add point of loss to memory if first robot lost from point
            grid.add_loss_memory()
        # Process and write output
        output = grid.report_last_condition() + robot.report_availability()
        print(output)
        utility.aggregate_output(output)
    utility.write_output()

if __name__ == '__main__':
    run_programme()