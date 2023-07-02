#!/usr/bin/python3
"""Unittest for max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""

    def test_if_empty_list(self):
        """Tests for empty list"""
        lst = []
        self.assertIsNone(max_integer(lst))

    def test_if_no_args(self):
        """Tests for no args"""
        self.assertIsNone(max_integer())

    def test_for_one_element(self):
        """Tests for only one item"""
        lst = [100]
        self.assertEqual(max_integer(lst), 100)

    def test_for_positive_end(self):
        """Tests for max at the end of list"""
        val = [2, 10, 8, 40]
        self.assertEqual(max_integer(val), 40)

    def test_positive_at_nth_position(self):
        """Tests for max at nth position"""
        pos = [8, 60, 1, 50]
        self.assertEqual(max_integer(pos), 60)

    def test_positive_at_first_position(self):
        """Tests for all max at the first position"""
        pos = [1000, 2, 3, 4]
        self.assertEqual(max_integer(pos), 1000)

    def test_mixed_negative_and_positive_list(self):
        """Tests for mixed list"""
        allVal = [13, -2, -3, 4]
        self.assertEqual(max_integer(allVal), 13)

    def test_for_negative_only(self):
        """Tests for list of negative integers"""
        allNeg = [-1, -2, -3, -4]
        self.assertEqual(max_integer(allNeg), -1)

    def test_for_non_int_argument(self):
        """Tests for a non-integers arguments"""
        lst = [1, 2, 3, 4, "BestSchool"]
        with self.assertRaises(TypeError):
            max_integer(lst)


if __name__ == "__main__":
    unittest.main()
