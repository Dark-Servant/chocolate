import lang
import re

class Value:
    def __init__(self, value):
        if type(value) not in [int, float]:
            raise Exception(lang.ERROR_NUMERIC_VALUE)

        if value < 0:
            self.value = 0
        elif value > 1:
            self.value = 1
        else:
            self.value = value

class DictValue:
    def __init__(self, value):
        if not type(value) is dict:
            raise Exception(lang.ERROR_DICT_VALUE)

        full_value = 0
        for code in value:
            if type(value[code]) not in [int, float]:
                raise Exception(lang.ERROR_DICT_PARAMETER_VALUE.format(code=code, value=value[code]))
            else:
                full_value += value[code] if value[code] >0 else 0

        if full_value == 0:
            self.value =  dict.fromkeys(value.keys(), 0)

        else:
            self.value = {}
            for code in value:
                self.value[code] = value[code] / full_value

class AnyValue:
    def __init__(self, value):
        if type(value) in [float, int]:
            self.value = DictValue({'main': Value(value).value}).value

        elif type(value) is dict:
            self.value = DictValue(value).value

        else:
            self.value = {'main': 0}

class ClassField:
    def __setattr__(self, key, value):
        if re.compile(r'percent$', re.I).findall(key):
            object.__setattr__(self, key, Value(value).value)

        else:
            object.__setattr__(self, key, value)