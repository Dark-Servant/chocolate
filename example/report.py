from chocolate.example import *

def PrintImpurityList():
    global impurity_list
    # ************************************* REPORT FOR EVERY UNIT
    impurity_list.use_prepared_unit = True
    for unit in impurity_list:
        name = unit['special_data']['name'] if 'name' in unit['special_data'] else '!!!! NO TITLE'
        print('****************** %s' % (name))
        data = {code: unit[code] for code in unit if code not in ['impurity', 'special_data']}
        data.update({'impurity_%s' % (code): unit['impurity'][code] for code in unit['impurity'] if unit['impurity'][code] > 0})
        data['oil_mass'] = sum(data['oil_mass'].values())
        data['sugar'] = unit['special_data']['sugar'] if 'sugar' in unit['special_data'] else 0
        print('\n'.join(['%s: %.2f' % (code, data[code]) for code in data]) + '\n')

    # ************************************* FINAL FULL REPORT
    print('\n%s RESULT DATA' % ('*' * 60))
    report = chocolate.ImpurityReport(impurity_list)

    report_first_mass = report.getFirstMass()
    print('\n'.join(['First mass (%s): %.2f' % (code, report_first_mass[code]) for code in report_first_mass]))

    print('Oil Mass: %.2f' % (report.getOilMass()))

    impurity_mass = report.getImpurityMass()
    print('\n'.join(['Impurity %s: %.2f' % (code, impurity_mass[code]) for code in impurity_mass if impurity_mass[code] > 0]))

    special_mass = report.getNumericSpecialData()
    print('\n'.join(['Special %s: %.2f' % (code, special_mass[code]) for code in special_mass]))