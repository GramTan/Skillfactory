money = int(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit.append(int(per_cent.get('ТКБ') * money))
deposit.append(int(per_cent.get('СКБ') * money))
deposit.append(int(per_cent.get('ВТБ') * money))
deposit.append(int(per_cent.get('СБЕР') * money))
print("Максиальная сумма, которую Вы можете заработать - " max(deposit))








