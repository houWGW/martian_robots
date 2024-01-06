import unittest
from robot import Robot
from grid import Grid

class TestStringMethods(unittest.TestCase):
    
    def test_grid_init(self):
        gd = Grid(5,3)

        with self.assertRaises(AssertionError):
            gd = Grid('a',3)

        with self.assertRaises(AssertionError):
            gd = Grid(3,'b')
        
        with self.assertRaises(AssertionError):
            gd = Grid(51, 4)
        with self.assertRaises(AssertionError):
            gd = Grid(3, 60)
        with self.assertRaises(AssertionError):
            gd = Grid(-2, 4)
        with self.assertRaises(AssertionError):
            gd = Grid(5, -4)
    
    def test_load_robot(self):
        rt = Robot(3, 2, 'N', ['F','R','R','F','L','L','F','F','R','R','F','L','L'])
        gd = Grid(5,3)
        gd.load_robot(rt)
        with self.assertRaises(AssertionError):
            gd.load_robot('a')
    
    def test_get_robot_condition(self):
        rt = Robot(3, 2, 'N', ['F','R','R','F','L','L','F','F','R','R','F','L','L'])
        gd = Grid(5,3)
        gd.load_robot(rt)
        gd.get_robot_condition()
        self.assertEqual(gd.last_x, 3)
        self.assertEqual(gd.last_y, 2)
        self.assertEqual(gd.last_orient, 'N')

    def test_add_loss_memory_and_report_last_condition(self):
        rt = Robot(3, 5, 'N', ['F','R','R','F','L','L','F','F','R','R','F','L','L'])
        gd = Grid(5,3)
        gd.load_robot(rt)
        gd.get_robot_condition()
        gd.add_loss_memory()
        self.assertEqual(gd.loss_point, set())

        rt = Robot(2, 3, 'W', ['F','F','F','F'])
        gd.load_robot(rt)
        while rt.move_in_queue() and rt.lost == False:
            if gd.in_grid_boundary():
                gd.get_robot_condition()
            else:
                gd.record_lost()
                gd.add_loss_memory()
            rt.execute_next_move()
        self.assertEqual(gd.loss_point, {(0,3)})
        self.assertEqual(gd.report_last_condition(), '0 3 W')
        self.assertEqual(rt.lost, True)
    
    def test_prevent_loss(self):
        gd = Grid(5,3)
        rt = Robot(2, 3, 'W', ['F','F','F','F'])
        # Robot 1 lost at (0, 3)
        gd.load_robot(rt)
        while rt.move_in_queue() and rt.lost == False:
            rt.execute_next_move()
            if gd.in_grid_boundary():
                gd.get_robot_condition()
            else:
                gd.record_lost()
            gd.prevent_loss()
            gd.add_loss_memory()
        self.assertEqual(gd.report_last_condition(), '0 3 W')
        self.assertEqual(rt.lost, True)
        # Test robot 2 loss at same point prevented
        rt2 = Robot(1, 3, 'W', ['F','F','F','F'])
        gd.load_robot(rt2)
        while rt2.move_in_queue() and rt2.lost == False:
            rt2.execute_next_move()
            if gd.in_grid_boundary():
                gd.get_robot_condition()
            else:
                gd.record_lost()
            gd.prevent_loss()
            gd.add_loss_memory()
        self.assertEqual(gd.report_last_condition(), '0 3 W')
        self.assertEqual(rt2.lost, False)
        # Test robot 3
        rt3 = Robot(4, 2, 'N', ['F','R','F','F'])
        gd.load_robot(rt3)
        while rt3.move_in_queue() and rt3.lost == False:
            rt3.execute_next_move()
            if gd.in_grid_boundary():
                gd.get_robot_condition()
            else:
                gd.record_lost()
            gd.prevent_loss()
            gd.add_loss_memory()
        self.assertEqual(gd.report_last_condition(), '5 3 E')
        self.assertEqual(rt3.lost, True)
        # Test robot 4
        rt4 = Robot(5, 3, 'N', ['F'])
        gd.load_robot(rt4)
        while rt4.move_in_queue() and rt4.lost == False:
            rt4.execute_next_move()
            if gd.in_grid_boundary():
                gd.get_robot_condition()
            else:
                gd.record_lost()
            gd.prevent_loss()
            gd.add_loss_memory()
        self.assertEqual(gd.report_last_condition(), '5 3 N')
        self.assertEqual(rt4.lost, False)