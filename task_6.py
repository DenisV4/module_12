print('Задача 6. НОД\n')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def print_gcd(first, second):
    a, b = first, second
    while a != 0:
        a, b = b % a, a

    print(f"\nНаибольший общий делитель чисел {first} и {second} = {b}")

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

print_gcd(first_num, second_num)
