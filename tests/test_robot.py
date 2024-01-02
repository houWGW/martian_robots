import unittest
from robot import Robot

class TestStringMethods(unittest.TestCase):
    
    def test_execute_next_move(self):
        rt = Robot(3, 2, 'N', ['F','R','R','F','L','L','F','F','R','R','F','L','L'])
        rt.execute_next_move()
        self.assertEqual(rt.x, 3)
        self.assertEqual(rt.y, 3)
        self.assertEqual(rt.orient, 'N')
    
    def test_execute_next_move_e2e(self):
        rt = Robot(1, 1, 'E', ['R','F','R','F','R','F','R'])
        while rt.move_in_queue():
            rt.execute_next_move()
        self.assertEqual(rt.x, 0)
        self.assertEqual(rt.y, 1)
        self.assertEqual(rt.orient, 'E')
    
    def test_wrong_command_type(self):
        with self.assertRaises(AssertionError):
            rt = Robot(3 ,2 ,'N',['F','R','B'])


if __name__ == '__main__':
    unittest.main()