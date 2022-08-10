import unittest
from app.TimeZone import TimeZone
from string import punctuation


class TestNameAttribute(unittest.TestCase):
    def setUp(self):
        self.t = TimeZone('MTS')
        self.t1 = TimeZone('mTS')

    def test_name_value_easy(self):
        """Easy Level Test - test the program runs correctly
        given the correct input information."""
        self.assertEqual(self.t.name, 'MTS')
        self.assertEqual(self.t1.name, 'mTS')

    def test_instance_has_name_attribute_easy(self):
        msg = 'The time instance does not have a category attribute.'
        self.assertTrue(hasattr(self.t, 'name'), msg)

    def test_raiseError_medium(self):
        """Medium Level Testing - test the program runs correctly
           given the wrong input information."""
        with self.assertRaises(Exception):
            TimeZone(None)
        self.assertRaises(Exception, TimeZone, None)
        self.assertRaises(ValueError, TimeZone, "")
        self.assertRaises(ValueError, TimeZone, "ABCDEFG")
        self.assertRaises(KeyError, TimeZone, "MTS5")
        self.assertRaises(TypeError, TimeZone, 123)

    def test_input_wrong_type_raise_error_hard(self):
        """Hard Level Testing - test the program runs correctly
            given any kind of input. Input that the user unlikely to pass as arguments."""
        lst_type = [int, str, float, complex, list, tuple, range, dict, set, frozenset]
        for entry in lst_type:
            self.assertRaises(TypeError, TimeZone, entry)

    def test_input_special_characters_raise_error_hard(self):
        for char in set(punctuation):
            self.assertRaises(KeyError, TimeZone, f'T{char}m')

    def test_error_message_on_alphabetic_characters_only_hard(self):  # (1)
        with self.assertRaisesRegex(KeyError, "The input must only be alphabet characters and no paces allowed."):
            # counter("MTS")
            TimeZone('MTS ')
            TimeZone(' MTS')
            TimeZone('M Ts')
            TimeZone('MTS21')
            # looping all special characters in the test:
            for char in set(punctuation):
                TimeZone(f'MT{char}S')

    # def test_input_special_characters(self):
    #     for char in set(punctuation):
    #         try:
    #             print(f"The entry is Joh{char}n")
    #             self.assertEqual(TimeZone(f'T{char}m'), 2)
    #             break
    #         except Exception as ex:
    #             print(f'Catching {type(ex).__name__} exception on line {ex.__traceback__.tb_lineno}.')
    #             print("Next entry.", '\n')

    # def test_name_attribute_value_hard(self):
    #     """Hard Level Testing - test the program runs correctly
    #     given any kind of input. Input that the user unlikely to pass as arguments."""
    #     # catching and printing exceptions for different types:
    #     lst_type = [int, str, float, complex, list, tuple, range, dict, set, frozenset]
    #     for entry in lst_type:
    #         try:
    #             print(f"The entry is {entry}")
    #             self.assertEqual(TimeZone(f'{entry}'), "MTS")
    #             break
    #         except Exception as ex:
    #             print(f'Catching {type(ex).__name__} exception on line {ex.__traceback__.tb_lineno}.')
    #             print("Next entry.", '\n')

    def tearDown(self):
        del self.t
        del self.t1


class TestRepr(unittest.TestCase):

    def setUp(self):
        self.t = TimeZone('MTS')

    def test_repr_method(self):
        self.assertEqual(repr(self.t), "TimeZone(name='MTS')")

    def tearDown(self):
        del self.t


if __name__ == "__main__":
    unittest.main()

# In unittest mode:
# (testing_venv) C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project>python -m tests.test_TimeZone
# .......
# ----------------------------------------------------------------------
# Ran 7 tests in 0.002s
#
# OK

# In Coverage Mode
# (testing_venv) C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project>coverage run -m tests.test_TimeZone
# .......
# ----------------------------------------------------------------------
# Ran 7 tests in 0.003s
#
# OK

# (testing_venv) C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project>coverage html
# Wrote HTML report to htmlcov\index.html

# In index.html check TimeZone.py



# Notes:

# (1)
# If you check the AssertionError carefully, you will see that
# the assertRaisesRegex method is actually trying to match your
# pattern against 'my message', including the quotes.

# When the match method is implemented, if it turns out that there
# are no matches, then None is returned. There are no functions in
# the re module that throw up an exception when the list or matche
# s is empty
#
# exception re.error
#
# Exception raised when a string passed to one of the functions here
# is not a valid regular expression (for example, it might contain
# unmatched parentheses) or when some other error occurs during
# compilation or matching. It is never an error if a string contains
# no match for a pattern.

