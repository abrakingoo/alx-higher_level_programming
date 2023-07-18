#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
import unittest


'''
    Runs test cases for the Rectangle module
'''

class test_rectangle(unittest.TestCase):
    '''
        Testing rectangle
    '''
    def test_id(self):
        '''
            Test the id for Rectangle
        '''
        rect = Rectangle(1, 2, 0, 0, 99)
        self.assertEqual(99, rect.id)

    def test_width_value(self):
        """width is less than zero"""

        with self.assertRaises(ValueError):
            rect = Rectangle(-6, 10, 0, 0)


    def test_height_value(self):
        """tests for height of the rectangle """

        with self.assertRaises(ValueError):
            Rectangle(6, -3)

    def test_x_value(self):
        """tests the value of x"""
        with self.assertRaises(ValueError):
            Rectangle(2, 4, -3, 9)

    def test_y_value(self):
        """tests the value of y"""
        with self.assertRaises(ValueError):
            Rectangle(2, 4, 3, -9)

    def test_width_type(self):
        """width is an integer"""

        with self.assertRaises(TypeError):
            rect = Rectangle("hello", 10, 0, 0)


    def test_height_type(self):
        """tests if height of the rectangle
            is an int
        """

        with self.assertRaises(TypeError):
            Rectangle(6, "sunday")

    def test_x_type(self):
        """tests the value of x is an int"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 'x', 9)

    def test_y_type(self):
        """tests the value of y is an int"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 3, 'y')


    def test_rectangle_area(self):
        ''''tests for the area '''
        rect = Rectangle(3, 2)
        res = rect.area()
        self.assertEqual(res, 6)

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.r = Rectangle(5, 10)

    def test_width(self):
        '''
            Testing the Rectangle width getter
        '''
        self.assertEqual(5, self.r.width)

    def test_height(self):
        '''
            Testing the Rectangle height getter
        '''
        self.assertEqual(10, self.r.height)

    def test_x(self):
        '''
            Testing Rectangle x getter and setter
        '''

        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        '''
            Testing Rectangle y getter and setter
        '''

        self.r.y = 45
        self.assertEqual(45, self.r.y)
        self.assertEqual(0, self.r.x)

if __name__ == "__main__":
    unittest.main()
