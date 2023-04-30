
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))
deposit=[0]*4
deposit[0] = per_cent["ТКБ"]*money//100
deposit[1] = per_cent["СКБ"]*money//100
deposit[2] = per_cent["ВТБ"]*money//100
deposit[3] = per_cent["СБЕР"]*money//100
print(deposit)
print(f"Максимальная сумма, которую вы можете заработать: {max(deposit)}")
