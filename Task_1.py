# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14
from math import pi

number_d =  int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {number_d} равно {round(pi, number_d)}')