# Два натуральных числа называются дружественными, если каждое из них равно сумме всех натуральных делителей другого
# (само число при этом не рассматривается в качестве собственного делителя).
# Необходимо найти все пары натуральных дружественных чисел (не равных друг другу),
# оба числа в которых меньше вводимого с клавиатуры числа N.
# Дано натуральное число n, требуется проверить его на простоту.

# Формат входных данных: Вводится одно целое число N (1≤N≤10000).
# Формат выходных данных: Требуется вывести все пары дружественных чисел,
# удовлетворяющие условию задачи. Пары можно выводить в любом порядке.

# Пример:
# Входные данные
# 300
# Выходные данные
#
# 220 284
# 284 220

num = int(input("Введите целое i: "))
first_friend = 1

while first_friend <= num:
    second_friend = 1
    sum1 = 0
    while second_friend < first_friend:
        if first_friend % second_friend == 0:
            sum1 += second_friend
        second_friend += 1
    second_friend = 1
    sum2 = 0
    while second_friend < sum1:
        if sum1 % second_friend == 0:
            sum2 += second_friend
        second_friend += 1
    if sum2 == first_friend and sum1 == second_friend and first_friend != second_friend:
        print(first_friend, second_friend)
    first_friend += 1
