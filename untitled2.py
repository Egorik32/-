# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yAy-JbehV92cqR2Xl9gpxurhLIQeCkFG

1)
"""

a = int(input())
if a == 1:
  print("Январь")
elif a == 2:
  print("Февраль")
elif a == 3:
  print("Март")
elif a == 4:
  print("Апрель")
elif a == 5:
  print("Май")
elif a == 6:
  print("Июнь")
elif a == 7:
  print("Июль")
elif a == 8:
  print("Август")
elif a == 9:
  print("Сентябрь")
elif a == 10:
  print("Октябрь")
elif a == 11:
  print("Ноябрь")
elif a == 12:
  print("Декабрь")
else:
  print("Нет такого месяца!")

"""2)"""

a = int(input())
if a % 2 == 0:
  print("Число чётное")
else:
  print("Число нечётное")

"""3)"""

N = int(input())
if N > 40:
  print("stonks")
else:
  print("not stonks")

"""4)"""

is_year_leap = int(input())
if is_year_leap % 4 == 0:
  print(True)
else:
  print(False)

"""5)"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Введите число: "))
print(is_prime(n))

"""6)"""

a, b = float(input()), float(input())

m = (-138 / 2 ) ** 1.3
n = abs( (-69 / 28 ** 5.1) * 4 )

if a / b == 3.6 or b in range(m, n + 1):
  a, b = b, a

print(a, b)

"""7)"""

n1, n2, n3, n4, n5 = float(input()), float(input()), float(input()), float(input()), float(input())
set1 = set()
set1.add(n1)
set1.add(n2)
set1.add(n3)
set1.add(n4)
set1.add(n5)
list1 = list(int(i) for i in range(-256, 1024 + 1))

if len(set1) == 5:
  print('Все числа явлются уникальными')

  count_chet = 0
  count_negative = 0
  count_p = 0

  for chislo in set1:

    if chislo % 2 == 0:
      count_chet += 1

    if chislo < 0:
      count_negative += 1

    if chislo in list1:
      count_p += 1

  if count_chet == 5:
    print('Все числа чётные')
  else:
    print(f'Не все числа чётные, а только {count_chet}')

  if count_negative == 5:
    print('Все числа отрицательные')
  else:
    print(f'Не все числа отрицательные, а только {count_negative}')

  if count_p == 5:
    print('Все числа находятся в заданном промежутке')
  else:
    print(f'Не все числа находлятся в заданном промежутке, а только {count_p}')

else:
  print('Не все числа уникальные')

"""Повышенная сложность"""

a = float(input())
b = float(input())
c = float(input())

res = (a ** 2 + b ** 3) / (4 * (c + 3))
if res % 2 == 0:
  print('Число чётное')
else:
  print('Число нечётное')