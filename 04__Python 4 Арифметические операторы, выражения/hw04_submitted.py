# Python Fundamentals 2025: Homework 3
# 1. Kalkulyator poezdki (s augmented assignment)
# vvod dannyh
distance = float(input("Введите расстояние (км): "))
consumption = float(input("Введите расход топлива (л на 100 км): "))
price_per_liter = float(input("Введите цену за литр топлива: "))
# raschet topliva
fuel_needed = 0
fuel_needed += (distance / 100) * consumption
# raschet stoimosti
total_cost = 0
total_cost += fuel_needed * price_per_liter
# vyvod rezultata
print("Для поездки потребуется топлива:", fuel_needed)
print("Стоимость поездки:", total_cost)

# 2. Razmen summy kupyurami

amount = int(input("Введите сумму: "))
# input() vozvrashchaet str → int() delaet yavnoe preobrazovanie v int

nominal = int(input("Введите номинал купюры: "))
# nominal — celoe chislo (int), znachenie kupyury

notes = amount // nominal
# // — celochislennoe delenie → skolko kupyur nuzhno

remainder = amount % nominal
# % — ostatok ot delenia → neoplachennaya summa

print("Купюр нужно:", notes)
print("Остаток:", remainder)
