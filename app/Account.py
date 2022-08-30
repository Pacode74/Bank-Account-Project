"""For import to work correctly mark `Bank account Project` as Source Root"""
import itertools
import numbers
from app.TimeZone import TimeZone
from datetime import datetime
from collections import namedtuple


class Account:
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5

    _transaction_codes = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        # in practice we probably would want to add checks to account number
        # make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone(0, 0, 'UTC')
        self.timezone = timezone

        self._balance = Account.validate_real_number(initial_balance, 0.01)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def timezone(self):
        return self._timezone

    @property
    def balance(self):
        return self._balance

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')
        self._timezone = value

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number')
        if value < 0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate = value

    def validate_and_set_name(self, property_name, value, field_title):
        """Refactoring Error for first_name and last_name"""
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, property_name, value)

    @staticmethod
    def validate_real_number(value, min_value=None):
        """Refactoring Error for balance, deposit and withdrawal.
        Validate for real and negative numbers"""
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')
        if min_value is not None and value < min_value:
            raise ValueError(f'Value must be at least {min_value}')
        # validation passed, return valid value
        return value

    def generate_confirmation_code(self, transaction_code):
        # main difficulty here is to generate the current time in UTC using this formatting:
        # YYYYMMDDHHMMSS
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}'

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        """Function that converts string confirmation number to separate pieces."""
        Confirmation = namedtuple('Confirmation', 'account_number transaction_code transaction_id time_utc time')

        # dummy-A100-20190325224918-101
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            # really simplistic validation here - would need something better
            raise ValueError('Invalid confirmation code')

        # unpack into separate variables
        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        # need to convert raw_dt_utc into a proper datetime object
        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            # again, probably need better error handling here
            raise ValueError('Invalid transaction datetime') from ex  # keep stacktrace too

        if preferred_time_zone is None:
            preferred_time_zone = TimeZone(0, 0, 'UTC')

        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone specified.')

        dt_preferred = dt_utc + preferred_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        return Confirmation(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str)

    def deposit(self, value):
        # validate for real and negative numbers
        value = Account.validate_real_number(value, min_value=0.01)

        # get transaction code
        transaction_code = Account._transaction_codes['deposit']
        # generate a confirmation code
        conf_code = self.generate_confirmation_code(transaction_code)

        # make deposit and return conf code
        self._balance += value
        return conf_code

    def withdrawal(self, value):
        # validate for real and negative numbers
        value = Account.validate_real_number(value, min_value=0.01)

        accepted = False
        if self.balance - value < 0:
            # insufficient funds - we'll reject this transaction
            transaction_code = Account._transaction_codes['rejected']
        else:
            transaction_code = Account._transaction_codes['withdraw']
            accepted = True

        conf_code = self.generate_confirmation_code(transaction_code)

        if accepted:
            self._balance -= value
        return conf_code

    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(Account._transaction_codes['interest'])
        self._balance += interest
        return conf_code

    def __eq__(self, other):
        """This is needed if we want to compare TimeZones()"""
        return (isinstance(other, Account) and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.timezone == other.timezone and
                self.balance == other.balance and
                self.account_number == other.account_number)

#
# if __name__ == '__main__':
#     from unittest.mock import Mock, MagicMock
#     from datetime import datetime
#
#     a = Account('123456', 'Eric', 'Idle', TimeZone(-2, 0, 'MTS'), 100)

    # print(a.first_name)
    # a.first_name = "Daniel"
    # print(a.first_name)
    #
    # print(a.balance)
    # print(a.deposit(100))
    # print(a.balance)

    # datetime = Mock()
    # datetime.return_value = '20050309080000'
    # print(datetime())
    # print(datetime.utcnow().strftime('%Y%m%d%H%M%S'))
    # print(a.generate_confirmation_code('D'))

    # next = Mock()
    # next.return_value = 333
    # print(a.deposit(100))
    # print(a.withdrawal(100))
#     print(a.balance)
#
#     try:
#         a.deposit(-100)
#     except ValueError as ex:
#         print(ex)
#
#     try:
#         a.withdrawal(-100)
#     except ValueError as ex:
#         print(ex)
#
#     try:
#         a.withdrawal(2000)
#     except ValueError as ex:
#         print(ex)
#
#     print(a.balance)
#     print(a.parse_confirmation_code('X-123456-20220712132334-102', TimeZone('TMS', -1, 0)))
#     print(a.parse_confirmation_code(a.withdrawal(100)))
#     print(a.balance)
#     print(a.parse_confirmation_code(a.deposit(400)))
#     print(a.balance)

