import chocolate

try:
    MASS_VALUE

except NameError:
    MASS_VALUE = 150

try:
    impurity_list

except NameError:
    impurity_list = chocolate.ImpurityList()

try:
    powder_full_mass

except NameError:
    powder_full_mass = chocolate.FullMass(MASS_VALUE)
    powder_full_mass.first_oil_percent = .2
    powder_full_mass.special_oil_percent = .5
    powder_full_mass.special_part_percent = .75

try:
    grated_full_mass

except NameError:
    grated_full_mass = chocolate.FullMass(MASS_VALUE)
    grated_full_mass.first_oil_percent = .53
    grated_full_mass.special_oil_percent = .5
    grated_full_mass.special_part_percent = .75
