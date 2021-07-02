# Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.
# По окончанию рабочего дня имеем файл data/sold.txt.
# Узнайте:
# 1. На какую сумму было продано товаров
# 2. Цену самого дорогого товара
# 3. Цену самого дешевого товара
sum_price = 0
max_price = 0
with open("data/sold.txt", "r", encoding="utf-8") as file:
    l =[]
    for f in file:
        l += (f.rstrip().split(" "))
min_price = float(l[0])
print(l)
for i in l:
    sum_price += float(i)
    if float(i) > max_price:
        max_price = float(i)
    if float(i) < min_price:
        min_price = float(i)

print("На какую сумму было продано товаров:", sum_price)
print("Цена самого дорогого товара:", max_price)
print("Цена самого дешевого товара:", min_price)
