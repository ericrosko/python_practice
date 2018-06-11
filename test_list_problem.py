#!/usr/bin/env python3

'''

Author:     Eric Rosko
Date:       june 11, 2018
File: test_list_problem.py
Usage:
    ./test_list_problem.py -v
    python3 -m unittest
    python3 -m unittest discover -v
    python3 -m unittest -v test_list_problem.py
    python3 -m unittest -v test_list_problem.FindLargestTests
    python3 -m unittest -v test_list_problem.FindLargestNestedArrayTests

'''
import unittest
from unittest import TestCase
from list_problem import find_largest
from list_problem import find_largest_with_nested_lists


class FindLargestNestedArrayTests(TestCase):
    """
    Using tuples here so its all different
    """
    def test_one_tuple(self):
        self.assertEqual(3, find_largest_with_nested_lists((3, 2)))

    def test_one_tuple_2(self):
        self.assertEqual(2, find_largest_with_nested_lists((1, 2)))

    def test_two_tuple(self):
        self.assertEqual(4, find_largest_with_nested_lists((3, 4), (1, 2)))

    def test_three_tuple_nested(self):
        self.assertEqual(6, find_largest_with_nested_lists((3, 4, (5, 6)), (1, 2)))

    def test_three_tuple_nested_3_deept(self):
        self.assertEqual(8, find_largest_with_nested_lists((3, (4, 8), (5, 6)), (1, 2)))


class FindLargestTests(TestCase):
    """
    using lists
    """
    def test_one_item(self):
        self.assertEqual(1, find_largest(1))

    def test_one_array(self):
        self.assertEqual(2, find_largest([1, 2]))

    def test_one_int_one_array(self):
        self.assertEqual(3, find_largest(3, [1, 2]))

    def test_one_int_one_array_var1(self):
        self.assertEqual(3, find_largest(1, [3, 2]))

    def test_one_int_one_array_var2(self):
        self.assertEqual(3, find_largest(2, [1, 3]))

    def test_one_array_one_int(self):
        self.assertEqual(3, find_largest([1, 2], 3))

    def test_one_array_one_int_var1(self):
        self.assertEqual(3, find_largest([1, 3], 2))

    def test_one_array_one_int_var2(self):
        self.assertEqual(3, find_largest([3, 2], 1))

if __name__ == "__main__":
    unittest.main()
