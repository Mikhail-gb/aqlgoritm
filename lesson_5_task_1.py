"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего
и ниже среднего.
"""
from collections import OrderedDict

y = OrderedDict()
countCompany = int(input('Введите количество предприятий: '))
x = 1
sum_profit = 0
while x <= countCompany:
    name = input('Введите название компании: ')
    profit_1 = int(input('Введите прибыль компании за 1 квартал: '))
    profit_2 = int(input('Введите прибыль компании за 2 квартал: '))
    profit_3 = int(input('Введите прибыль компании за 3 квартал: '))
    profit_4 = int(input('Введите прибыль компании за 4 квартал: '))
    profit = profit_1 + profit_2 + profit_3 + profit_4
    y.update({name: profit})
    sum_profit += profit
    x += 1
medium = sum_profit / countCompany
before = []
after = []
for k, v in y.items():
    if v > medium:
        after.append(k)
    elif v < medium:
        before.append(k)

print(f'Средняя прибыль составила {medium} рублей')
print(f'Прибыль выше среднего получили следующие компании: {",".join(after)}')
print(f'Прибыль ниже среднего получили следующие компании: {",".join(before)}')