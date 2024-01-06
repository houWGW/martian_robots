This repository contains an implimentation of the Martian Robot problem.

### Specs:
- The Martian Robot problem specifications are outlined in the `Developer Programming Problem.pdf` file

### Inputs:
- The input should be contained in the `input.txt` file
- The format of input should start with two values seperated by space to specify the
    x and y coordinates of the top right corner of the Martian grid
- The remaining inputs should be blocks of two rows seperated by empty line specifying initial position and
    orientation of robots and a string specifying a series of robot commands
- The initial position should be contain x coordinate, y coordinate and orientation (`N` / `W` /`E` / `S`)
- The robot commands should be a string (`L` / `R` / `F`)
- Additional robot command types can be added in the `load_command_library` method in `robot.py`
- Max grid size is 50 by 50
- Max command length is 100
- Below is a example input:
```
    5 3
    1 1 E
    RFRFRFRF
    
    3 2 N
    FRRFLLFFRRFLL
    
    0 3 W
    LLFFFLFLFL
```
### Running the programme:
- Clone the repository
- Update the `input.txt` file
- Run the programme by running the below in the repository directory:
    `python main.py`

### Output:
- Output will be shown in terminal output
- Each line of output will indicate an individual robot
- An `.txt` file (`output.txt` by default) would contain all output for all robots

### Notes:
- An invalid input for any robots in the input file will cause an error
- The initial position of robot need to be within the boundary of grid otherwise
    an error will be raised
