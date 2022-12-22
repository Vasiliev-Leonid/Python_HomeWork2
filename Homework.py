#Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
#- 6782 -> 23
#- 0,56 -> 11

# num = abs(float(input("Enter your number: ")))
# while num % 1 != 0:
#     num = round(num*10, 3)
# # print(num) 
# sum = 0 
# while num > 0:
#     sum += num % 10 
#     num //= 10
# print(sum)


# Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Enter your number: '))
# factorial = 1
# for i in range(2, n+1):
#     factorial *= i
 
# print(factorial)

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и 
#выведите на экран их сумму.
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Input your number: '))
# seq = dict()
# seq_sum = 0 
# for i in range(1, n+1):
#     seq[i] = round((1+1/i)**i, 2)
# print(f'N={seq}')
# print(f'Sum{sum(seq.values())}')

# OR without of dictionary

# n = int(input("Input your number: "))
# my_list = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# print(f'N= {my_list}\n Sum: {round(sum(my_list), 2)}')


#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random

# num = int(input("Enter your number: "))
# my_list = []
# for i in range(num):
#     my_list.append(random.randint(-num,num))
# print(my_list)

# data = open('file.txt', "w")
# path = "file.txt"  
# data.write('1\n')
# data.write('3\n')
# data.close()
# path = ('file.txt')
# data = open(path, "r")
# mult = 1
# for line in data:
#     mult *= my_list[int(line)]
#     print(line, end='')
# print(mult)

#Реализуйте алгоритм перемешивания списка.

# import random 

# list = [1, 2, 3, 4, 5, "Privet"] 
# random.shuffle(list) 
# print(list)

