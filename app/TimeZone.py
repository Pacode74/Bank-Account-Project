import re


class TimeZone:
    def __init__(self, name=None):
        """:name is the name of timezone"""
        self.validate_timezone_name(value=name, field_title='Timezone "name"', timezone_name='_name')

    def validate_timezone_name(self,  field_title, timezone_name, value=None):
        """Refactoring Error for timezone name"""
        m = re.compile(r'[a-zA-Z]*$')
        if value is None:
            raise Exception(f'The {field_title} parameters is missing. You must insert {field_title} parameter.')
        elif value == "":
            raise ValueError(f"{field_title} parameter is en empty string. Please input valid string.")
        elif not isinstance(value, str):
            raise TypeError("Wrong input type. Input must be alphabetic string.")
        elif not m.match(value):
            raise KeyError("The input must only be alphabet characters and no paces allowed.")
        elif len(value) > 5:
            raise ValueError("The name cannot be more that 5 characters.")
        setattr(self, timezone_name, value)

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"TimeZone(name='{self.name}')"

#
# if __name__ == "__main__":
#     t = TimeZone("MTS")
#     # t = TimeZone("")
#     # t = TimeZone()
#     # t = TimeZone('TMS2')
#     # t = TimeZone('TMS ')
#     # t = TimeZone("ABCDEF")
#     print(t)
#     print(t.name)
#     # t.name = "ZOO"
#     # print(t.name)
#     print(hasattr(t, "name"))
#     print(hasattr(t, "_name"))




