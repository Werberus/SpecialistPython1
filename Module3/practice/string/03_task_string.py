# Подсчитать количество букв «а» во введенной строке

s = input("string: ")
i = 0
count = 0
while i < len(s):
    if s[i] == "а":
        count += 1
    i += 1
print(count)
