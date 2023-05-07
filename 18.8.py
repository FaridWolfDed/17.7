price = 0
i = 0
count_tickets = int(input("Введите количество билетов: "))
if count_tickets <= 0:
    raise ValueError("Некорректное количество билетов")
while i < count_tickets:
    age = int(input(f"Возраст посетителя билета №:{i+1} - "))
    i += 1
    print (i)
    try:
        if age > 100 or age <= 0:
            raise ValueError("Некорректный возраст")
    except ValueError as error:
        print("Некорректный возраст")
        i -= 1
        continue
    else:
        if age < 18:
            print(f"Билет бесплатный, так как посетителю меньше 18 лет")
        elif 18 <= age < 25:
            print(f"Стоимость билета составляет 990 рублей")
            price += 990
        elif age >= 25:
            print(f"Стоимость билета составляет 1390 рублей")
            price += 1390
print(f"Итоговая стоимость билетов составляет: {price} рублей")
if count_tickets > 3:
    price = price*0.9
    print(f"Так как вы зарегистрировали больше 3 посетителей, то на стоимость билетов действует скидка 10%\n" 
          f"Итоговая стоимость билетов со скидкой составляет: {price} рублей")