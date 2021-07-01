def palindrome(number):
    return str(number) == str(number)[::-1]

a = 10
b = 1000
count = 0
for i in range(a, b):
    if palindrome(i):
        count += 1
print(count)
