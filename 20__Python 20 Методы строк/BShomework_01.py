""" 01 Звёздочки вместо чисел

Напишите программу, которая заменяет все цифры в строке на звёздочки *.

text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""

text = "My number is 123-456-789"
print("Строка:", text)
# вариант 1
#result = ""
#for char in text:
#    if char.isdigit():   # если символ — цифра
#        result += "*"
#    else:
#        result += char
#print("Результат:", result)

# вариант 2
#text = "My number is 123-456-789"
#print("Строка:", text)
#result = text
#for digit in "0123456789":
#    result = result.replace(digit, "*")
#print("Результат:", result)

# вариант 3
#text = "My number is 123-456-789"
#print("Строка:", text)

# разбиваем строку на символы (получаем список символов)
chars = list(text)

# обрабатываем каждый символ в списке (заменяем цифры на звёздочки)
for i in range(len(chars)):
    if chars[i].isdigit():
        chars[i] = "*"

# собираем обратно в строку (склеиваем символы в строку)
result = "".join(chars)

print("Результат:", result)