from rearrange import rearrange_name 

import unittest 

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"

        self.assertEqual(rearrange_name(testcase), expected)
    
    # These are the edge cases, the inputs to our code that produce unexpected results
    def test_empty(self):
        testcase = ""
        expected = ""

        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "John, F Kennedy"
        expected = "F Kennedy John"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()