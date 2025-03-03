from chocolate.mass import *
from percent import AnyValue as PercentAnyValue, ClassField as PercentClassField
import lang

DEFAULT_MAIN_PERCENT = 1
DEFAULT_FULL_MASS_VALUE = 100

class FullMassField:
    def __init__(self, value):
        if type(value) is not FullMass:
            raise Exception(lang.ERROR_VALUE_IS_NOT_FULL_MASS.format(classname=FullMass.__name__))

        self.value = value

class ImpurityPart:
    def __init__(self, value=1):
        self.main_percent = DEFAULT_MAIN_PERCENT
        self.value = value

    def __setattr__(self, key, value):
        if key == 'value':
            object.__setattr__(self, key, PercentAnyValue(value).value)

        elif key == 'full_mass':
            object.__setattr__(self, key, FullMassField(value).value)

        else:
            PercentClassField.__setattr__(self, key, value)

    def __getattr__(self, name):
        if name == 'full_mass':
            self.full_mass = FullMass(DEFAULT_FULL_MASS_VALUE)
            return self.full_mass

        else:
            return getattr(self, name)

    def getMassValue(self):
        value = {}
        full_value = self.full_mass.getFirstPartValue() * (1 - self.full_mass.first_oil_percent) * self.main_percent
        for code in self.value:
            value[code] = full_value * self.value[code]
        return value

    def getFirstMassValue(self):
        return self.full_mass.getFirstPartValue() * (1 - self.main_percent)

    def getOilMassValue(self):
        return self.full_mass.getFirstPartValue() * self.full_mass.first_oil_percent * self.main_percent

class ImpurityList:
    def __init__(self):
        self.units = []
        self.special_data = {}
        self.use_prepared_unit = False

    def append(self, unit):
        if type(unit is ImpurityPart):
            self.units.append(unit)

        else:
            self.units.append(ImpurityPart(unit))

        return self

    def __setattr__(self, key, value):
        if key == 'full_mass':
            full_mass = FullMassField(value).value
            for unit in self.units:
                unit.full_mass = full_mass
        else:
            object.__setattr__(self, key, value)

    def setLastUnitSpecialData(self, **data):
        self.special_data[id(self.units[-1])] = data
        return self

    def getLastUnitSpecialData(self):
        return self.special_data[id(self.units[-1])]

    def __getitem__(self, number):
        if len(self.units) < number:
            return None

        return self.getPreparedUnit(number) if self.use_prepared_unit else self.units[number]

    def __iter__(self):
        self.unit_iterator = iter(range(len(self.units)))
        return self

    def __next__(self):
        number = next(self.unit_iterator)
        return  self.getPreparedUnit(number) if self.use_prepared_unit else self.units[number]

    def getPreparedUnit(self, number : int):
        if (not type(number) is int) or (number >= len(self.units)):
            return None

        special_data_id = id(self.units[number])
        return {
            'special_data': self.special_data[special_data_id] if special_data_id in self.special_data else {},
            'first_mass': self.units[number].getFirstMassValue(),
            'oil_mass': {
                'replaced': self.units[number].getOilMassValue(),
                'extented': self.units[number].full_mass.getExtentedOil(),
                'added': self.units[number].full_mass.getAddedOil(),
            },
            'impurity': self.units[number].getMassValue()
        }

class ImpurityReport:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        if (key == 'value') and (not type(value) is ImpurityList):
            raise Exception(lang.ERROR_REPORT_IMPURITY_TYPE.format(classname=FullMass.__name__))
        object.__setattr__(self, key, value)

    def getFirstMass(self):
        result = {}
        for unit in self.value.units:
            first_mass_code = '%.2f' % (unit.full_mass.first_oil_percent)
            if not first_mass_code in result:
                result[first_mass_code] = 0.0
            result[first_mass_code] += unit.getFirstMassValue()
        return result

    def getOilMass(self):
        result = 0
        old_use_prepared_unit = self.value.use_prepared_unit
        self.value.use_prepared_unit = True
        for unit in self.value:
            result += sum(unit['oil_mass'].values())
        self.value.use_prepared_unit = old_use_prepared_unit
        return result

    def getImpurityMass(self):
        result = {}
        old_use_prepared_unit = self.value.use_prepared_unit
        self.value.use_prepared_unit = True
        for unit in self.value:
            for code in unit['impurity']:
                result[code] = (result[code] if code in result else 0) + unit['impurity'][code]
        self.value.use_prepared_unit = old_use_prepared_unit
        return result

    def getNumericSpecialData(self):
        result = {}
        old_use_prepared_unit = self.value.use_prepared_unit
        self.value.use_prepared_unit = True
        for unit in self.value:
            for code in unit['special_data']:
                if type(unit['special_data'][code]) in [int, float]:
                    result[code] = (result[code] if code in result else 0) + unit['special_data'][code]
        self.value.use_prepared_unit = old_use_prepared_unit
        return result