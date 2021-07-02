# Дан список с названиями фруктов, орехов и ягод.
# Определите, названий начинающихся на какую(какие) букву(буквы) больше всего.
# Известно, что названия могут начинаться как с заглавной, так и с маленькой буквы.
# Примеры
# Дано: [“ананас”, “кокос”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к” больше.
# Дано: [“ананас”, “яблоко”, “Арбуз”, “киви”, “Клюква”, “банан”, “хурма”]
# Результат: фруктов на букву “к”и “а” больше.
def check_fruits(fruits):
    count = 0
    char = set()
    for fruit in fruits:
        count_new = 0
        for fruit2 in fruits:
            if not fruit2 == fruits:
                if fruit.upper()[0] == fruit2.upper()[0]:
                    count_new += 1
        if count_new > count:
            count = count_new
            char = set()
            char.add(fruit.upper()[0])
        elif count_new == count:
            char.add(fruit.upper()[0])
    return char



print(check_fruits(["ананас", "яокос", "Арбуз", "киви", "Клюква", "банан", "хурма"]))
