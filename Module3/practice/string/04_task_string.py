# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
i = 0
arr_str = text.split(" ")
count = 0
while i < len(arr_str):
    if len(arr_str[i]) > 5:
        count += 1
    i += 1
print(count)
