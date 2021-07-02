# Иван кладет в банк x рублей под a процентов годовых на n лет. Напишите функцию, которая возвращает
# число - сколько денег получит Иван в результате.
# функция принимает три числа и возвращает одно - итоговая сумма на счету Ивана.
# Проценты на вклад начисляются один раз в год.

def deposit(x, a, n):
    n -= 1
    x += x * (a / 100)
    if n > 0:
        x = deposit(x, a, n)
    return round(x, 2)


print(deposit(1000, 5, 10))
