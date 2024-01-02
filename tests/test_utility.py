import unittest
from utility import Utility

class TestStringMethods(unittest.TestCase):
    def test_input_loader(self):
        ut = Utility(input_file="tests/test_input.txt")
        self.assertEqual(ut.grid_size, ['5', '3'])
        self.assertEqual(ut.robots_command, 
                         {'0':{
                             'init_pos': ['1', '1', 'E'], 
                             'move': ['R','F','R','F','R','F','R','F']
                             }, 
                          '1': {
                              'init_pos': ['3', '2', 'N'], 
                              'move': ['F','R','R','F','L','L','F','F','R','R','F','L','L']
                              }
                            }
                        )

    def test_get_grid_size(self):
        ut = Utility(input_file="tests/test_input.txt")
        x_max, y_max = ut.get_grid_size()
        self.assertEqual(x_max, 5)
        self.assertEqual(y_max, 3)

    def test_get_next_robot(self):
        ut = Utility(input_file="tests/test_input.txt")
        ut.robot_number = 1
        x_start, y_start, orient_start, move = ut.get_next_robot()
        self.assertEqual(x_start, 3)
        self.assertEqual(y_start, 2)
        self.assertEqual(orient_start, 'N')
        self.assertEqual(move, ['F','R','R','F','L','L','F','F','R','R','F','L','L'])

    def test_robots_in_queue(self):
        ut = Utility(input_file="tests/test_input.txt")
        self.assertTrue(ut.robots_in_queue())
        _, _, _, _ = ut.get_next_robot()
        self.assertTrue(ut.robots_in_queue())
        _, _, _, _ = ut.get_next_robot()
        self.assertFalse(ut.robots_in_queue())


if __name__ == '__main__':
    unittest.main()