# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1

# n = int(input("Введите число элементов в массиве: "))
# A=list()
# for i in range(n):
#     a=int(input("Введите число списка: "))
#     A.append(a)
# print(A)
# X = int(input("Введите число, которое необходимо найти в списке: "))
# count = 0
# for i in range(n):
#     if A[i] == X:
#         count += 1
# print(f"Число {X} встречается в списке A {count} раз") 


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# n = int(input("Введите число элементов в массиве: "))
# A=list()
# for i in range(n):
#     a=int(input("Введите число списка: "))
#     A.append(a)
# print(A)

# X = int(input("Задайте число X, с которым необходимо сравнивать элементы списка: "))
# min = abs(X - A[0])
# index = 0
# for i in range(1, n):
#     count = abs(X - A[i])
#     if count < min:
#         min = count
#         index = i
# print(f"Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}")


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*

# ноутбук
#     12

# list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}

# word = input("Введите слово: ").upper()
# summ = 0
# for i in word:
#     for k, v in list_letters.items():
#         if i in v:
#             summ += k
# print(f"Стоимость слова: {summ}")
