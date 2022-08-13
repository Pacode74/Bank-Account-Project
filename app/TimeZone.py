import re
import numbers
from datetime import timedelta


class TimeZone:
    def __init__(self, offset_hours: numbers.Integral, offset_minutes: numbers.Integral, name: str = None):
        """:name is the name of timezone"""
        self._validate_timezone_name(value=name, field_title='Timezone "name"', property_name='_name')
        self._offset_hours, self._offset_minutes = \
            self._validate_offset_hours_and_offset_minutes(offset_hours, offset_minutes)
        self._offset = offset  # offset comes from validation func

    def _validate_timezone_name(self, field_title, property_name, value=None):
        """Refactoring Error for timezone name"""
        m = re.compile(r'[a-zA-Z]*$')
        if value is None:
            raise Exception(f'The {field_title} parameters is missing. You must insert {field_title} parameter.')
        elif value == "":
            raise ValueError(f"{field_title} parameter is en empty string. Please input valid string.")
        elif not isinstance(value, str):
            raise TypeError(f"Wrong input type. {field_title} must be alphabetic string.")
        elif not m.match(value):
            raise KeyError(f"The {field_title} parameter must only be alphabet characters and no paces allowed.")
        elif len(value) > 5:
            raise ValueError("The name cannot be more that 5 characters.")
        setattr(self, property_name, value)

    @staticmethod
    def _validate_offset_hours_and_offset_minutes(offset_hours, offset_minutes):
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minutes offset must be an integer.')

        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')

        # for time delta sign of minutes will be set to sign of hours
        global offset
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        # offsets are technically bounded between -12:00 and 14:00
        # see: https://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')

        return offset_hours, offset_minutes

    @property
    def name(self):
        return self._name

    @property
    def offset(self):
        return self._offset

    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")

    def __eq__(self, other):
        """This is needed if we want to compare TimeZones()"""
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    """If I want TimeZones is usable as keys, sa we defined __eq__ method,
    I would also have to defined __hash__ method. This class is not hashable."""






