"""02 Високосный год

Напишите программу, которая
- запрашивает у пользователя год
- и проверяет, является ли он високосным.
Год является високосным, если он
- делится на 4 без остатка, и в то же время НЕ делится на 100 без остатка.
- При этом если год делятся на 400 без остатка, он тоже является високосным.

Выведите соответствующее сообщение на экран с помощью функции print.

⚠️ ВАЖНО: при решении использовать ТОЛЬКО конструкцию if - elif - else

* Попробуйте решить задача двумя способами:
 - 1. c вложенными операторами if
 - 2. с помощью логических операторов and / or

"""

# ===== Variant 1: vlojennye if =====
year = int(input("Vvedite god: "))

if year % 4 == 0:
    if year % 100 != 0:
        print(
            "Visokosnyy god"
        )  # poetomu: delitsya na 4 i NE delitsya na 100 → visokosnyy
    else:
        if year % 400 == 0:  # iskluchenie: esli delitsya na 400 → vse ravno visokosnyy
            print("Visokosnyy god")  # naprimer 2000 god
        else:
            print("Ne vysokosnyy god")  # delitsya na 100, no ne na 400 → ne visokosnyy
else:
    print("Ne vysokosnyy god")  # ne delitsya na 4 → srazu ne vysokosnyy


# ===== Variant 2: if - elif - else + and/or =====
year = int(input("Введите год: "))  # получаем год от пользователя

if (year % 4 == 0 and year % 100 != 0) or (
    year % 400 == 0
):  # главная формула високосного года
    print("Visokosnyy god")  # vypolnyaetsya esli uslovie istinno
elif year % 100 == 0:  # esli delitsya na 100 (i ne popal vyshe)
    print("Ne vysokosnyy god")  # znachit ne vysokosnyy (naprimer 1900)
else:
    print("Ne vysokosnyy god")  # vse ostalnye sluchai tozhe ne vysokosnye
