import lang
from percent import Value as PercentValue, ClassField as PercentClassField

#
DEFAULT_SPECIAL_PART_PERCENT = .8

#
DEFAULT_SPECIAL_OIL_PERCENT =\
DEFAULT_FIRST_OIL_PERCENT = .5

def setDefaultSpecialPartPercent(value: float):
    global DEFAULT_SPECIAL_PART_PERCENT
    DEFAULT_SPECIAL_PART_PERCENT = PercentValue(value).value

def setDefaultSpecialOilPercent(value: float):
    global DEFAULT_SPECIAL_OIL_PERCENT
    DEFAULT_SPECIAL_OIL_PERCENT = PercentValue(value).value

def setDefaultFirstOilPercent(value: float):
    global DEFAULT_FIRST_OIL_PERCENT
    DEFAULT_FIRST_OIL_PERCENT = PercentValue(value).value

#
class Mass:
    def __init__(self, value: float):
        self.value = value
        self.special_part_percent = DEFAULT_SPECIAL_PART_PERCENT
        self.special_oil_percent = DEFAULT_SPECIAL_OIL_PERCENT
        self.first_oil_percent = DEFAULT_FIRST_OIL_PERCENT

    def __setattr__(self, key, value):
        if key == 'value':
            if type(value) not in (float, int):
                raise Exception(lang.ERROR_MASS_VALUE_TYPE.format(value=value))

            object.__setattr__(self, key, value)

        else:
            PercentClassField.__setattr__(self, key, value)

#
class FullMass(Mass):
    def getExtentedOil(self):
        return self.value * self.special_part_percent - self.getFirstPartValue()

    def getAddedOil(self):
        return self.value * (1 - self.special_part_percent)

    def getFirstPartValue(self):
        if 1 - self.first_oil_percent <  0.01:
            raise Exception(lang.ERROR_OIL_FIRST_PART_IS_100)
        return self.value * (1 - self.special_oil_percent) / (1 - self.first_oil_percent) * self.special_part_percent

#
class AddedOil(Mass):
    def getExtentedOil(self):
        return self.getFullValue() - self.value - self.getFirstPartValue()

    def getFirstPartValue(self):
        if 1 - self.first_oil_percent <  0.01:
            raise Exception(lang.ERROR_OIL_FIRST_PART_IS_100)
        return self.getFullValue() * self.special_part_percent * (1 - self.special_oil_percent) / (1 - self.first_oil_percent)

    def getFullValue(self):
        if 1 - self.special_part_percent <  0.01:
            raise Exception(lang.ERROR_SPECIAL_PART_IS_100)
        return self.value / (1 - self.special_part_percent)

#
class ExtentedOil(Mass):
    def getAddedOil(self):
        return self.getFullValue() * (1 - self.special_part_percent)

    def getFullValue(self):
        if self.special_part_percent <  0.01:
            raise Exception(lang.ERROR_SPECIAL_PART_IS_0)
        return (self.value + self.getFirstPartValue()) / self.special_part_percent

    def getFirstPartValue(self):
        if self.special_oil_percent - self.first_oil_percent <  0.01:
            raise Exception(lang.ERROR_OIL_FIRST_PART_EQU_SPECIAL_PART)
        return self.value * (1 - self.special_oil_percent) / (self.special_oil_percent - self.first_oil_percent)

#
class FirstMass(Mass):
    def getExtentedOil(self):
        if 1 - self.special_oil_percent <  0.01:
            raise Exception(lang.ERROR_OIL_FULL_PART_IS_100)
        return self.value * (self.special_oil_percent - self.first_oil_percent) / (1 - self.special_oil_percent)

    def getAddedOil(self):
        if self.special_part_percent <  0.01:
            raise Exception(lang.ERROR_SPECIAL_PART_IS_0)
        if 1 - self.special_oil_percent <  0.01:
            raise Exception(lang.ERROR_OIL_FULL_PART_IS_100)
        return self.value * (1 - self.first_oil_percent) / (1 - self.special_oil_percent) * (1 - self.special_part_percent) / self.special_part_percent

    def getFullValue(self):
        if self.special_part_percent <  0.01:
            raise Exception(lang.ERROR_SPECIAL_PART_IS_0)

        if 1 - self.special_oil_percent <  0.01:
            raise Exception(lang.ERROR_OIL_FULL_PART_IS_100)

        return self.value * (1 - self.first_oil_percent) / (1 - self.special_oil_percent) / self.special_part_percent