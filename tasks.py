from random import choice, randint
from math import sqrt, floor
from decimal import Decimal, getcontext
import time

#task 10
print("Задача 10\n\n")
num = int(input("Введите число монет, пожалуйста\n"))
coins = []
for i in range(num):
    coins.append(choice(["eagle","tail"]))

eagle_counter = 0
for coin in coins:
    if coin == "eagle":
        eagle_counter += 1

print("Минимальное количество монет, которое нужно перевернуть: {0}\n----------\n"
      .format(eagle_counter if eagle_counter < num - eagle_counter else num - eagle_counter))

#task 12
print("Задача 12\n")
print("Задумайте два натуральных числа <= 1000")
s = int(input("Введите сумму этих чисел\n"))
p = int(input("Введите произведение этих чисел\n"))
x = s/2 + sqrt((s/2)**2 - p)
y = s - x
rs = input("Ваши числа это {0} и {1}, я угадал? (y/n)".format(int(x),int(y)))
if rs == "y":
    print ("То то же")
elif rs == "n":
    print ("Да ладно?")
else:
    print ("Вы кажется, перегрелись")
print ("\n----------\n")

#task 14
print("Задача 14\n")
n = int(input("Введите число N\n"))
print("Вывожу все целые степени двойки, не превосходящие N:\n")
x = 0
while 2**x <= n:
    print ("2 в степени {0} = {1}".format(x,2**x))
    x += 1
print ("\n----------\n")

#task 1 add
print("Задача 1 дополнительная\n")
n = Decimal(input("Введите любое целое или вещественное число c точностью до {0} знаков после запятой \n".format(getcontext().prec)))
remainder = n - floor(n)
n = floor(n)
s = 0
if remainder > 0:
    print("Нецелая часть числа = {0}".format(remainder))
    while remainder > 0:
        s += floor(remainder*10)
        remainder = remainder*10 - floor(remainder*10)
    print("Сумма цифр остатка = {0}".format(s))
while n > 0:
    s += n % 10
    n = n // 10
print("Общая сумма цифр в числе = {0}".format(s))
print ("\n----------\n")

#task 2 add
print("Задача 2 дополнительная\n")
start = time.time()
for case in range(100):
    #количество предикат
    n = randint(3,15)
    #генерируем предикаты
    predicates = []
    for i in range(n):
        predicates.append(choice([True, False]))
    #проверяем утверждение
    rs1 = predicates[0]
    rs2 = not predicates[0]
    for p in predicates[1:]:
        rs1 = rs1 or p
        rs2 = rs2 and not p
    rs1 = not rs1
    print("Случай {0}, количество предикатов {1}, результат сравнения {2}".format(case+1,n,rs1==rs2))
end = time.time()
print("Выполнение программы заняло {0} секунд".format(end-start))
print ("\n----------\n")

#task 3 add
print("Задача 3 дополнительная\n")
def all_divisors(number):
    rs = []
    x = number
    while x > 0:
        if number % x == 0:
            rs.append(x)
        x -= 1
    rs = sorted(rs,reverse = True)
    return rs
print ("Положительные делители числа 23436: {0}".format(all_divisors(23436)))
print ("Положительные делители числа 190187200: {0}".format(all_divisors(190187200)))
#можно посчитать, но очень долго
#print ("Положительные делители числа 380457890232: {0}".format(all_divisors(380457890232)))
n = int(input("Введите любое число:\n"))
print ("Положительные делители числа {0}: {1}".format(n, all_divisors(n)))
print ("\n----------\n")
