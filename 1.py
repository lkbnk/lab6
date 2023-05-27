dictionary = {"Нидерланды": "Амстердам",
              "Андорра": "Андорра-ла-Велья",
              "Греция": "Афины",
              "Сербия": "Белград",
              "Швейцария": "Берн",
              "Словакия": "Братислава",
              "Бельгия": "Брюссель",
              "Венгрия": "Будапешт",
              "Румыния": "Бухарест"}
print(dictionary, "\n")

country = input(str("Введите страну: "))
if country in dictionary:
    print("Столица - ", dictionary[country], "\n")
else:
    print("Этой страны нет в словаре", "\n")

for capital in sorted(dictionary):
    print(capital, " - ", dictionary[capital])
