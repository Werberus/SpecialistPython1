# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    temp_number = number
    number_2 = 0
    while temp_number > 0:
        new_num = temp_number % 10
        temp_number = temp_number // 10
        number_2 = number_2 * 10
        number_2 = number_2 + new_num
    if number_2 == number:
        return True
    return False


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
