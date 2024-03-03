amount = 0
tickets = int(input("Количество билетов:\n "))
for age in range (tickets):
    age = int(input("Возраст:\n "))
    if age < 18:
        amount += 0
        print("Самым юным посетителям вход бесплатный!")
    elif age >= 18 and age <= 25:
                amount += 990
    elif age > 25:
                amount += 1390
if amount == 0:
    print("Добро пожаловать, самые юные участники конференции!")
else:
    print("Количество билетов - ", tickets)
    if tickets > 3:
            discount = amount / 100 * 10
            print("Ваша скидка - ", discount, "рублей")

print("К оплате (со скидкой) - ", (amount - discount), "рублей")
