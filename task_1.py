print('Задача 1. Сумма чисел\n')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15

def summa_n(n):
    result = int((n ** 2 + n) / 2)
    print(f"\nЯ знаю, что сумма чисел от 1 до {n} равна {result}")

summa_n(int(input("Введите число: ")))
