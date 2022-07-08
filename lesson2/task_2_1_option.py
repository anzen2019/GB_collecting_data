def findSalary(salaryField):
    salary = {'min': 0, 'max': 0, 'Валюта': ""} #начальные условия - если ничего не задано
    if salaryField:
        salaryArr = salaryField.text.replace('\u202f', '').split(" ")
        if salaryArr[0] == 'от':
            salary['min'] = salaryArr[1]
        else:
            if salaryArr[0] == 'до':
                salary['max'] = int(salaryArr[1])
            else:
                salary['min'] = int(salaryArr[0])
                salary['max'] = int(salaryArr[2])
        salary['currency'] = salaryArr[-1]
    return salary