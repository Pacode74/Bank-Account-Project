"""For import to work correctly mark `Bank account Project` as Source Root"""
import unittest
from app.Account import Account
from app.TimeZone import TimeZone
import itertools
import inspect
import types
from string import punctuation


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


class TestInstanceAccountNumberAttribute(unittest.TestCase):
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

    def test_method_is_property(self):
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'account_number'), property))

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestInstanceFirstNameAttribute(unittest.TestCase):
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

    def test_method_is_property(self):
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

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestInstanceLastNameAttribute(unittest.TestCase):
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

    def test_method_is_property(self):
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

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestTimeZoneAttribute(unittest.TestCase):
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

    def test_method_is_property(self):
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'timezone'), property))

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestBalanceAttribute(unittest.TestCase):
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

    def test_method_is_property(self):
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'balance'), property))

    def tearDown(self):
        del self.account_number
        del self.first_name
        del self.last_name
        del self.tz
        del self.balance
        del self.a


class TestFullNameAttribute(unittest.TestCase):
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

    def test_method_is_property(self):
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'full_name'), property))

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
        self.assertTrue(inspect.ismethod(Account.set_interest_rate) and Account.set_interest_rate.__self__ is Account)
        # alternatively testing if method is classmethod:
        self.assertTrue(isinstance(Account.__dict__['set_interest_rate'], classmethod))
        # alternatively:
        self.assertTrue(isinstance(inspect.getattr_static(Account, 'set_interest_rate'), classmethod))

        # # testing if method is staticmethod:
        # self.assertTrue(isinstance(Account.__dict__['put_here_the_name_of_method'], staticmethod))
        # # alternatively:
        # self.assertTrue(isinstance(inspect.getattr_static(Account, 'put_here_the_name_of_method'), staticmethod))

        # # testing if method is just a function, import types:
        # self.assertTrue(isinstance(Account.__dict__['put_here_the_name_of_method'], types.FunctionType))

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

    def test_get_interest_rate_is_class_method(self):
        # alternatively testing if method is just method:
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


if __name__ == "__main__":
    unittest.main()

# In unittest mode:
# PS C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project> python -m tests.test_Account
# .....................................................................
# ----------------------------------------------------------------------
# Ran 69 tests in 0.011s
#
# OK

# In coverage mode:
# PS C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project> coverage run -m tests.test_Account
# .....................................................................
# ----------------------------------------------------------------------
# Ran 69 tests in 0.011s
#
# OK
# PS C:\Users\Pavlo\Desktop\Projects\Testing\Unittest\Bank Account Project> coverage html
# Wrote HTML report to htmlcov\index.html


