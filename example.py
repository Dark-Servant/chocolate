from  chocolate import *

impurity_list = ImpurityList()

MASS_VALUE = 150
powder_full_mass = FullMass(MASS_VALUE)
powder_full_mass.first_oil_percent = .2
powder_full_mass.special_oil_percent = .5
powder_full_mass.special_part_percent = .75

grated_full_mass = FullMass(MASS_VALUE)
grated_full_mass.first_oil_percent = .53
grated_full_mass.special_oil_percent = .5
grated_full_mass.special_part_percent = .75

impurity = ImpurityPart(0)
impurity.main_percent = 0
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из какао-порошка 20%', sugar=MASS_VALUE * .2)

impurity = ImpurityPart(0)
impurity.main_percent = 0
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из тёртого какао', sugar=MASS_VALUE * .3)

impurity = ImpurityPart({'whey protein': 1})
impurity.main_percent = .5
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из какао-порошка 20% c сывороточным протеином', sugar=MASS_VALUE * .2)

impurity = ImpurityPart({'whey protein': 1})
impurity.main_percent = .5
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из тёртого какао c сывороточным протеином', sugar=MASS_VALUE * .25)

impurity = ImpurityPart({'milk': 1})
impurity.main_percent = .65
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад из какао-порошка 20%', sugar=MASS_VALUE * .1)

impurity = ImpurityPart({'milk': .65, 'coffee': .35})
impurity.main_percent = .65
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад с кофе из какао-порошка 20%', sugar=MASS_VALUE * .15)

impurity = ImpurityPart({'milk': 1})
impurity.main_percent = .65
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад из тёртого какао', sugar=MASS_VALUE * .15)

impurity = ImpurityPart({'milk': .65, 'coffee': .35})
impurity.main_percent = .65
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад с кофе из тёртого какао', sugar=MASS_VALUE * .2)

impurity = ImpurityPart({'milk': .55, 'whey protein': .45})
impurity.main_percent = .65
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад из какао-порошка 20% c сывороточным протеином', sugar=MASS_VALUE * .15)

impurity = ImpurityPart({'milk': .45, 'coffee': .25, 'whey protein': .3})
impurity.main_percent = .7
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад с кофе и сывороточным протеином из какао-порошка 20%', sugar=MASS_VALUE * .15)

impurity = ImpurityPart({'milk': .55, 'whey protein': .45})
impurity.main_percent = .65
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад из тёртого какао c сывороточным протеином', sugar=MASS_VALUE * .2)

impurity = ImpurityPart({'milk': .45, 'coffee': .25, 'whey protein': .3})
impurity.main_percent = .7
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Молочный шоколад с кофе и сывороточным протеином из тёртого какао', sugar=MASS_VALUE * .2)

impurity = ImpurityPart({'coffee': 1})
impurity.main_percent = .5
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из какао-порошка 20% с кофе', sugar=MASS_VALUE * .25)

impurity = ImpurityPart({'coffee': 1})
impurity.main_percent = .5
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из тёртого какао с кофе', sugar=MASS_VALUE * .35)

impurity = ImpurityPart({'coffee': .5, 'whey protein': .5})
impurity.main_percent = .65
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из какао-порошка 20% с кофе и сывороточным протеином', sugar=MASS_VALUE * .2)

impurity = ImpurityPart({'coffee': .5, 'whey protein': .5})
impurity.main_percent = .65
impurity.full_mass = grated_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Тёмный шоколад из тёртого какао с кофе и сывороточным протеином', sugar=MASS_VALUE * .3)

impurity = ImpurityPart({'milk': .65, 'coffee': .35})
impurity.main_percent = 1
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Белый шоколад с кофе', sugar=MASS_VALUE * .2)

impurity = ImpurityPart({'milk': .55, 'whey protein': .45})
impurity.main_percent = 1
impurity.full_mass = powder_full_mass
impurity_list.append(impurity).setLastUnitSpecialData(name='Белый шоколад с сывороточным протеином', sugar=MASS_VALUE * .15)