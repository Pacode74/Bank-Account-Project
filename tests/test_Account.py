"""For import to work correctly mark `Bank account Project` as Source Root"""
import unittest
from unittest.mock import patch
from app.Account import Account
from app.TimeZone import TimeZone
import itertools
import inspect
import types
from string import punctuation
from datetime import datetime
from collections import namedtuple
from unittest.mock import Mock


class TestAccountClass(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_account_is_instance_of_type(self):
        self.assertIsInstance(Account, type)

    def test_instance_has_four_attr(self):
        msg = 'Four instance attributes are not defined.'
        actual = len([attr for attr in dir(self.a)
                      if not attr.startswith('_')])
        expected = 16
        self.assertEqual(actual, expected, msg)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestClassTransactionCounterAttribute(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_transaction_counter_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(Account.transaction_counter, type(self.a).transaction_counter)

    def test_transaction_counter_numbers_easy(self):
        self.assertEqual(str(self.a.transaction_counter), str(itertools.count(100)))

    def test_transaction_counter_numbers_medium(self):
        c = itertools.count(100)
        for i in range(20):
            self.assertEqual(next(c), next(self.a.transaction_counter))

    def test_class_has_transaction_counter_attribute_easy(self):
        msg = 'The Account does not have a transaction_counter attribute.'
        self.assertTrue(hasattr(Account, 'transaction_counter'), msg)

    def test_instance_has_class_transaction_counter_attribute_easy(self):
        msg = 'The Account instance does not have a account_number attribute.'
        self.assertTrue(hasattr(self.a, 'transaction_counter'), msg)

    def test_if_transaction_counter_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('transaction_counter', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('transaction_counter', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('transaction_counter', self.a.__class__.__dict__)

    def test_get_transaction_counter_as_333_without_patch_decorator(self):
        """mocking next() and datatime.utcnow"""
        with patch("app.Account.next") as mock_next:
            mock_next.return_value = 333
            with patch("app.Account.datetime") as mock_datetime:
                mock_datetime.utcnow = Mock(return_value=datetime(2011, 3, 9, 8, 0, 0))
                actual = self.a.deposit(100)
                expected = 'D-A100-20110309080000-333'
                self.assertEqual(actual, expected)

    @patch("app.Account.next")
    @patch("app.Account.datetime")
    def test_get_transaction_counter_as_333_with_patch_decorator(self, mock_dt, mock_next):
        mock_dt.utcnow = Mock(return_value=datetime(2005, 3, 1, 6, 0, 0))
        mock_next.return_value = 444
        actual = self.a.deposit(100)
        expected = 'D-A100-20050301060000-444'
        self.assertEqual(actual, expected)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestClassInterestRateAttribute(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_interest_number_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(Account._interest_rate, type(self.a)._interest_rate)

    def test_class_has_interest_rate_attribute_easy(self):
        msg = 'The Account does not have a _interest_rate attribute.'
        self.assertTrue(hasattr(Account, '_interest_rate'), msg)

    def test_instance_has_class_interest_rate_attribute_easy(self):
        msg = 'The Account instance does not have a _interest_rate attribute.'
        self.assertTrue(hasattr(self.a, '_interest_rate'), msg)

    def test_if_attribute_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('_interest_rate', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('_interest_rate', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('_interest_rate', self.a.__class__.__dict__)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestAccountNumber(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_account_number_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(self.a.account_number, self.account_number)

    def test_account_number_property__account_number_attribute(self):
        self.assertEqual(self.a._account_number, self.account_number)

    def test_instance_has__account_number_attribute_easy(self):
        msg = 'The Account instance does not have a account_number attribute.'
        self.assertTrue(hasattr(self.a, '_account_number'), msg)

    def test_instance_has_account_number_property_easy(self):
        msg = 'The Account instance does not have a account_number attribute.'
        self.assertTrue(hasattr(self.a, 'account_number'), msg)

    def test_instance_attribute__account_number_belongs_to_instance(self):
        # print(a.__dict__)
        self.assertTrue('_account_number' in self.a.__dict__)

    def test_property_account_number_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('account_number', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('account_number', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('account_number', self.a.__class__.__dict__)

    def test_account_number_is_property(self):
        self.assertIsInstance(Account.account_number, property)
        # alternatively
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'account_number'), property))

    def test_account_number(self):
        cases = [
            ('test1', 'A100', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'A100'),
            ('test2', 'A200', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'A200'),
            ('test3', 'B453', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'B453'),
            ('test4', 'G9956', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'G9956'),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertEqual(Account(account_number, first_name, last_name, tz, balance).account_number, result)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestFirstName(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_first_name_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(self.a.first_name, self.first_name)

    def test_first_name_property__first_name_attribute(self):
        # print(self.a.__dict__)
        self.assertEqual(self.a._first_name, self.first_name)

    def test_instance_has__first_name_attribute_easy(self):
        msg = 'The Account instance does not have a account_number attribute.'
        self.assertTrue(hasattr(self.a, '_first_name'), msg)

    def test_instance_has_first_name_property_easy(self):
        msg = 'The Account instance does not have a account_number attribute.'
        self.assertTrue(hasattr(self.a, 'first_name'), msg)

    def test_instance_attribute__first_name_belongs_to_instance(self):
        # print(self.a.__dict__)
        self.assertIn('_first_name', self.a.__dict__)

    def test_property_first_name_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('first_name', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('first_name', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('first_name', self.a.__class__.__dict__)

    def test_first_name_is_property(self):
        self.assertIsInstance(Account.first_name, property)
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'first_name'), property))

    def test_set_name_property(self):
        self.a.first_name = 'Daniel'
        self.assertEqual(self.a._first_name, 'Daniel')
        self.assertEqual(self.a.first_name, 'Daniel')

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            self.a.first_name = None
        with self.assertRaises(ValueError):
            self.a.first_name = ''

    def test_first_name(self):
        cases = [
            ('test1', 'A100', 'Daniel', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'Daniel'),
            ('test2', 'A200', 'John', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'John'),
            ('test3', 'B453', 'Fred', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'Fred'),
            ('test4', 'G9956', 'Cris', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'Cris'),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertEqual(Account(account_number, first_name, last_name, tz, balance).first_name, result)

    def test_first_name_incorrect_type_should_raise_error(self):
        cases = [
            ('test1', 'A100', '', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'Daniel'),
            ('test2', 'A200', None, 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'John'),
            ('test3', 'B453', '', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'Fred'),
            ('test4', 'G9956', None, 'LAST', TimeZone(1, 30, 'TZ'), 100.00, 'Cris'),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertRaises(ValueError, Account, account_number, first_name, last_name, tz, balance)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestLastName(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_last_name_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(self.a.last_name, self.last_name)

    def test_last_name_property__last_name_attribute(self):
        # print(self.a.__dict__)
        self.assertEqual(self.a._last_name, self.last_name)

    def test_instance_has__last_name_attribute_easy(self):
        msg = 'The Account instance does not have a account_number attribute.'
        self.assertTrue(hasattr(self.a, '_last_name'), msg)

    def test_instance_has_last_name_property_easy(self):
        msg = 'The Account instance does not have a account_number attribute.'
        self.assertTrue(hasattr(self.a, 'last_name'), msg)

    def test_instance_attribute__last_name_belongs_to_instance(self):
        # print(self.a.__dict__)
        self.assertIn('_last_name', self.a.__dict__)

    def test_property_last_name_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('last_name', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('last_name', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('last_name', self.a.__class__.__dict__)

    def test_last_name_is_property(self):
        self.assertIsInstance(Account.last_name, property)
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'last_name'), property))

    def test_set_last_name_property(self):
        self.a.last_name = 'Ivanov'
        self.assertEqual(self.a._last_name, 'Ivanov')
        self.assertEqual(self.a.last_name, 'Ivanov')

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            self.a.last_name = None
        with self.assertRaises(ValueError):
            self.a.last_name = ''

    def test_last_name(self):
        cases = [
            ('test1', 'A100', 'Daniel', 'de Boer', TimeZone(1, 30, 'TZ'), 100.00, 'de Boer'),
            ('test2', 'A200', 'John', 'Lennon', TimeZone(1, 30, 'TZ'), 100.00, 'Lennon'),
            ('test3', 'B453', 'Fred', 'Mercury', TimeZone(1, 30, 'TZ'), 100.00, 'Mercury'),
            ('test4', 'G9956', 'Cris', 'Scott', TimeZone(1, 30, 'TZ'), 100.00, 'Scott'),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertEqual(Account(account_number, first_name, last_name, tz, balance).last_name, result)

    def test_last_name_incorrect_type_should_raise_error(self):
        cases = [
            ('test1', 'A100', 'Daniel', '', TimeZone(1, 30, 'TZ'), 100.00, 'Daniel'),
            ('test2', 'A200', 'John', None, TimeZone(1, 30, 'TZ'), 100.00, 'John'),
            ('test3', 'B453', 'Fred', None, TimeZone(1, 30, 'TZ'), 100.00, 'Fred'),
            ('test4', 'G9956', 'Cris', '', TimeZone(1, 30, 'TZ'), 100.00, 'Cris'),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertRaises(ValueError, Account, account_number, first_name, last_name, tz, balance)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestTimeZone(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_timezone_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(self.a.timezone, self.tz)

    def test_timezone_none(self):
        self.tz = None
        a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)
        self.assertEqual(a.timezone, TimeZone(0, 0, 'UTC'))

    def test_timezone_property__timezone_attribute(self):
        # print(self.a.__dict__)
        self.assertEqual(self.a._timezone, self.tz)

    def test_instance_has__timezone_attribute(self):
        msg = 'The Account instance does not have a _timezone attribute.'
        self.assertTrue(hasattr(self.a, '_timezone'), msg)

    def test_instance_has_timezone_property(self):
        msg = 'The Account instance does not have a timezone attribute.'
        self.assertTrue(hasattr(self.a, 'timezone'), msg)

    def test_instance_attribute__timezone_belongs_to_instance(self):
        # print(self.a.__dict__)
        self.assertIn('_timezone', self.a.__dict__)

    def test_property_timezone_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('timezone', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('timezone', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('timezone', self.a.__class__.__dict__)

    def test_wrong_input(self):
        self.tz = 1
        with self.assertRaises(ValueError):
            Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_timezone_is_property(self):
        self.assertIsInstance(Account.timezone, property)
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'timezone'), property))

    def test_timezone(self):
        cases = [
            ('test1', 'A100', 'Daniel', 'de Boer', TimeZone(1, 30, 'TZ'), 100.00, TimeZone(1, 30, 'TZ')),
            ('test2', 'A200', 'John', 'Lennon', TimeZone(-1, -30, 'MTS'), 100.00, TimeZone(-1, -30, 'MTS')),
            ('test3', 'B453', 'Fred', 'Mercury', TimeZone(6, -45, 'LUH'), 100.00, TimeZone(6, -45, 'LUH')),
            ('test4', 'G9956', 'Cris', 'Scott', TimeZone(0, 0, 'UTC'), 100.00, TimeZone(0, 0, 'UTC')),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertEqual(Account(account_number, first_name, last_name, tz, balance).timezone, result)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestBalance(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_balance_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(self.a.balance, self.balance)
        self.assertEqual(self.a.balance, 100.00)

    def test_create_account_negative_balance(self):
        self.balance = -100.00
        with self.assertRaises(ValueError):
            self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_balance_property__balance_attribute(self):
        # print(self.a.__dict__)
        self.assertEqual(self.a._balance, self.balance)

    def test_instance_has__balance_attribute(self):
        msg = 'The Account instance does not have a _balance attribute.'
        self.assertTrue(hasattr(self.a, '_balance'), msg)

    def test_instance_has_balance_property(self):
        msg = 'The Account instance does not have a balance attribute.'
        self.assertTrue(hasattr(self.a, 'balance'), msg)

    def test_instance_attribute__balance_belongs_to_instance(self):
        # print(self.a.__dict__)
        self.assertIn('_balance', self.a.__dict__)

    def test_property_balance_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('balance', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('balance', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('balance', self.a.__class__.__dict__)

    def test_balance_is_property(self):
        self.assertIsInstance(Account.balance, property)
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'balance'), property))

    def test_balance(self):
        cases = [
            ('test1', 'A100', 'Daniel', 'de Boer', TimeZone(1, 30, 'TZ'), 100.00, 100.00),
            ('test2', 'A200', 'John', 'Lennon', TimeZone(-1, -30, 'MTS'), 200.00, 200.00),
            ('test3', 'B453', 'Fred', 'Mercury', TimeZone(6, -45, 'LUH'), 1000.00, 1000.00),
            ('test4', 'G9956', 'Cris', 'Scott', TimeZone(0, 0, 'UTC'), 1.00, 1.00),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertEqual(Account(account_number, first_name, last_name, tz, balance).balance, result)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestFullName(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_full_name_easy(self):
        """Easy Level Test - test the program runs correctly
                given the correct input information."""
        self.assertEqual(self.first_name + ' ' + self.last_name, self.a.full_name)

    def test_instance_calls_full_name_property(self):
        self.assertEqual(self.a.full_name, "FIRST LAST")

    def test_instance_has_full_name_property(self):
        msg = 'The Account instance does not have a full_name property.'
        self.assertTrue(hasattr(self.a, 'full_name'), msg)

    def test_property_full_name_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('full_name', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('full_name', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('full_name', self.a.__class__.__dict__)

    def test_full_name_is_property(self):
        self.assertIsInstance(Account.full_name, property)
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'full_name'), property))

    def test_full_name(self):
        cases = [
            ('test1', 'A100', 'Daniel', 'de Boer', TimeZone(1, 30, 'TZ'), 100.00, 'Daniel de Boer'),
            ('test2', 'A200', 'John', 'Lennon', TimeZone(-1, -30, 'MTS'), 200.00, 'John Lennon'),
            ('test3', 'B453', 'Fred', 'Mercury', TimeZone(6, -45, 'LUH'), 1000.00, 'Fred Mercury'),
            ('test4', 'G9956', 'Cris', 'Scott', TimeZone(0, 0, 'UTC'), 1.00, 'Cris Scott'),
        ]

        for test, account_number, first_name, last_name, tz, balance, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertEqual(Account(account_number, first_name, last_name, tz, balance).full_name, result)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestClassMethodSetInterestRateMethod(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_set_interest_rate_is_class_method(self):
        """Test that it is a method and that it is a class method.
        if inspect.ismethod(cls.method) and cls.method.__self__ is cls:
        method bound to the class, e.g. a classmethod"""
        self.assertIsInstance(Account.__dict__['set_interest_rate'], classmethod)
        # alternatively:
        self.assertTrue(inspect.ismethod(Account.set_interest_rate) and Account.set_interest_rate.__self__ is Account)
        # alternatively testing if method is classmethod:
        self.assertTrue(isinstance(Account.__dict__['set_interest_rate'], classmethod))
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'set_interest_rate'), classmethod))

        # # testing if method is staticmethod:
        # self.assertTrue(isinstance(Account.__dict__['put_here_the_name_of_method'], staticmethod))
        # # alternatively:
        # self.assertTrue(isinstance(inspect.getattr_static(Account, 'put_here_the_name_of_method'), staticmethod))
        #
        # # testing if method is just a function, import types:
        # self.assertTrue(isinstance(Account.__dict__['put_here_the_name_of_method'], types.FunctionType))
        #
        # # test is method is a property:
        # self.assertTrue(isinstance(inspect.getattr_static(Account, 'put_here_the_name_of_method'), property))

    def test_setting_interest_rate_easy(self):
        type(self.a).set_interest_rate(1.0)
        self.assertEqual(type(self.a).get_interest_rate(), 1.0)
        # alternatively 1:
        self.a.__class__.set_interest_rate(0.4)
        self.assertEqual(self.a.__class__.get_interest_rate(), 0.4)
        # alternatively 2:
        self.a.__class__.set_interest_rate(0.6)
        self.assertEqual(self.a.__class__.get_interest_rate(), self.a._interest_rate)

    def test_class_has_set_interest_rate_method(self):
        msg = 'The Account does not have a set_interest_rate method.'
        self.assertTrue(hasattr(Account, 'set_interest_rate'), msg)

    def test_if_set_interest_rate_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('set_interest_rate', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('set_interest_rate', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('set_interest_rate', self.a.__class__.__dict__)

    def test_wrong_input(self):
        # with self.assertRaises(ValueError):
        #     self.a.__class__.set_interest_rate('John')

        wrong_types = ['John', None, -0.5, "", int, str, float, complex, list, tuple, range, dict, set, frozenset]
        for entry in wrong_types:
            self.assertRaises(ValueError, self.a.__class__.set_interest_rate, entry)
        for char in set(punctuation):
            self.assertRaises(ValueError, self.a.__class__.set_interest_rate, char)

    def test_set_interest_rate(self):
        cases = [
            ('test1', Account, 0.1, 0.1),
            ('test2', Account, 0.5, 0.5),
            ('test3', Account, 0.7, 0.7),
            ('test4', Account, 1.0, 1.0),
        ]

        for test, account, interest_rate, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                account.set_interest_rate(interest_rate)
                self.assertEqual(account.get_interest_rate(), result)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestClassMethodGetInterestRateMethod(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_get_interest_rate_is_class_method(self):
        """Test that it is a method and that it is a class method.
        if inspect.ismethod(cls.method) and cls.method.__self__ is cls:
        method bound to the class, e.g. a classmethod"""
        self.assertTrue(inspect.ismethod(Account.get_interest_rate) and Account.get_interest_rate.__self__ is Account)
        # alternatively testing if method is classmethod:
        self.assertTrue(isinstance(Account.__dict__['get_interest_rate'], classmethod))
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'get_interest_rate'), classmethod))

    def test_get_interest_rate_easy(self):
        # alternatively 1:
        self.assertEqual(self.a.__class__.get_interest_rate(), self.a._interest_rate)
        # alternatively 2:
        self.a.__class__.set_interest_rate(0.6)
        self.assertEqual(self.a.__class__.get_interest_rate(), self.a._interest_rate)

    def test_class_has_get_interest_rate_method(self):
        msg = 'The Account does not have a get_interest_rate method.'
        self.assertTrue(hasattr(Account, 'get_interest_rate'), msg)

    def test_if_get_interest_rate_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('get_interest_rate', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('get_interest_rate', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('get_interest_rate', self.a.__class__.__dict__)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestMethodValidateAndSetName(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_get_interest_rate_is_function(self):
        self.assertIsInstance(Account.__dict__['validate_and_set_name'], types.FunctionType)
        # alternatively:
        self.assertTrue(isinstance(Account.__dict__['validate_and_set_name'], types.FunctionType))
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'validate_and_set_name'), types.FunctionType))

    def test_get_interest_rate_easy(self):
        self.a.validate_and_set_name("_first_name", "George", "First Name")
        self.assertEqual(self.a.first_name, 'George')

    def test_class_has_validate_and_set_name_method(self):
        msg = 'The Account does not have a validate_and_set_name method.'
        self.assertTrue(hasattr(Account, 'validate_and_set_name'), msg)

    def test_if_validate_and_set_name_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('validate_and_set_name', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('validate_and_set_name', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('validate_and_set_name', self.a.__class__.__dict__)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestCompareInstances(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_instances_equal(self):
        a1 = Account("A200", "Daniel", "Ivanov", TimeZone(-1, 30, 'TZ'), 1000.00)
        a2 = Account("A200", "Daniel", "Ivanov", TimeZone(-1, 30, 'TZ'), 1000.00)
        self.assertEqual(a1, a2)

    def test_instances_not_equal_with_name_subset(self):
        """Option 1 - Testing is one instance not equal to another instance"""
        test_accounts = (
            ('test1', Account("A200", "Daniel", "Ivanov", TimeZone(-1, 30, 'TZ'), 1000.00)),
            ('test2', Account("A300", "Pavlo", "Ivanov", TimeZone(0, 0, 'UTC'), 2000.00)),
            ('test3', Account("A500", "John", "Hue", TimeZone(1, 40, 'TMC'), 3000.00)),
            ('test4', Account("A600", "Luk", "Besson", TimeZone(0, 30, 'RTW'), 10.00)),
            ('test5', Account("A200", "Peter", "Zalm", TimeZone(-9, 30, 'PLO'), 50.00)),
            # ('test6', Account('A100', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00))  # errors
        )
        for i, test_a in test_accounts:
            with self.subTest(test_number=f'Test # {i}'):
                self.assertNotEqual(self.a, test_a)

    def test_instances_not_equal_without_name_subset(self):
        """Option 2 - Testing is one instance not equal to another instance"""
        test_accounts = (
            Account("A200", "Daniel", "Ivanov", TimeZone(-1, 30, 'TZ'), 1000.00),  # test 0
            Account("A300", "Pavlo", "Ivanov", TimeZone(0, 0, 'UTC'), 2000.00),  # test 1
            Account("A500", "John", "Hue", TimeZone(1, 40, 'TMC'), 3000.00),  # test 2
            Account("A600", "Luk", "Besson", TimeZone(0, 30, 'RTW'), 10.00),  # test 3
            Account("A200", "Peter", "Zalm", TimeZone(-9, 30, 'PLO'), 50.00),  # test 4
            # Account('A100', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00)  # test 5 errors
        )
        for i, test_a in enumerate(test_accounts):
            with self.subTest(test_number=f'Test # {i}'):
                self.assertNotEqual(self.a, test_a)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestStaticMethodValidateRealNumber(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_static_method(self):
        """Test that it is a method and that it is a static method."""
        self.assertIsInstance(Account.__dict__['validate_real_number'], staticmethod)
        # alternatively:
        self.assertTrue(isinstance(Account.__dict__['validate_real_number'], staticmethod))
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'validate_real_number'), staticmethod))

    def test_validate_real_number_easy(self):
        self.assertEqual(type(self.a).validate_real_number(1.0, min_value=0.1), 1.0)
        self.assertEqual(self.a.validate_real_number(1.0, min_value=0.1), 1.0)

    def test_account_has_validate_real_number_function_attribute(self):
        self.assertTrue(hasattr(Account, 'validate_real_number'))

    def test_account_has_callable_validate_real_number_function(self):
        self.assertTrue(callable(Account.validate_real_number))

    def test_if_validate_real_number_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('validate_real_number', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('validate_real_number', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('validate_real_number', self.a.__class__.__dict__)

    def test_wrong_input(self):
        # with self.assertRaises(ValueError):
        #     self.a.__class__.set_interest_rate('John')

        wrong_types = [0, 'John', None, -0.5, "", int, str, float, complex, list, tuple, range, dict, set, frozenset]
        for entry in wrong_types:
            self.assertRaises(ValueError, self.a.__class__.validate_real_number, entry, 0.1)
        for char in set(punctuation):
            self.assertRaises(ValueError, self.a.__class__.validate_real_number, char, 0.1)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestGenerateConfirmationCode(unittest.TestCase):

    def setUp(self):
        Account.transaction_counter = itertools.count(100)
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.b = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    @patch("app.Account.datetime")
    def test_get_datetime_as_20110309080000_with_patch_decorator(self, mock_dt):
        mock_dt.utcnow = Mock(return_value=datetime(2011, 3, 9, 8, 0, 0))
        actual = self.b.generate_confirmation_code('D')
        expected = 'D-A100-20110309080000-100'
        self.assertEqual(actual, expected)

    def test_get_datetime_as_20050309080000_without_patch_decorator(self):
        with patch("app.Account.datetime") as mock_datetime:
            mock_datetime.utcnow = Mock(return_value=datetime(2011, 3, 9, 8, 0, 0))
            actual = self.b.generate_confirmation_code('D')
            expected = 'D-A100-20110309080000-100'
            self.assertEqual(actual, expected)

    def test_get_datetime_as_20050309080000_in_other_functions(self):
        with patch("app.Account.datetime") as mock_datetime:
            mock_datetime.utcnow = Mock(return_value=datetime(2011, 3, 9, 8, 0, 0))
            actual = self.b.deposit(100)
            expected = 'D-A100-20110309080000-100'
            self.assertEqual(actual, expected)

            actual = self.b.withdrawal(100)
            expected = 'W-A100-20110309080000-101'
            self.assertEqual(actual, expected)

            actual = self.b.pay_interest()
            expected = 'I-A100-20110309080000-102'
            self.assertEqual(actual, expected)

            actual = self.b.withdrawal(1000)
            expected = 'X-A100-20110309080000-103'
            self.assertEqual(actual, expected)

    def test_generate_confirmation_code_is_method(self):
        """Test that it is a function method."""
        self.assertIsInstance(Account.__dict__['generate_confirmation_code'], types.FunctionType)
        # alternatively:
        self.assertTrue(isinstance(Account.__dict__['generate_confirmation_code'], types.FunctionType))

    def test_function_attribute(self):
        self.assertTrue(hasattr(self.b, 'generate_confirmation_code'))

    def test_function_callable(self):
        self.assertTrue(callable(self.b.generate_confirmation_code))

    def test_generate_confirmation_code_easy(self):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        trans_counter = itertools.count(100)
        acc_number = 'A100'
        trans_codes = {
            'deposit': 'D',
            'withdraw': 'W',
            'interest': 'I',
            'rejected': 'X'
        }

        r = trans_codes['deposit'] + "-" + acc_number + "-" + str(dt_str) + "-" + str(next(trans_counter))
        self.assertEqual(self.b.generate_confirmation_code('D'), r)

    def test_generate_confirmation_code(self):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        trans_counter = itertools.count(100)

        trans_codes = {
            'deposit': 'D',
            'withdraw': 'W',
            'interest': 'I',
            'rejected': 'X'
        }

        r1 = trans_codes['deposit'] + "-" + 'A100' + "-" + str(dt_str) + "-" + str(next(trans_counter))
        r2 = trans_codes['withdraw'] + "-" + 'A200' + "-" + str(dt_str) + "-" + str(next(trans_counter))
        r3 = trans_codes['interest'] + "-" + 'B453' + "-" + str(dt_str) + "-" + str(next(trans_counter))
        r4 = trans_codes['rejected'] + "-" + 'G9956' + "-" + str(dt_str) + "-" + str(next(trans_counter))

        cases = [
            ('test1', 'A100', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, trans_codes['deposit'], r1),
            ('test2', 'A200', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, trans_codes['withdraw'], r2),
            ('test3', 'B453', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, trans_codes['interest'], r3),
            ('test4', 'G9956', 'FIRST', 'LAST', TimeZone(1, 30, 'TZ'), 100.00, trans_codes['rejected'], r4),
        ]

        for test, account_number, first_name, last_name, tz, balance, transaction_code, result in cases:
            with self.subTest(test_number=f'Test # {test}'):
                self.assertEqual(Account(account_number, first_name, last_name, tz, balance).
                                 generate_confirmation_code(transaction_code), result)

    def test_if_generate_confirmation_code_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('generate_confirmation_code', Account.__dict__)

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.b


class TestStaticMethodParseConfirmationCode(unittest.TestCase):
    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.a = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)
        self.trans_codes = {
            'deposit': 'D',
            'withdraw': 'W',
            'interest': 'I',
            'rejected': 'X'
        }
        self.conf_code = self.a.generate_confirmation_code(self.trans_codes['deposit'])

    def test_static_method(self):
        """Test that it is a method and that it is a static method."""
        self.assertIsInstance(Account.__dict__['parse_confirmation_code'], staticmethod)
        # alternatively:
        self.assertTrue(isinstance(Account.__dict__['parse_confirmation_code'], staticmethod))
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'parse_confirmation_code'), staticmethod))

    def test_parse_confirmation_code_with_preferred_time_zone(self):
        # print(conf_code)
        # print(type(self.a).parse_confirmation_code(conf_code, TimeZone(1, 30, "MTC")))
        Confirm = namedtuple('Confirmation', 'account_number transaction_code transaction_id time_utc time')
        parts = self.conf_code.split('-')
        transaction_code, account_number, raw_dt_utc, transaction_id = parts
        dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        preferred_time_zone = TimeZone(1, 30, "MTC")
        dt_preferred = dt_utc + preferred_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        self.assertEqual(type(self.a).parse_confirmation_code(self.conf_code, TimeZone(1, 30, "MTC")),
                        Confirm(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str))

    def test_parse_confirmation_code_without_preferred_time_zone(self):
        # print(conf_code)
        # print(type(self.a).parse_confirmation_code(conf_code, TimeZone(1, 30, "MTC")))
        Confirm = namedtuple('Confirmation', 'account_number transaction_code transaction_id time_utc time')
        parts = self.conf_code.split('-')
        transaction_code, account_number, raw_dt_utc, transaction_id = parts
        dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        preferred_time_zone = TimeZone(0, 0, "UTC")
        dt_preferred = dt_utc + preferred_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        self.assertEqual(type(self.a).parse_confirmation_code(self.conf_code, preferred_time_zone=None),
                         Confirm(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str))

    def test_if_parse_confirmation_code_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('parse_confirmation_code', Account.__dict__)
        # alternatively 1:
        # print(type(self.a).__dict__)
        self.assertIn('parse_confirmation_code', type(self.a).__dict__)
        # alternatively 2:
        # print(self.a.__class__.__dict__)
        self.assertIn('parse_confirmation_code', self.a.__class__.__dict__)

    def test_wrong_input_easy(self):
        # with self.assertRaises(ValueError):
        #     self.a.__class__.set_interest_rate('John')

        wrong_values = ['D-A100-20220822200421-100-SD', 'D-A100-20220822200421', 'D-A100-08222022200421-100',
                        'D-A100-John-100']  # 'D-A100-20220822200421-100'
        for entry in wrong_values:
            self.assertRaises(ValueError, self.a.__class__.parse_confirmation_code, entry)

        self.assertRaises(ValueError, self.a.__class__.parse_confirmation_code, 'D-A100-20220822200421-100',
                          preferred_time_zone=str)

    def test_function_attribute(self):
        self.assertTrue(hasattr(self.a, 'parse_confirmation_code'))

    def test_function_callable(self):
        self.assertTrue(callable(self.a.parse_confirmation_code))

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a
        del self.trans_codes
        del self.conf_code


class TestDeposit(unittest.TestCase):

    def setUp(self):
        Account.transaction_counter = itertools.count(100)
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.b = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_deposit_is_method(self):
        """Test that it is a function method."""
        self.assertIsInstance(Account.__dict__['deposit'], types.FunctionType)
        # alternatively:
        self.assertTrue(isinstance(Account.__dict__['deposit'], types.FunctionType))

    def test_deposit_easy(self):
        l1 = [self.b.deposit(100) for _ in range(4)]
        self.assertEqual(self.b.balance, 500)

    def test_if_generate_confirmation_code_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('deposit', Account.__dict__)

    def test_account_deposit_ok(self):
        conf_code = self.b.deposit(100)
        self.assertIn('D-', conf_code)  # checks if `D-` in the confirmation code
        # alternatively:
        # self.assertTrue(conf_code.startswith('D-'))

    def test_account_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            conf_code = self.b.deposit(-100)

    def test_function_attribute(self):
        self.assertTrue(hasattr(self.b, 'deposit'))

    def test_function_callable(self):
        self.assertTrue(callable(self.b.deposit))

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.b


class TestWithdrawal(unittest.TestCase):

    def setUp(self):
        Account.transaction_counter = itertools.count(100)
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 100.00
        self.b = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_withdrawal_is_method(self):
        """Test that it is a function method."""
        self.assertIsInstance(Account.__dict__['withdrawal'], types.FunctionType)
        # alternatively:
        self.assertTrue(isinstance(Account.__dict__['withdrawal'], types.FunctionType))

    def test_deposit_easy(self):
        l1 = [self.b.deposit(100) for _ in range(4)]
        l2 = [self.b.withdrawal(50) for _ in range(4)]
        self.assertEqual(self.b.balance, 300)

    def test_if_generate_confirmation_code_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('withdrawal', Account.__dict__)

    def test_withdrawal_ok(self):
        conf_code = self.b.withdrawal(50)
        self.assertIn('W-', conf_code)  # checks if `W-` in the confirmation code
        # alternatively:
        # self.assertTrue(conf_code.startswith('w-'))

    def test_withdrawal_fail(self):
        conf_code = self.b.withdrawal(300)
        self.assertIn('X-', conf_code)  # checks if `X-` in the confirmation code
        # alternatively:
        # self.assertTrue(conf_code.startswith('x-'))

    def test_account_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            conf_code = self.b.withdrawal(-100)

    def test_function_attribute(self):
        self.assertTrue(hasattr(self.b, 'withdrawal'))

    def test_function_callable(self):
        self.assertTrue(callable(self.b.withdrawal))

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.b


class TestPayInterest(unittest.TestCase):

    def setUp(self):
        Account.transaction_counter = itertools.count(100)
        self.account_number = 'A100'
        self.first_name = 'FIRST'
        self.last_name = 'LAST'
        self.tz = TimeZone(1, 30, 'TZ')
        self.balance = 1000.00
        self.b = Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)
        self.b.set_interest_rate(0.5)

    def test_pay_interest_is_method(self):
        """Test that it is a function method."""
        self.assertIsInstance(Account.__dict__['pay_interest'], types.FunctionType)
        # alternatively:
        self.assertTrue(isinstance(Account.__dict__['pay_interest'], types.FunctionType))

    def test_pay_interest_easy(self):
        l1 = [self.b.pay_interest() for _ in range(2)]
        self.assertEqual(self.b.balance, 1010.025)

    def test_pay_interest_print(self):
        interest = self.b.pay_interest()
        self.assertIn('I-', interest)

    def test_if_generate_confirmation_code_method_belongs_to_class(self):
        # print(Account.__dict__)
        self.assertIn('pay_interest', Account.__dict__)

    def test_function_attribute(self):
        self.assertTrue(hasattr(self.b, 'pay_interest'))

    def test_function_callable(self):
        self.assertTrue(callable(self.b.pay_interest))

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.b


if __name__ == "__main__":
    unittest.main()

# In unittest mode:
# PS C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project> python -m tests.test_Account
# ....................................................................................................
# ----------------------------------------------------------------------
# Ran 100 tests in 0.021s
#
# OK


# In coverage mode:
# PS C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project> coverage run -m tests.test_Account
# ....................................................................................................
# ----------------------------------------------------------------------
# Ran 100 tests in 0.030s
#
# OK

# PS C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project> coverage html
# Wrote HTML report to htmlcov\index.html

# Look at Account.py in Index.html

