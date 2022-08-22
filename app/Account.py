"""For import to work correctly mark `Bank account Project` as Source Root"""
import itertools
import numbers
from app.TimeZone import TimeZone


class Account:
    transaction_counter = itertools.count(100)
    _interest_rate = 0.5

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        # in practice we probably would want to add checks to make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone(0, 0, 'UTC')
        self.timezone = timezone

        self._balance = float(initial_balance)  # force use of floats here, but maybe Decimal would be better

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

    def __eq__(self, other):
        """This is needed if we want to compare TimeZones()"""
        return (isinstance(other, Account) and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.timezone == other.timezone and
                self.balance == other.balance and
                self.account_number == other.account_number)

# if __name__ == '__main__':
#     a = Account('123456', 'Eric', 'Idle', TimeZone(-2, 0, 'MTS'), 1000)
#     print(a.first_name)
#     a.first_name = "Daniel"
#     print(a.first_name)
#     print(a.balance)
#     print(a.deposit(100))
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

