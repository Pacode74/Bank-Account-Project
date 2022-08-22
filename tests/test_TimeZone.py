"""Important: For import mark 'Bank Account Project` as Source Root"""

import numbers
import unittest
from app.TimeZone import TimeZone
from datetime import timedelta, datetime
from string import punctuation


class TestNameAttribute(unittest.TestCase):
    def setUp(self):
        self.t = TimeZone(-0, 0, 'MTS')
        self.t1 = TimeZone(-0, 0, 'mTS')

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
        self.assertRaises(Exception, TimeZone, 0, 0, None)
        self.assertRaises(ValueError, TimeZone, 0, 0, "")
        self.assertRaises(ValueError, TimeZone, 0, 0, "ABCDEFG")
        self.assertRaises(KeyError, TimeZone, 0, 0, "MTS5")
        self.assertRaises(TypeError, TimeZone, 0, 0, 123)

    def test_input_wrong_type_raise_error_hard(self):
        """Hard Level Testing - test the program runs correctly
            given any kind of input. Input that the user unlikely to pass as arguments."""
        lst_type = [int, str, float, complex, list, tuple, range, dict, set, frozenset]
        for entry in lst_type:
            self.assertRaises(TypeError, TimeZone, 0, 0, entry)

    def test_input_special_characters_raise_error_hard(self):
        for char in set(punctuation):
            self.assertRaises(KeyError, TimeZone, 0, 0, f'T{char}m')

    def test_error_message_on_alphabetic_characters_only_hard(self):  # (1)
        self.assertRaisesRegex(KeyError, 'The Timezone "name" parameter must only be alphabet characters and no '
                                         'paces allowed.', TimeZone, 0, 0, '1TS')
        self.assertRaisesRegex(KeyError, 'The Timezone "name" parameter must only be alphabet characters and '
                                         'no paces allowed.', TimeZone, 0, 0, 'MTS ')
        self.assertRaisesRegex(KeyError, 'The Timezone "name" parameter must only be alphabet characters and '
                                         'no paces allowed.', TimeZone, 0, 0, ' MTS')
        self.assertRaisesRegex(KeyError, 'The Timezone "name" parameter must only be alphabet characters and '
                                         'no paces allowed.', TimeZone, 0, 0, 'M Ts')
        self.assertRaisesRegex(KeyError, 'The Timezone "name" parameter must only be alphabet characters and '
                                         'no paces allowed.', TimeZone, 0, 0, 'MTS21')

        # looping all special characters in the test:
        for char in set(punctuation):
            self.assertRaisesRegex(KeyError, 'The Timezone "name" parameter must only be alphabet characters and no'
                                             ' paces allowed.', TimeZone, 0, 0, f'MT{char}S')

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


class TestOffsetHourAndOffsetMinutes(unittest.TestCase):
    def setUp(self):
        self.t = TimeZone(-1, -30, "ABC")

    def test_integral_easy(self):
        TimeZone(-1, -30, "ABC")

    def test_integer_medium(self):
        self.assertTrue(type(self.t._offset_hours), isinstance(self.t._offset_hours, numbers.Integral))
        self.assertTrue(type(self.t._offset_minutes), isinstance(self.t._offset_minutes, numbers.Integral))

    def test_integer_easy_medium(self):
        self.assertRaises(ValueError, TimeZone, "a", 0, "ABC")
        self.assertRaises(ValueError, TimeZone, 0, "a", "ABC")
        self.assertRaises(ValueError, TimeZone, "a", "b", "ABC")

    def test_input_wrong_type_raise_error_hard(self):
        """Hard Level Testing - test the program runs correctly
            given any kind of input. Input that the user unlikely to pass as arguments."""
        lst_type = [int, str, float, complex, list, tuple, range, dict, set, frozenset]
        for entry in lst_type:
            self.assertRaises(ValueError, TimeZone, entry, 0, "ABC")
            self.assertRaises(ValueError, TimeZone, 0, entry, "ABC")
            self.assertRaises(ValueError, TimeZone, entry, entry, "ABC")

    def test_input_special_characters_raise_error_hard(self):
        for char in set(punctuation):
            self.assertRaises(ValueError, TimeZone, char, 0, "ABC")

    def test_offset_hour_boundaries(self):
        """Hour offsets are technically bounded between -12:00 and 14:00."""
        with self.assertRaises(ValueError):
            TimeZone(-13, 0, "ABC")
            TimeZone(15, 0, "ABC")

    def test_offset_minutes_boundaries(self):
        """Minutes offset must between -59 and 59 (inclusive)."""
        self.assertRaises(ValueError, TimeZone, 0, -60, "ABC")
        self.assertRaises(ValueError, TimeZone, 0, 60, "ABC")

    def test_offset_minutes_hours_boundaries(self):
        """Testing both hour and minutes boundaries"""
        with self.assertRaises(ValueError):
            TimeZone(-12, -1, "ABC")
            TimeZone(14, 1, "ABC")

    def tearDown(self):
        del self.t


class TestOffsetAttribute(unittest.TestCase):
    def setUp(self):
        self.t = TimeZone(-1, -30, "ABC")

    def test_offset_easy(self):
        """Easy Level Test - test the program runs correctly
        given the correct input information."""
        self.assertEqual(self.t.offset, timedelta(hours=-1, minutes=-30))

    def test_offset_plus_datetime(self):
        """Easy Level Test - test the program runs correctly
        given the correct input information."""
        dt = datetime.utcnow()
        self.assertEqual(self.t.offset + dt, timedelta(hours=-1, minutes=-30) + dt)

    def test_instance_has_offset_attribute(self):
        msg = 'The time instance does not have a category attribute.'
        self.assertTrue(hasattr(self.t, 'offset'), msg)

    def tearDown(self):
        del self.t


class TestEQ(unittest.TestCase):
    """Testing Instance Equality"""

    def test_timezones_equal(self):
        tz1 = TimeZone(-1, -30, 'ABC')
        tz2 = TimeZone(-1, -30, 'ABC')
        self.assertEqual(tz1, tz2)

    def test_timezones_not_equal_without_name_subset(self):
        """Option 1 - Testing is one instance not equal to another instance"""
        tz = TimeZone(-1, -30, 'ABC')

        test_timezones = (
            TimeZone(-1, -30, 'DEF'),
            TimeZone(-1, 0, 'ABC'),
            TimeZone(1, -30, 'ABC'),
            # TimeZone(offset_hours=-1, offset_minutes=-30, name='ABC')  # here is an error
        )
        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=f'Test # {i}'):
                self.assertNotEqual(tz, test_tz)

    def test_timezones_not_equal_with_name_subset(self):
        """Option 2 - Testing is one instance not equal to another instance"""
        tz = TimeZone(-1, -30, 'ABC')

        test_timezones = (
            ('test1', TimeZone(-1, -30, 'DEF')),
            ('test2', TimeZone(-1, 0, 'ABC')),
            ('test3', TimeZone(1, -30, 'ABC')),
            # ('test4', TimeZone(offset_hours=-1, offset_minutes=-30, name='ABC')),  # here is an error
        )
        for i, test_tz in test_timezones:
            with self.subTest(test_number=f'Test # {i}'):
                self.assertNotEqual(tz, test_tz)


class TestRepr(unittest.TestCase):

    def setUp(self):
        self.t = TimeZone(offset_hours=-1, offset_minutes=30, name="MTS")

    def test_repr_method(self):
        self.assertEqual(repr(self.t), "TimeZone(name='MTS', offset_hours=-1, offset_minutes=30)")

    def tearDown(self):
        del self.t


class Test_ValidateOffsetHoursAndOffsetMinutesIsStaticMethod(unittest.TestCase):
    def test_method_is_staticmethod(self):
        self.assertTrue(isinstance(TimeZone.__dict__['_validate_offset_hours_and_offset_minutes'], staticmethod))


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
