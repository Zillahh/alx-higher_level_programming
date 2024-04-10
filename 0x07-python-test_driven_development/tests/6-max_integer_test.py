#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ A unitest class that inherits a base class unittest """
    def test_ord_list(self):
        """ test list value to see if returns the highest"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_uord_list(self):
        """ test a list thats unordered and see if it returns the highest"""
        self.assertEqual(max_integer([7, 2, 1, 3]), 7)

    def test_somany(self):
        """ test both float and negative number """
        self.assertEqual(max_integer([2.0, 5.9, -2]), 5.9)
        self.assertEqual(max_integer([-2.6, -0.066, -899]), -0.066)

    def test_empty(self):
        """ test for empty list """
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        """ test chaaracyter not string """
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_string(self):
        """ test just one list"""
        self.assertEqual(max_integer([7]), 7)
