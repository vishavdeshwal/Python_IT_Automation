# Unit tests are used to validate that small, isolated parts of a program (units) work as intended.
# They are typically written to test functions or methods in a program.
# In this example, we will write unit tests for a function that rearranges names from "Last, First" to "First Last".
# The function we will test is called rearrange_name, which takes a string in the format "Last, First" and returns it in the format "First Last".
# Importing the function to be tested



# Edge cases = inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with.
# Importing the function to be tested
from rearrange import rearrange_name

import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"

        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_empty(self):
        testcase = ""
        expected = ""

        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()

# Edge cases Inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically word with.
